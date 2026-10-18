"""Gemma-backed memory extractor and entity resolution module.
Classifies user messages and extracts structured facts, corrections, overrides, claims, or competing notes.
Entities (wells, areas, users, inspections) are resolved strictly via DuckDB, without regex intent matching.
"""
import re
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union
import duckdb
from pydantic import BaseModel, Field

from backend.app.agent.llm import GemmaClient
from backend.app.config import GEMMA_MODEL_FAST

class MessageClassification(str, Enum):
    QUESTION = "question"
    SHARED_FACT = "shared_fact"
    CORRECTION = "correction"
    RULE_OVERRIDE = "rule_override"
    USER_CLAIM = "user_claim"
    COMPETING_NOTE = "competing_note"

class ExtractedMemoryItem(BaseModel):
    classification: MessageClassification = Field(
        description="Classification: 'question' for queries; 'shared_fact' for FYI/announcements/downtime notes; "
                    "'correction' for explicit corrections to readings, volumes, or data; 'rule_override' for rule/threshold changes; "
                    "'user_claim' for operational status assertions (running fine, back online); 'competing_note' for inquiries on disputed notes/oil vs water."
    )
    target: Optional[str] = Field(
        default=None,
        description="Target well ID (e.g. 'WELL-0164'), well type ('T350', 'T200'), inspection ID ('INS-0151-0201'), or area."
    )
    field: Optional[str] = Field(
        default=None,
        description="The field being addressed or corrected, e.g. 'wellhead_temp_c', 'spill_est_volume_bbl', 'rca_repair_count_threshold', 'operational_status'."
    )
    original_value: Optional[Union[float, str]] = Field(
        default=None,
        description="Original or previous value stated or referenced (e.g. 24.0, 4.5, 3)."
    )
    new_value: Optional[Union[float, str]] = Field(
        default=None,
        description="New value stated, corrected, or commanded (e.g. 41.0, 5.4, 2)."
    )
    unit: Optional[str] = Field(
        default=None,
        description="Unit of measurement, e.g. '°C', 'bbl', 'repairs', 'days', 'hours'."
    )
    scope: Optional[str] = Field(
        default=None,
        description="Scope of application: 'fleet', 'T200', 'T350', or 'well'."
    )
    reason: Optional[str] = Field(
        default=None,
        description="Reason given by user for the statement, correction, or override."
    )
    dates: Optional[List[str]] = Field(
        default_factory=list,
        description="Any specific dates or timestamps mentioned in the statement (e.g. ['15 Oct', '24 Sep'])."
    )


def is_pure_query_without_statement(message: str) -> bool:
    """Cheap syntactic check to see if message is purely a single question without statements or notes.
    
    Returns True ONLY if message has no assertive statements or note-related dispute inquiries.
    """
    clean = message.strip()
    if not clean.endswith("?"):
        return False
    
    # Check for multiple sentences / clauses
    sentences = [s.strip() for s in re.split(r'[.!;\n]', clean) if s.strip()]
    if len(sentences) > 1:
        return False

    low = clean.lower()
    # If the inquiry asks about real oil vs water, disputed analysis, or claims, do not skip
    if any(k in low for k in ["real oil", "water", "dispute", "competing", "agree", "disagree", "claim"]):
        return False

    # Check if starts with typical pure question words
    pure_question_starters = (
        "what", "which", "how", "where", "when", "who", "show", "is", "are", 
        "can", "could", "list", "does", "do", "will", "why", "give"
    )
    return any(low.startswith(w) for w in pure_question_starters)


def resolve_well_db(conn: duckdb.DuckDBPyConnection, target_str: Optional[str]) -> Optional[str]:
    """Resolves target string to canonical WELL-xxxx format strictly via DB lookups."""
    if not target_str:
        return None
    s = target_str.strip()

    # Exact or lowercase match on asset_id
    row = conn.execute("SELECT asset_id FROM wells WHERE LOWER(asset_id) = LOWER(?)", [s]).fetchone()
    if row:
        return row[0]

    # Match by digits if present (e.g. '164', '0164', 'well-164')
    digits = re.findall(r'\d+', s)
    if digits:
        canonical = f"WELL-{int(digits[-1]):04d}"
        row = conn.execute("SELECT asset_id FROM wells WHERE asset_id = ?", [canonical]).fetchone()
        if row:
            return row[0]

    # Match by name
    row = conn.execute("SELECT asset_id FROM wells WHERE LOWER(name) = LOWER(?)", [s]).fetchone()
    if row:
        return row[0]

    return None


def resolve_area_db(conn: duckdb.DuckDBPyConnection, area_str: Optional[str]) -> Optional[str]:
    """Resolves area name strictly from areas table in DuckDB."""
    if not area_str:
        return None
    s = area_str.strip().lower()

    areas = conn.execute("SELECT name FROM areas").fetchall()
    for (a_name,) in areas:
        if a_name.lower() in s or s in a_name.lower():
            return a_name
    return None


def resolve_user_name_db(conn: duckdb.DuckDBPyConnection, user_id: str) -> str:
    """Resolves user display name from users table."""
    row = conn.execute("SELECT name FROM users WHERE user_id = ?", [user_id]).fetchone()
    return row[0] if row else user_id


def extract_memory_with_gemma(
    client: GemmaClient,
    user_message: str,
    model: Optional[str] = None,
) -> ExtractedMemoryItem:
    """Calls Gemma with role='memory_extractor' and returns structured ExtractedMemoryItem.
    
    Validated with Pydantic and one retry on failure.
    """
    model_name = model or GEMMA_MODEL_FAST

    prompt = (
        "You are the memory extractor for an Asset Intelligence Copilot.\n"
        "Analyze the user's message and classify it into exactly one category:\n"
        "- question: user is querying records or asking for information (e.g. 'Is the well producing oil?').\n"
        "- shared_fact: user is announcing or sharing a note/schedule across the team (e.g. 'FYI for everyone: the well will be shut in...').\n"
        "- correction: user is explicitly correcting an erroneous measurement, sensor reading, or AI volume estimate (e.g. 'reading for the well is wrong...').\n"
        "- rule_override: user is commanding a team or type-wide rule modification (e.g. 'Note for all T350 wells: RCA after 2 repairs, not 3').\n"
        "- user_claim: user is making an assertion about an asset's operating status (e.g. 'the well is running fine', 'the well is back online').\n"
        "- competing_note: user is inquiring about conflicting notes or disputed oil vs water classification (e.g. 'Was the spill real crude oil?').\n\n"
        "Extract:\n"
        "- target: well ID (e.g. 'WELL-0164'), well type ('T350', 'T200'), inspection ID, or area.\n"
        "- field: the field name being addressed (e.g. 'wellhead_temp_c', 'spill_est_volume_bbl', 'rca_repair_count_threshold', 'status').\n"
        "- original_value: original/previous value stated or referenced (numeric or string).\n"
        "- new_value: new value stated, corrected, or commanded (numeric or string).\n"
        "- unit: unit of measurement (e.g. '°C', 'bbl', 'repairs', 'days', 'hours').\n"
        "- scope: 'fleet', 'T200', 'T350', or 'well'.\n"
        "- reason: the stated reason or explanation from the user.\n"
        "- dates: any specific dates mentioned (e.g. ['15 Oct', '24 Sep', '20 Aug']).\n\n"
        f"User Message:\n\"{user_message}\""
    )

    return client.generate_json(
        prompt=prompt,
        response_schema=ExtractedMemoryItem,
        model=model_name,
        role="memory_extractor",
        use_cache=True,
    )
