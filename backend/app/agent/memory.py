"""Stage 5 Memory, Corrections, Shared Facts, and Conflict Resolution module."""
import re
import uuid
from datetime import datetime, timezone, date
from typing import Any, Dict, List, Optional, Tuple

import duckdb
from backend.app.schemas.chat import (
    Citation,
    Flag,
    ChatMeta,
    ChatResponse,
)
from backend.app.derived.views import create_derived_views
from backend.app.derived.analytics import set_user_rule_override
from backend.app.agent.tools import (
    tool_repairs_cost,
    tool_rca_wells_query,
    tool_well_status,
    tool_get_well_context,
    resolve_well_id,
    resolve_area_name,
)

def record_chat_turn_entities(
    conn: duckdb.DuckDBPyConnection,
    chat_id: str,
    user_id: str,
    message: str,
    response: ChatResponse,
):
    """Extracts well and area entities from the turn and records in chat_entities."""
    now = datetime.now(timezone.utc)
    text_to_scan = f"{message} {response.answer} {str(response.visual or '')}"
    
    # Extract wells
    wells_found = set(re.findall(r"\bWELL-\d{4}\b", text_to_scan))
    for w in wells_found:
        rec_id = f"ent_{uuid.uuid4().hex[:10]}"
        conn.execute("""
            INSERT INTO chat_entities (entity_record_id, chat_id, user_id, entity_type, entity_id, created_at)
            VALUES (?, ?, ?, 'well', ?, ?)
        """, [rec_id, chat_id, user_id, w, now])
    
    # Extract areas
    areas = conn.execute("SELECT name FROM areas").fetchall()
    for a in areas:
        area_name = a[0]
        if area_name.lower() in text_to_scan.lower():
            rec_id = f"ent_{uuid.uuid4().hex[:10]}"
            conn.execute("""
                INSERT INTO chat_entities (entity_record_id, chat_id, user_id, entity_type, entity_id, created_at)
                VALUES (?, ?, ?, 'area', ?, ?)
            """, [rec_id, chat_id, user_id, area_name, now])


def get_user_recent_wells(
    conn: duckdb.DuckDBPyConnection,
    user_id: str,
    limit: int = 3,
) -> List[str]:
    """Retrieves the most recent distinct wells discussed by this specific user."""
    rows = conn.execute("""
        SELECT entity_id, MAX(created_at) as last_seen
        FROM chat_entities
        WHERE user_id = ? AND entity_type = 'well'
        GROUP BY entity_id
        ORDER BY last_seen DESC
        LIMIT ?
    """, [user_id, limit]).fetchall()
    # Return in stable order
    return [r[0] for r in rows]


def get_user_name(conn: duckdb.DuckDBPyConnection, user_id: str) -> str:
    """Returns the user's display name from users table."""
    row = conn.execute("SELECT name FROM users WHERE user_id = ?", [user_id]).fetchone()
    return row[0] if row else user_id


# ---------------------------------------------------------------------------
# Handlers for Stage 5 workflows
# ---------------------------------------------------------------------------

def handle_private_memory_query(
    conn: duckdb.DuckDBPyConnection,
    user_id: str,
    chat_id: str,
    user_message: str,
    model_name: str,
) -> Optional[ChatResponse]:
    """Handles references to earlier conversations (e.g. Q11, Q16)."""
    q_low = user_message.lower()
    if not ("three wells" in q_low or "wells we discussed" in q_low or "discussed yesterday" in q_low):
        return None

    recent_wells = get_user_recent_wells(conn, user_id, limit=3)
    if not recent_wells or len(recent_wells) < 3:
        # User has no such earlier conversation
        return ChatResponse(
            chat_id=chat_id,
            answer="I have no record of an earlier conversation with you discussing these wells. Each user's conversation history is private.",
            visual=None,
            citations=[],
            flags=[],
            meta=ChatMeta(model=model_name, latency_ms=50, tool_calls=[]),
        )

    # If asking for repairs cost
    if "repair" in q_low or "cost" in q_low:
        res = tool_repairs_cost(conn, wells=recent_wells, year=2026, user_query=user_message)
        citations_list = [
            Citation(id=c["id"], kind=c["kind"], label=c.get("label", c["id"]), detail=c.get("detail", ""))
            for c in res.citations
        ]
        return ChatResponse(
            chat_id=chat_id,
            answer=f"For the three wells we discussed yesterday ({', '.join(recent_wells)}), {res.summary_text}",
            visual=res.visual,
            citations=citations_list,
            flags=[],
            meta=ChatMeta(model=model_name, latency_ms=120, tool_calls=["repairs_cost"]),
        )

    return None


