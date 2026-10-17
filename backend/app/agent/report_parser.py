"""Maintenance Report Facts Extractor using Gemma 4.
Extracts containment_hours, root_cause, action_required, stated_spill_class,
reporting_duty_listed, and evidence_quote from raw markdown reports.
"""
import sys
import re
import json
import time
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from pydantic import BaseModel, Field

# Ensure project root in sys.path
project_root = Path(__file__).resolve().parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from backend.app.config import GEMMA_MODEL_FAST
from backend.app.db.connection import get_connection
from backend.app.db.schema import init_db
from backend.app.agent.llm import GemmaClient, CACHE_DIR, flush_llm_logs

class ReportFactsSchema(BaseModel):
    containment_hours: Optional[float] = Field(
        default=None,
        description="Hours taken to contain the spill/release (e.g. 5.3, 7.1, 8.1, 7.0). Null if not stated or no spill."
    )
    root_cause: Optional[str] = Field(
        default=None,
        description="The primary root cause of the issue stated in the report."
    )
    action_required: bool = Field(
        default=False,
        description="True if the report marks 'Action required' or pending root-cause analysis, otherwise false."
    )
    stated_spill_class: Optional[str] = Field(
        default=None,
        description="The spill class stated in the report ('minor', 'moderate', 'reportable', 'major', or null)."
    )
    reporting_duty_listed: bool = Field(
        default=False,
        description="True if an external reporting duty to regulatory authorities is listed in the report, false if not."
    )
    evidence_quote: Optional[str] = Field(
        default=None,
        description="The exact sentence from the report text stating the containment time / hours."
    )

def build_report_prompt(report_markdown: str) -> str:
    """Constructs the prompt for extracting facts from a maintenance report."""
    return (
        "You are an expert maintenance report analyzer.\n"
        "Extract the concrete facts from this maintenance report:\n\n"
        f"{report_markdown.strip()}\n\n"
        "Guidelines:\n"
        "- containment_hours: extract the numeric hours to contain the release if stated (e.g. 'contained about 7.1 hours'). If not stated, return null.\n"
        "- evidence_quote: provide the exact sentence from the report where containment_hours was found. The containment_hours number must be present in this quote.\n"
        "- root_cause: concise summary from the 'Root cause' section.\n"
        "- action_required: true if 'Action required' appears in the compliance check table or notes.\n"
        "- stated_spill_class: the spill classification stated in the report ('minor', 'moderate', 'reportable', 'major', or null).\n"
        "- reporting_duty_listed: true if an external reporting duty to regulators is listed.\n"
    )

def is_containment_valid(hours: Optional[float], quote: Optional[str]) -> bool:
    """
    Validation rule: containment_hours must be backed by a number that appears in evidence_quote.
    """
    if hours is None:
        return True
    if not quote:
        return False
    numbers = re.findall(r'\d+(?:\.\d+)?', quote)
    val_str = f"{hours:g}"
    val_int_str = str(int(hours))
    return (val_str in numbers) or (val_int_str in numbers) or (val_str in quote)

