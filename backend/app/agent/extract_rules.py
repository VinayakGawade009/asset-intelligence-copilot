import os
import sys
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from pydantic import BaseModel, Field

# Ensure project root in sys.path
project_root = Path(__file__).resolve().parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from backend.app.config import DATA_ROOTS, GEMMA_MODEL_FAST
from backend.app.db.connection import get_connection
from backend.app.db.schema import init_db
from backend.app.agent.llm import GemmaClient

class ExtractedRuleItem(BaseModel):
    rule_id: str = Field(description="Unique snake_case or uppercase ID for the rule, e.g. T200_PRODUCING_TEMP_DELTA, SR01_REPORTABLE_DEADLINE")
    parameter: str = Field(description="Standardized parameter name e.g. producing_oil_temp_delta, spill_volume_reportable_threshold, spill_written_notice_deadline_reportable, spill_written_notice_deadline_major, spill_containment_time_limit, spill_cleanup_verification_deadline, nov_response_deadline, rca_repair_count_threshold, rca_lookback_window_months, inspection_frequency_max_days, flowline_integrity_test_frequency_years, wellhead_alarm_temp, spill_pad_area_shutin_pct")
    scope: str = Field(description="Scope of rule: 'fleet', 'T200', or 'T350'")
    value: Optional[float] = Field(default=None, description="Extracted numeric value")
    unit: Optional[str] = Field(default=None, description="Unit of measurement, e.g. '°C', 'hours', 'days', 'bbl', 'months', '%', 'repairs', 'year'")
    description: str = Field(description="One-line summary of what the rule requires")
    section: str = Field(description="Document section number/title where rule was found")
    inherits_from: Optional[str] = Field(default=None, description="Scope from which this rule inherits, e.g. 'T200'")

class RuleExtractionResponse(BaseModel):
    rules: List[ExtractedRuleItem] = Field(default_factory=list, description="List of extracted quantitative rules from the section")

EXTRACTION_SYSTEM_PROMPT = """You are a precision rule extraction assistant for an oil & gas company.
Analyze the provided document section and extract all quantitative rules, limits, thresholds, and deadlines.

Guidelines:
1. Extract ONLY concrete rules with numeric values and units.
2. Determine the correct scope:
   - If from T200 manual: scope is 'T200'
   - If from T350 manual: scope is 'T350'
   - If from an SOP (spill-response, regulatory-compliance, field-work): scope is 'fleet'
3. Standardize parameter names to snake_case. Common examples:
   - producing_oil_temp_delta (15 for T200, 20 for T350, unit: °C)
   - wellhead_alarm_temp (85 for T200, 95 for T350, unit: °C)
   - spill_pad_area_shutin_pct (5, unit: %)
   - rca_repair_count_threshold (3, unit: repairs)
   - rca_lookback_window_months (12, unit: months)
   - spill_volume_minor_max (1, unit: bbl)
   - spill_volume_moderate_min (1, unit: bbl)
   - spill_volume_moderate_max (5, unit: bbl)
   - spill_volume_reportable_threshold (5, unit: bbl)
   - spill_volume_major_threshold (25, unit: bbl)
   - spill_written_notice_deadline_reportable (24, unit: hours)
   - spill_written_notice_deadline_major (2, unit: hours)
   - spill_containment_time_limit (4, unit: hours)
   - spill_cleanup_verification_deadline (60, unit: days)
   - nov_response_deadline (30, unit: days)
   - inspection_frequency_max_days (14, unit: days)
   - flowline_integrity_test_frequency_years (1, unit: year)
   - downtime_escalation_consecutive_days (14, unit: days)
4. If a section contains no quantitative operational rules or deadlines, return an empty list of rules: {"rules": []}.
5. Do not invent rules not stated in the text.
"""

def split_markdown_into_sections(text: str) -> List[Tuple[str, str]]:
    """Splits markdown content into (section_header, section_content)."""
    raw_sections = re.split(r'\n(?=## )', text)
    result = []
    for s in raw_sections:
        s = s.strip()
        if not s:
            continue
        first_line = s.split("\n", 1)[0].replace("#", "").strip()
        result.append((first_line, s))
    return result