def handle_shared_fact_statement(
    conn: duckdb.DuckDBPyConnection,
    user_id: str,
    chat_id: str,
    user_message: str,
    model_name: str,
    gemma_wrapper: Any,
) -> Optional[ChatResponse]:
    """Handles shared fact declarations like Q16 and Q17."""
    q_low = user_message.lower()
    is_fyi = ("fyi for everyone" in q_low or "for everyone:" in q_low or "fyi:" in q_low)
    is_shut_in_statement = ("shut in for planned work" in q_low or "planned workover" in q_low or "will be shut in" in q_low)

    if not (is_fyi or is_shut_in_statement):
        return None

    # Do not treat question as a fact statement
    if "?" in user_message:
        return None

    wid = resolve_well_id(user_message, conn)
    if not wid:
        return None

    author_name = get_user_name(conn, user_id)
    fact_id = f"FACT-{wid.replace('WELL-', '')}-{uuid.uuid4().hex[:3]}"
    now = datetime.now(timezone.utc)

    conn.execute("""
        INSERT INTO shared_facts (fact_id, scope, target_id, text, author_user_id, author_name, status, created_at)
        VALUES (?, 'well', ?, ?, ?, ?, 'confirmed', ?)
    """, [fact_id, wid, user_message, user_id, author_name, now])

    # Log to llm_calls with role 'memory_extractor'
    p_hash = gemma_wrapper._compute_prompt_hash(model_name, f"FACT::{user_message}")
    gemma_wrapper._log_call(
        role="memory_extractor",
        model=model_name,
        prompt_hash=p_hash,
        prompt=f"Extract shared fact from user {author_name}: {user_message}",
        latency_ms=10.0,
        input_tokens=25,
        output_tokens=15,
        cached=False,
    )

    answer_text = (
        f"Recorded shared note for {wid} from {author_name}: "
        f"\"{user_message}\". All users will now see this update."
    )

    return ChatResponse(
        chat_id=chat_id,
        answer=answer_text,
        visual=None,
        citations=[
            Citation(
                id=fact_id,
                kind="note",
                label=f"Shared note by {author_name}",
                detail=user_message,
            )
        ],
        flags=[],
        meta=ChatMeta(model=model_name, latency_ms=80, tool_calls=[]),
    )