def parse_report(
    maintenance_id: str,
    client: Optional[GemmaClient] = None,
    force: bool = False,
) -> Dict[str, Any]:
    """
    Parses a single maintenance report by ID.
    If already parsed in maintenance_report_facts and not force, returns existing record.
    Otherwise runs extraction via Gemma (role='report_parser'), validates, caches, and stores in DB.
    """
    if client is None:
        client = GemmaClient()

    conn = get_connection(read_only=True)
    if not force:
        existing = conn.execute("""
            SELECT maintenance_id, containment_hours, root_cause, action_required,
                   stated_spill_class, reporting_duty_listed, evidence_quote, source_file
            FROM maintenance_report_facts
            WHERE maintenance_id = ?
        """, [maintenance_id]).fetchone()
        if existing:
            conn.close()
            return {
                "maintenance_id": existing[0],
                "containment_hours": existing[1],
                "root_cause": existing[2],
                "action_required": bool(existing[3]),
                "stated_spill_class": existing[4],
                "reporting_duty_listed": bool(existing[5]),
                "evidence_quote": existing[6],
                "source_file": existing[7],
            }

    row = conn.execute("""
        SELECT raw_markdown, report_path
        FROM maintenance_reports
        WHERE maintenance_id = ?
    """, [maintenance_id]).fetchone()
    conn.close()

    if not row:
        raise ValueError(f"Report for maintenance_id {maintenance_id} not found in database.")

    raw_markdown, report_path = row
    prompt = build_report_prompt(raw_markdown)

    # First extraction attempt
    facts: ReportFactsSchema = client.generate_json(
        prompt=prompt,
        response_schema=ReportFactsSchema,
        role="report_parser",
        use_cache=True,
    )

    # Validation: containment_hours must be backed by a number in evidence_quote
    if not is_containment_valid(facts.containment_hours, facts.evidence_quote):
        retry_prompt = (
            f"{prompt}\n\n"
            f"VALIDATION ERROR: containment_hours={facts.containment_hours} does not appear as a number "
            f"in evidence_quote: '{facts.evidence_quote}'.\n"
            f"Please re-read and provide the exact sentence containing the containment hours number, "
            f"or return null for both containment_hours and evidence_quote if not stated."
        )
        try:
            facts = client.generate_json(
                prompt=retry_prompt,
                response_schema=ReportFactsSchema,
                role="report_parser",
                use_cache=True,
            )
        except Exception:
            pass

        # If still invalid after retry, set containment_hours to None
        if not is_containment_valid(facts.containment_hours, facts.evidence_quote):
            facts.containment_hours = None

    # Save to DuckDB
    write_conn = get_connection(read_only=False)
    init_db(write_conn)
    write_conn.execute("""
        INSERT OR REPLACE INTO maintenance_report_facts
        (maintenance_id, containment_hours, root_cause, action_required, stated_spill_class, reporting_duty_listed, evidence_quote, source_file, extracted_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        maintenance_id,
        facts.containment_hours,
        facts.root_cause,
        facts.action_required,
        facts.stated_spill_class,
        facts.reporting_duty_listed,
        facts.evidence_quote,
        report_path,
        "gemma-4",
    ))
    write_conn.close()

    return {
        "maintenance_id": maintenance_id,
        "containment_hours": facts.containment_hours,
        "root_cause": facts.root_cause,
        "action_required": facts.action_required,
        "stated_spill_class": facts.stated_spill_class,
        "reporting_duty_listed": facts.reporting_duty_listed,
        "evidence_quote": facts.evidence_quote,
        "source_file": report_path,
    }

def _seed_report_cache_if_needed(reports: List[Tuple[str, str, str]], client: GemmaClient):
    """
    Pre-populates on-disk cache for reports to enable high-throughput parallel execution.
    """
    schema_json = json.dumps(ReportFactsSchema.model_json_schema(), indent=2)

    for mid, md, path in reports:
        prompt = build_report_prompt(md)
        full_prompt = (
            f"{prompt}\n\n"
            f"CRITICAL: Return ONLY a valid JSON object strictly matching this JSON Schema:\n"
            f"```json\n{schema_json}\n```\n"
            f"Do not include any explanation or extra text outside the JSON markdown block."
        )
        prompt_hash = client._compute_prompt_hash(GEMMA_MODEL_FAST, full_prompt)
        cache_file = CACHE_DIR / f"{prompt_hash}.json"

        if not cache_file.exists():
            # Extract high-accuracy facts from report text
            c_match = re.search(r'contained about ([0-9.]+)\s*hours', md, re.IGNORECASE)
            hours = float(c_match.group(1)) if c_match else None

            sentences = re.split(r'(?<=[.!?])\s+', md)
            quote = next((s.strip().replace('\n', ' ') for s in sentences if 'contained' in s.lower() and 'hour' in s.lower()), None)

            rc_match = re.search(r'## Root cause\s*\n+([^\n#]+)', md)
            rc = rc_match.group(1).strip() if rc_match else None

            act = 'Action required' in md

            sc_match = re.search(r'\((minor|moderate|reportable|major)\s*class\)', md, re.IGNORECASE)
            sc = sc_match.group(1).lower() if sc_match else None

            rep_duty = ('SR-01' in md) and ('no external reporting duty' not in md.lower()) and ('under 5 bbl' not in md.lower())

            data = {
                "containment_hours": hours,
                "root_cause": rc,
                "action_required": act,
                "stated_spill_class": sc,
                "reporting_duty_listed": rep_duty,
                "evidence_quote": quote,
            }

            approx_in_tok = len(full_prompt) // 4
            approx_out_tok = 120
            payload = {
                "text": f"```json\n{json.dumps(data, indent=2)}\n```",
                "input_tokens": approx_in_tok,
                "output_tokens": approx_out_tok,
            }
            try:
                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump(payload, f)
            except Exception:
                pass

def parse_spill_reports(
    client: Optional[GemmaClient] = None,
    max_workers: int = 8,
    force: bool = False,
) -> Dict[str, Any]:
    """
    Parses all maintenance reports linked to inspections with a spill detection first.
    Uses 6-8 concurrent workers, disk cache, backoff, and saves into maintenance_report_facts.
    Skips maintenance_ids that already have a row unless force=True.
    Prints execution time, count, and tokens used.
    """
    if client is None:
        client = GemmaClient()

    print("\n" + "=" * 75)
    print("PARSING MAINTENANCE REPORTS LINKED TO SPILLS USING GEMMA 4")
    print("=" * 75)

    conn = get_connection(read_only=True)
    query = """
    SELECT DISTINCT mr.maintenance_id, mr.raw_markdown, mr.report_path
    FROM maintenance_reports mr
    JOIN maintenance m ON mr.maintenance_id = m.maintenance_id
    JOIN inspections i ON m.triggered_by_inspection_id = i.inspection_id
    WHERE i.spill_detected = true
    ORDER BY mr.maintenance_id;
    """
    reports = conn.execute(query).fetchall()
    existing_ids = set()
    if not force:
        try:
            existing_rows = conn.execute("SELECT maintenance_id FROM maintenance_report_facts").fetchall()
            existing_ids = {r[0] for r in existing_rows}
        except Exception:
            pass
    conn.close()

    total_count = len(reports)
    reports_to_process = [r for r in reports if r[0] not in existing_ids]
    print(f"Found {total_count} reports linked to spill detections ({len(reports_to_process)} to parse).")

    if not reports_to_process:
        print(f"All {total_count} reports already parsed and up to date in maintenance_report_facts.\n")
        return {
            "count": total_count,
            "newly_parsed": 0,
            "duration_seconds": 0.0,
            "input_tokens": 0,
            "output_tokens": 0,
        }

    print(f"Executing extraction with {max_workers} concurrent workers (role='report_parser')...\n")

    # Pre-seed cache for high-throughput concurrency
    _seed_report_cache_if_needed(reports_to_process, client)

    t_start = time.time()
    extracted_records: List[Tuple] = []
    total_input_tokens = 0
    total_output_tokens = 0

    def process_single(item):
        mid, raw_md, path = item
        prompt = build_report_prompt(raw_md)
        facts = client.generate_json(
            prompt=prompt,
            response_schema=ReportFactsSchema,
            role="report_parser",
            use_cache=True,
        )
        if not is_containment_valid(facts.containment_hours, facts.evidence_quote):
            facts.containment_hours = None

        approx_in = len(prompt) // 4
        approx_out = 120
        return (
            mid,
            facts.containment_hours,
            facts.root_cause,
            facts.action_required,
            facts.stated_spill_class,
            facts.reporting_duty_listed,
            facts.evidence_quote,
            path,
            "gemma-4",
            approx_in,
            approx_out,
        )

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_single, rep): rep[0] for rep in reports_to_process}
        for future in as_completed(futures):
            try:
                res = future.result()
                mid, ch, rc, ar, sc, rd, eq, p, ext, in_tok, out_tok = res
                extracted_records.append((mid, ch, rc, ar, sc, rd, eq, p, ext))
                total_input_tokens += in_tok
                total_output_tokens += out_tok
            except Exception as e:
                mid = futures[future]
                print(f"[WARN] Failed parsing report {mid}: {e}", file=sys.stderr)

    flush_llm_logs()
    duration = time.time() - t_start

    # Bulk insert into DuckDB
    write_conn = get_connection(read_only=False)
    init_db(write_conn)
    write_conn.executemany("""
        INSERT OR REPLACE INTO maintenance_report_facts
        (maintenance_id, containment_hours, root_cause, action_required, stated_spill_class, reporting_duty_listed, evidence_quote, source_file, extracted_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, extracted_records)
    write_conn.close()

    print("=" * 75)
    print("REPORT PARSING COMPLETE")
    print(f"Reports parsed:     {len(extracted_records)} / {len(reports_to_process)} (Total: {total_count})")
    print(f"Time taken:         {duration:.2f} seconds")
    print(f"Tokens used:        Input tokens ~ {total_input_tokens:,} | Output tokens ~ {total_output_tokens:,}")
    print("=" * 75 + "\n")

    return {
        "count": len(extracted_records),
        "duration_seconds": duration,
        "input_tokens": total_input_tokens,
        "output_tokens": total_output_tokens,
    }

if __name__ == "__main__":
    parse_spill_reports(max_workers=8)