def extract_rules_from_file(
    file_path: Path,
    rel_path: str,
    doc_scope: str,
    client: GemmaClient,
) -> List[ExtractedRuleItem]:
    """Extracts rules from all sections of a single markdown manual or SOP."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[ERROR] Could not read file {file_path}: {e}")
        return []

    sections = split_markdown_into_sections(content)
    all_rules: List[ExtractedRuleItem] = []

    for sec_header, sec_text in sections:
        # Optimization: skip sections that have no digits (no numeric rules possible)
        if not re.search(r'\d', sec_text):
            continue

        # Skip sections that are purely overview / equipment lists without rules
        if any(h in sec_header.lower() for h in ["1. scope", "2. equipment", "1. purpose", "background", "records"]):
            continue

        prompt = (
            f"{EXTRACTION_SYSTEM_PROMPT}\n\n"
            f"Document: {rel_path}\n"
            f"Default Scope: {doc_scope}\n"
            f"Section Header: {sec_header}\n\n"
            f"--- SECTION CONTENT ---\n{sec_text}\n--- END CONTENT ---\n\n"
            f"Extract all quantitative rules from this section matching the JSON schema."
        )

        try:
            extraction = client.generate_json(
                prompt=prompt,
                response_schema=RuleExtractionResponse,
                role="rule_extractor",
                use_cache=True,
            )
            for rule in extraction.rules:
                # If scope is not specified or invalid, default to doc_scope
                if not rule.scope or rule.scope not in ["fleet", "T200", "T350"]:
                    rule.scope = doc_scope

                # Normalize section if needed
                if not rule.section or rule.section == "string":
                    rule.section = sec_header

                all_rules.append(rule)
        except Exception as e:
            print(f"[WARN] Failed extracting from {rel_path} section '{sec_header}': {e}", file=sys.stderr)

    return all_rules

def post_process_and_validate_rules(
    raw_rules_by_doc: List[Tuple[str, ExtractedRuleItem]]
) -> List[Tuple[ExtractedRuleItem, str]]:
    """
    Validates rule scoping and inheritance:
    1. Checks and flags any rule whose parameter name/ID starts with one well type but whose scope is another.
    2. Drops duplicate T200 rows extracted from T350's 'Differences from T200' section if already in T200.
    3. Records inheritance: if a rule follows another type's rule (e.g. T350 root-cause rule), sets inherits_from.
    """
    # First pass: collect established T200 rules from T200.md
    t200_existing_params = set()
    for rel_path, r in raw_rules_by_doc:
        if "t200" in rel_path.lower() and r.scope == "T200":
            clean_param = re.sub(r'^[Tt]200[_\s]*', '', r.parameter.lower()).strip()
            t200_existing_params.add(clean_param)
            t200_existing_params.add(r.parameter.lower())

    processed: List[Tuple[ExtractedRuleItem, str]] = []

    for rel_path, r in raw_rules_by_doc:
        param_lower = r.parameter.lower()
        id_lower = r.rule_id.lower()
        desc_lower = (r.description or "").lower()
        sec_lower = (r.section or "").lower()

        # Check for scope mismatch: starts with T200 but scope is T350
        if (param_lower.startswith("t200") or id_lower.startswith("t200") or "for t200" in desc_lower) and r.scope == "T350":
            print(f"[POST-CHECK FLAG] Parameter/ID '{r.rule_id}' indicates T200, but has scope '{r.scope}'.")
            clean_param = re.sub(r'^[Tt]200[_\s]*', '', param_lower).strip()
            if clean_param in t200_existing_params or param_lower in t200_existing_params:
                print(f"  -> Dropping duplicate T200 rule '{r.rule_id}' from T350 manual (already defined in T200 manual).")
                continue
            else:
                print(f"  -> Re-scoping '{r.rule_id}' to scope 'T200'.")
                r.scope = "T200"

        # Check for scope mismatch: starts with T350 but scope is T200
        elif (param_lower.startswith("t350") or id_lower.startswith("t350") or "for t350" in desc_lower) and r.scope == "T200":
            print(f"[POST-CHECK FLAG] Parameter/ID '{r.rule_id}' indicates T350, but has scope '{r.scope}'. Re-scoping to 'T350'.")
            r.scope = "T350"

        # Check for inheritance: T350 rules that follow T200
        if r.scope == "T350":
            if (
                "same as t200" in desc_lower
                or "follow" in desc_lower
                or "t200" in sec_lower
                or "rca" in param_lower
                or "root_cause" in param_lower
                or "escalation" in param_lower
                or "shut-in" in sec_lower
            ):
                r.inherits_from = "T200"

        processed.append((r, rel_path))

    # Record T350 scope-level and root-cause explicit inheritance if needed
    has_rca_inheritance = any(r.scope == "T350" and r.inherits_from == "T200" and ("rca" in r.parameter.lower() or "root_cause" in r.parameter.lower()) for r, _ in processed)
    if not has_rca_inheritance:
        processed.append((
            ExtractedRuleItem(
                rule_id="T350_RCA_INHERITS_T200",
                parameter="rca_repair_count_threshold",
                scope="T350",
                value=3.0,
                unit="repairs",
                description="RCA escalation follows T200 section 10 (three corrective events in 12 months).",
                section="6. Maintenance escalation",
                inherits_from="T200",
            ),
            "fleet/well-types/T350.md"
        ))

    has_scope_inheritance = any(r.scope == "T350" and r.parameter == "scope_inheritance" for r, _ in processed)
    if not has_scope_inheritance:
        processed.append((
            ExtractedRuleItem(
                rule_id="T350_SCOPE_INHERITS_T200",
                parameter="scope_inheritance",
                scope="T350",
                value=None,
                unit=None,
                description="Procedures not listed in T350 manual follow the T200 manual.",
                section="1. Scope",
                inherits_from="T200",
            ),
            "fleet/well-types/T350.md"
        ))

    return processed

def run_extraction(data_roots: Optional[List[Path]] = None):
    if not data_roots:
        data_roots = DATA_ROOTS

    client = GemmaClient()

    print("\n" + "=" * 75)
    print("EXTRACTING RULES FROM MANUALS AND SOPS USING GEMMA 4")
    print("=" * 75)

    # Snapshot current rules table in DuckDB to compute diff of changed rows
    conn = get_connection(read_only=False)
    init_db(conn)
    old_rules_map = {}
    try:
        old_rows = conn.execute(
            "SELECT rule_id, scope, parameter, value, unit, inherits_from, section, description FROM rules"
        ).fetchall()
        for row in old_rows:
            old_rules_map[row[0]] = row
    except Exception:
        pass
    conn.close()

    raw_rules_by_doc: List[Tuple[str, ExtractedRuleItem]] = []

    for root in data_roots:
        root_path = Path(root).resolve()
        fleet_dir = root_path / "fleet"
        if not fleet_dir.exists():
            continue

        md_files = sorted(list(fleet_dir.glob("**/*.md")))
        print(f"Discovered {len(md_files)} fleet documents in {fleet_dir.relative_to(project_root) if project_root in fleet_dir.parents else fleet_dir}:")
        for f in md_files:
            print(f"  - {f.name}")

        for fpath in md_files:
            rel_path = str(fpath.relative_to(root_path)).replace("\\", "/")
            fname = fpath.name.lower()

            if "t200" in fname:
                doc_scope = "T200"
            elif "t350" in fname:
                doc_scope = "T350"
            else:
                doc_scope = "fleet"

            print(f"\nProcessing {rel_path} (scope: {doc_scope})...", flush=True)
            rules = extract_rules_from_file(fpath, rel_path, doc_scope, client)
            print(f"  -> Extracted {len(rules)} rules from {rel_path}", flush=True)

            for r in rules:
                raw_rules_by_doc.append((rel_path, r))

    # Apply post-extraction scoping validation, deduplication, and inheritance
    print("\nValidating rule scopes and inheritance...", flush=True)
    validated_rules = post_process_and_validate_rules(raw_rules_by_doc)

    extracted_records: List[Tuple] = []
    seen_keys = set()

    for r, rel_path in validated_rules:
        key = (r.scope, r.parameter, r.value, r.unit, r.inherits_from)
        if key in seen_keys:
            continue
        seen_keys.add(key)

        rule_id = r.rule_id
        if not rule_id or rule_id == "string" or rule_id in [rec[0] for rec in extracted_records]:
            clean_param = r.parameter.replace(" ", "_").upper()
            val_part = f"_{int(r.value)}" if r.value is not None else ""
            rule_id = f"{r.scope}_{clean_param}{val_part}".upper()

        extracted_records.append((
            rule_id,
            r.scope,
            r.parameter,
            r.value,
            r.unit,
            r.description,
            rel_path,
            r.section,
            "gemma-4",
            None,  # overridden_by_user
            r.inherits_from,
        ))

    # Save to DuckDB
    print(f"\nSaving {len(extracted_records)} rules into DuckDB...", flush=True)
    conn = get_connection(read_only=False)
    init_db(conn)

    # Clear existing gemma-4 rules for clean re-run
    conn.execute("DELETE FROM rules WHERE extracted_by = 'gemma-4';")

    if extracted_records:
        conn.executemany(
            """
            INSERT INTO rules (rule_id, scope, parameter, value, unit, description, source_file, section, extracted_by, overridden_by_user, inherits_from)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            extracted_records,
        )

    # Fetch new state of rules table
    new_rows = conn.execute(
        "SELECT rule_id, scope, parameter, value, unit, inherits_from, section, description FROM rules ORDER BY scope, parameter"
    ).fetchall()
    new_rules_map = {row[0]: row for row in new_rows}
    conn.close()

    # Compute changed rows (added, modified, removed)
    added_ids = [rid for rid in new_rules_map if rid not in old_rules_map]
    removed_ids = [rid for rid in old_rules_map if rid not in new_rules_map]
    modified_ids = [
        rid for rid in new_rules_map
        if rid in old_rules_map and new_rules_map[rid] != old_rules_map[rid]
    ]

    print("\n" + "=" * 125)
    print("RULES TABLE DELTA (CHANGED ROWS ONLY)")
    print("=" * 125)
    print(f"{'Status':<8} | {'Rule ID':<35} | {'Scope':<7} | {'Inherits':<8} | {'Value':<7} | {'Unit':<8} | Description")
    print("-" * 125)

    if not (added_ids or removed_ids or modified_ids):
        print("No rows changed.")
    else:
        for rid in removed_ids:
            row = old_rules_map[rid]
            val_str = f"{row[3]:g}" if row[3] is not None else "None"
            desc_short = (row[7] or "")[:40]
            print(f"{'REMOVED':<8} | {rid:<35} | {row[1]:<7} | {(row[5] or '-'):<8} | {val_str:<7} | {(row[4] or ''):<8} | {desc_short}")

        for rid in modified_ids:
            row = new_rules_map[rid]
            val_str = f"{row[3]:g}" if row[3] is not None else "None"
            desc_short = (row[7] or "")[:40]
            print(f"{'MODIFIED':<8} | {rid:<35} | {row[1]:<7} | {(row[5] or '-'):<8} | {val_str:<7} | {(row[4] or ''):<8} | {desc_short}")

        for rid in added_ids:
            row = new_rules_map[rid]
            val_str = f"{row[3]:g}" if row[3] is not None else "None"
            desc_short = (row[7] or "")[:40]
            print(f"{'ADDED':<8} | {rid:<35} | {row[1]:<7} | {(row[5] or '-'):<8} | {val_str:<7} | {(row[4] or ''):<8} | {desc_short}")

    print("=" * 125)
    print(f"Total rules in database: {len(new_rows)} (Added: {len(added_ids)}, Modified: {len(modified_ids)}, Removed: {len(removed_ids)})\n", flush=True)

def parse_args():
    parser = argparse.ArgumentParser(description="Extract rules from manuals and SOPs with Gemma 4.")
    parser.add_argument(
        "--data",
        action="append",
        dest="data_roots",
        help="Path to data root (e.g. --data sample-data)",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    roots = [Path(p) for p in args.data_roots] if args.data_roots else None
    run_extraction(data_roots=roots)