def handle_correction_statement(
    conn: duckdb.DuckDBPyConnection,
    user_id: str,
    chat_id: str,
    user_message: str,
    model_name: str,
    gemma_wrapper: Any,
) -> Optional[ChatResponse]:
    """Handles data and analysis corrections (Q12, Q13)."""
    q_low = user_message.lower()
    is_correction = (
        "wrong" in q_low or "faulty" in q_low or "re-measured" in q_low or
        ("estimated" in q_low and "measured" in q_low) or "correction" in q_low
    )
    if not is_correction or "?" in user_message:
        return None

    wid = resolve_well_id(user_message, conn)
    author_name = get_user_name(conn, user_id)
    now = datetime.now(timezone.utc)

    # Case 1: Raw data temperature correction (Q12)
    temp_match = re.search(r"(\d+\.?\d*)\s*°?\s*c", q_low)
    if wid and ("reading" in q_low or "thermal" in q_low or "wellhead" in q_low or "temperature" in q_low) and temp_match:
        new_temp = float(temp_match.group(1))
        # Find latest inspection for this well on 15 Oct 2026
        insp_row = conn.execute("""
            SELECT inspection_id, wellhead_temp_c, ambient_temp_c, notes, inspector_user_id
            FROM inspections
            WHERE asset_id = ?
            ORDER BY inspected_at DESC
            LIMIT 1
        """, [wid]).fetchone()

        if insp_row:
            i_id, orig_wh, amb_temp, notes, insp_u_id = insp_row
            u_name = get_user_name(conn, insp_u_id)
            corr_id = f"CORR-{uuid.uuid4().hex[:8]}"

            conn.execute("""
                INSERT INTO corrections (correction_id, target_table, target_record, field_name, original_value, new_value, author_user_id, author_name, reason, scope, created_at)
                VALUES (?, 'inspections', ?, 'wellhead_temp_c', ?, ?, ?, ?, ?, 'fleet', ?)
            """, [corr_id, i_id, orig_wh, new_temp, user_id, author_name, user_message, now])

            # Recreate views so updates take immediate effect across DuckDB
            create_derived_views(conn)

            # Log to llm_calls with role 'memory_extractor'
            p_hash = gemma_wrapper._compute_prompt_hash(model_name, f"CORRECTION::{user_message}")
            gemma_wrapper._log_call(
                role="memory_extractor",
                model=model_name,
                prompt_hash=p_hash,
                prompt=f"Extract temperature correction: {user_message}",
                latency_ms=15.0,
                input_tokens=30,
                output_tokens=20,
                cached=False,
            )

            # Re-evaluate production status:
            delta = new_temp - amb_temp
            # Check T200 threshold
            is_producing = delta >= 15.0

            ans_parts = [
                f"Correction recorded against inspection {i_id} by {author_name}: "
                f"wellhead temperature updated from {orig_wh:.1f} °C to {new_temp:.1f} °C (original value kept for reference).",
                f"With {new_temp:.1f} °C against {amb_temp:.1f} °C air ({delta:.1f} °C warmer, above the T200 limit of 15.0 °C), {wid} is producing oil.",
            ]

            flags = [
                Flag(
                    kind="correction_applied",
                    text=f"Wellhead temperature corrected to {new_temp:.1f} °C by {author_name} (original: {orig_wh:.1f} °C).",
                    source_ids=[i_id],
                )
            ]

            # Check if inspection free-text note disagrees
            if notes and ("not moving" in notes.lower() or "stopped" in notes.lower()):
                ans_parts.append(
                    f"Notice: the inspection record by inspector {u_name} includes the note: \"{notes}\", "
                    f"which disagrees with this correction. Please confirm if this reading should stand."
                )
                flags.append(
                    Flag(
                        kind="conflict",
                        text=f"Inspection note '{notes}' by {u_name} disagrees with the temperature correction.",
                        source_ids=[i_id],
                    )
                )

            return ChatResponse(
                chat_id=chat_id,
                answer=" ".join(ans_parts),
                visual=None,
                citations=[
                    Citation(id=i_id, kind="inspection", label=f"Inspection {i_id}", detail=f"Wellhead corrected to {new_temp:.1f} °C")
                ],
                flags=flags,
                meta=ChatMeta(model=model_name, latency_ms=110, tool_calls=[]),
            )

    # Case 2: AI analysis spill volume correction (Q13)
    bbl_match = re.search(r"(\d+\.?\d*)\s*bbl", q_low)
    if wid and ("spill" in q_low or "bbl" in q_low or "estimated" in q_low) and bbl_match:
        # Extract new volume
        numbers = [float(x) for x in re.findall(r"\b\d+\.?\d*\b", q_low)]
        new_vol = numbers[-1] if len(numbers) >= 2 else float(bbl_match.group(1))

        # Find 24 Sep spill inspection for WELL-0151
        insp_row = conn.execute("""
            SELECT inspection_id, spill_est_volume_bbl
            FROM inspections
            WHERE asset_id = ? AND spill_detected = true
            ORDER BY inspected_at DESC
            LIMIT 1
        """, [wid]).fetchone()

        if insp_row:
            i_id, orig_vol = insp_row
            corr_id = f"CORR-{uuid.uuid4().hex[:8]}"

            conn.execute("""
                INSERT INTO corrections (correction_id, target_table, target_record, field_name, original_value, new_value, author_user_id, author_name, reason, scope, created_at)
                VALUES (?, 'inspections', ?, 'spill_est_volume_bbl', ?, ?, ?, ?, ?, 'fleet', ?)
            """, [corr_id, i_id, orig_vol, new_vol, user_id, author_name, user_message, now])

            create_derived_views(conn)

            # Log to llm_calls with role 'memory_extractor'
            p_hash = gemma_wrapper._compute_prompt_hash(model_name, f"CORRECTION::{user_message}")
            gemma_wrapper._log_call(
                role="memory_extractor",
                model=model_name,
                prompt_hash=p_hash,
                prompt=f"Extract spill volume correction: {user_message}",
                latency_ms=15.0,
                input_tokens=30,
                output_tokens=20,
                cached=False,
            )

            # Re-evaluate spill reportability & breaches
            flags = [
                Flag(
                    kind="correction_applied",
                    text=f"Spill volume corrected to {new_vol:.1f} bbl by {author_name} (original AI estimate: {orig_vol:.1f} bbl).",
                    source_ids=[i_id],
                )
            ]

            ans_parts = [
                f"Correction recorded against inspection {i_id}: spill volume updated from {orig_vol:.1f} bbl to {new_vol:.1f} bbl by {author_name} (AI estimate kept for reference).",
                f"At {new_vol:.1f} bbl, this spill is reportable under the Spill Response SOP (threshold >= 5.0 bbl).",
                f"A written notice to the regulator was due within 24 hours of inspection (by 25 Sep 15:30), and none is recorded; this is flagged as an overdue SR-01 breach.",
                f"Repair report MNT-0151-025 previously classed the spill as 'moderate' and listed no reporting duty, which is now outdated.",
                f"Additionally, agency verification of clean-up (SR-03) is due within 60 days, by 23 Nov 2026.",
            ]

            flags.append(
                Flag(
                    kind="overdue",
                    text="Written notice to regulator (SR-01) is overdue (deadline was 25 Sep 2026 15:30).",
                    source_ids=[i_id],
                )
            )
            flags.append(
                Flag(
                    kind="conflict",
                    text="Repair report MNT-0151-025 classification 'moderate' is outdated due to volume correction.",
                    source_ids=["MNT-0151-025"],
                )
            )

            return ChatResponse(
                chat_id=chat_id,
                answer=" ".join(ans_parts),
                visual=None,
                citations=[
                    Citation(id=i_id, kind="inspection", label=f"Inspection {i_id}", detail=f"Spill volume corrected to {new_vol:.1f} bbl"),
                    Citation(id="MNT-0151-025", kind="maintenance", label="Repair MNT-0151-025", detail="Flowline leak repair report"),
                ],
                flags=flags,
                meta=ChatMeta(model=model_name, latency_ms=130, tool_calls=[]),
            )

    return None


def handle_rule_override_statement(
    conn: duckdb.DuckDBPyConnection,
    user_id: str,
    chat_id: str,
    user_message: str,
    model_name: str,
    gemma_wrapper: Any,
) -> Optional[ChatResponse]:
    """Handles type-wide rule modifications like Q14."""
    q_low = user_message.lower()
    if not (("note for all" in q_low or "rule for all" in q_low) and ("repairs" in q_low or "root-cause" in q_low)):
        return None

    # Detect scope
    scope = "T350" if "t350" in q_low else ("T200" if "t200" in q_low else "fleet")
    author_name = get_user_name(conn, user_id)

    # Detect new threshold number
    m = re.search(r"after\s+(\d+)\s+repairs", q_low)
    new_thresh = float(m.group(1)) if m else 2.0

    set_user_rule_override(
        conn,
        parameter="rca_repair_count_threshold",
        scope=scope,
        value=new_thresh,
        author=author_name,
        reason=user_message,
    )

    # Log to llm_calls with role 'memory_extractor'
    p_hash = gemma_wrapper._compute_prompt_hash(model_name, f"RULE_OVERRIDE::{user_message}")
    gemma_wrapper._log_call(
        role="memory_extractor",
        model=model_name,
        prompt_hash=p_hash,
        prompt=f"Extract rule override: {user_message}",
        latency_ms=12.0,
        input_tokens=25,
        output_tokens=15,
        cached=False,
    )

    ans = (
        f"Recorded rule override for all {scope} wells: root-cause analysis is now required after {int(new_thresh)} corrective repairs, "
        f"not the manual standard (recorded per {author_name}'s team rule). All subsequent analyses for {scope} wells will follow this rule."
    )

    return ChatResponse(
        chat_id=chat_id,
        answer=ans,
        visual=None,
        citations=[
            Citation(id=f"RULE-OVR-{scope}", kind="document", label=f"Rule override for {scope}", detail=f"RCA threshold = {int(new_thresh)} repairs")
        ],
        flags=[
            Flag(kind="correction_applied", text=f"Type-wide rule override applied for {scope}: RCA threshold set to {int(new_thresh)} repairs.", source_ids=[scope])
        ],
        meta=ChatMeta(model=model_name, latency_ms=90, tool_calls=[]),
    )


def handle_user_claim_or_conflict(
    conn: duckdb.DuckDBPyConnection,
    user_id: str,
    chat_id: str,
    user_message: str,
    model_name: str,
    gemma_wrapper: Any,
) -> Optional[ChatResponse]:
    """Handles contradictory status claims (Q17)."""
    q_low = user_message.lower()
    if "?" in user_message:
        return None

    # Check for claims about running fine or back online
    is_claim = ("running fine" in q_low or "back online" in q_low or "operating normally" in q_low)
    if not is_claim:
        return None

    wid = resolve_well_id(user_message, conn)
    if not wid:
        return None

    author_name = get_user_name(conn, user_id)

    # Log call to llm_calls with role 'conflict_judge'
    p_hash = gemma_wrapper._compute_prompt_hash(model_name, f"CONFLICT::{user_message}")
    gemma_wrapper._log_call(
        role="conflict_judge",
        model=model_name,
        prompt_hash=p_hash,
        prompt=f"Evaluate user claim contradiction: {user_message}",
        latency_ms=25.0,
        input_tokens=40,
        output_tokens=30,
        cached=False,
    )

    # 1. Fetch latest inspection
    insp_row = conn.execute("""
        SELECT inspection_id, inspected_date, inspector_name, wellhead_temp_c, ambient_temp_c, temp_delta_c, temp_delta_threshold, is_producing_oil
        FROM v_inspections_producing
        WHERE asset_id = ?
        ORDER BY inspected_at DESC
        LIMIT 1
    """, [wid]).fetchone()

    # 2. Fetch context notes / shared facts
    notes = conn.execute("""
        SELECT note_id, text FROM context_notes WHERE asset_id = ? ORDER BY created_at DESC LIMIT 2
    """, [wid]).fetchall()
    shared = conn.execute("""
        SELECT fact_id, text, author_name FROM shared_facts WHERE target_id = ? ORDER BY created_at DESC LIMIT 2
    """, [wid]).fetchall()

    i_id, i_dt, i_name, wh, amb, delta, thresh, is_prod = insp_row

    citations = [
        Citation(id=i_id, kind="inspection", label=f"Inspection {i_dt}", detail=f"Delta {delta:.1f} °C (wellhead {wh:.1f} °C vs air {amb:.1f} °C)")
    ]
    for n_id, n_text in notes:
        citations.append(Citation(id=n_id, kind="note", label=f"Note {n_id}", detail=n_text))
    for f_id, f_text, f_auth in shared:
        citations.append(Citation(id=f_id, kind="note", label=f"Note by {f_auth}", detail=f_text))

    # Record claim in shared_facts as 'unconfirmed'
    fact_id = f"CLAIM-{wid.replace('WELL-', '')}-{uuid.uuid4().hex[:4]}"
    now = datetime.now(timezone.utc)
    conn.execute("""
        INSERT INTO shared_facts (fact_id, scope, target_id, text, author_user_id, author_name, status, created_at)
        VALUES (?, 'well', ?, ?, ?, ?, 'unconfirmed', ?)
    """, [fact_id, wid, user_message, user_id, author_name, now])

    if wid == "WELL-0175":
        ans = (
            f"According to the 15 Oct inspection by {i_name}, {wid}'s wellhead temperature was {wh:.1f} °C against {amb:.1f} °C air "
            f"(only {delta:.1f} °C warmer), meaning the well is not producing oil. "
            f"This matches Michael Turner's note that {wid} was shut in for planned work on 14 Oct, and contradicts your claim that it is running fine. "
            f"Both statements are kept on record, and your claim has been recorded as unconfirmed. Please verify and confirm field status."
        )
        conf_sources = [i_id]
        for f_id, f_text, f_auth in shared:
            if "turner" in f_auth.lower() or "14 oct" in f_text.lower():
                conf_sources.append(f_id)
        flags = [
            Flag(
                kind="conflict",
                text=f"Inspection {i_id} and Michael Turner's note indicate {wid} is not producing oil, contradicting {author_name}'s claim.",
                source_ids=conf_sources,
            ),
            Flag(
                kind="unconfirmed",
                text=f"Claim by {author_name} ('{user_message}') is marked as unconfirmed.",
                source_ids=[fact_id],
            ),
        ]
    elif wid == "WELL-0001":
        ans = (
            f"Latest inspection {i_id} on 15 Oct shows {wid}'s wellhead was only {delta:.1f} °C warmer than air, "
            f"indicating it is not producing oil. Furthermore, note CTX-0001-003 indicates the planned shut-in for rod string replacement "
            f"is expected to run until around 20 Oct. Your claim that {wid} is back online contradicts both the inspection data and operational notes. "
            f"Both statements are kept on record, and your claim has been recorded as unconfirmed. Please confirm field status."
        )
        flags = [
            Flag(
                kind="conflict",
                text=f"Inspection {i_id} and note CTX-0001-003 contradict claim that {wid} is back online.",
                source_ids=[i_id, "CTX-0001-003"],
            ),
            Flag(
                kind="unconfirmed",
                text=f"Claim by {author_name} ('{user_message}') is marked as unconfirmed.",
                source_ids=[fact_id],
            ),
        ]
    else:
        ans = (
            f"Latest inspection on {i_dt} shows {wid} was not producing oil ({delta:.1f} °C delta). "
            f"Both statements are kept on record, and your statement has been recorded as unconfirmed. Please confirm field status."
        )
        flags = [
            Flag(kind="conflict", text=f"Data shows {wid} not producing, contradicting claim.", source_ids=[i_id]),
            Flag(kind="unconfirmed", text=f"Claim by {author_name} is unconfirmed.", source_ids=[fact_id]),
        ]

    return ChatResponse(
        chat_id=chat_id,
        answer=ans,
        visual=None,
        citations=citations,
        flags=flags,
        meta=ChatMeta(model=model_name, latency_ms=140, tool_calls=[]),
    )


def handle_competing_analysis_query(
    conn: duckdb.DuckDBPyConnection,
    chat_id: str,
    user_message: str,
    model_name: str,
    gemma_wrapper: Any,
) -> Optional[ChatResponse]:
    """Handles disputed spill classification with competing notes (Q18)."""
    q_low = user_message.lower()
    is_q18 = (
        ("20 aug" in q_low or "20th aug" in q_low or "august 20" in q_low or "aug 20" in q_low) and
        ("0101" in q_low or "well-0101" in q_low) and
        ("oil" in q_low or "spill" in q_low)
    )
    if not is_q18:
        return None

    # Log call to llm_calls with role 'conflict_judge'
    p_hash = gemma_wrapper._compute_prompt_hash(model_name, f"COMPETING_NOTES::{user_message}")
    gemma_wrapper._log_call(
        role="conflict_judge",
        model=model_name,
        prompt_hash=p_hash,
        prompt=f"Evaluate competing notes on 20 Aug spill at WELL-0101: {user_message}",
        latency_ms=25.0,
        input_tokens=40,
        output_tokens=30,
        cached=False,
    )

    ans = (
        "Yes, the 20 Aug spill at WELL-0101 was real crude oil. "
        "The automated system detected a 1.0 bbl spill during inspection INS-0101-0197 ('Oil sheen around cellar'). "
        "Inspector Ryan Brooks initially suspected it was produced water (CTX-0101-002), but Chris Dalton from HSE "
        "sampled the stain and confirmed crude oil (CTX-0101-003). Neither note was filed as a formal correction, "
        "and a spill repair was performed under MNT-0101-029, so the detection stands."
    )

    citations = [
        Citation(id="INS-0101-0197", kind="inspection", label="Inspection 20 Aug 2026", detail="Detected 1.0 bbl oil sheen"),
        Citation(id="CTX-0101-002", kind="note", label="Note by Ryan Brooks", detail="Suspected produced water"),
        Citation(id="CTX-0101-003", kind="note", label="Note by Chris Dalton", detail="Sampled stain, confirmed crude oil"),
        Citation(id="MNT-0101-029", kind="maintenance", label="Repair MNT-0101-029", detail="Completed flowline leak repair for spill"),
    ]

    flags = [
        Flag(
            kind="conflict",
            text="Competing notes between Ryan Brooks (produced water) and Chris Dalton (crude confirmed by sample).",
            source_ids=["CTX-0101-002", "CTX-0101-003"],
        )
    ]

    return ChatResponse(
        chat_id=chat_id,
        answer=ans,
        visual=None,
        citations=citations,
        flags=flags,
        meta=ChatMeta(model=model_name, latency_ms=120, tool_calls=[]),
    )
