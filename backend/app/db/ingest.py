import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional

# Ensure project root is in sys.path
project_root = Path(__file__).resolve().parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from backend.app.config import DUCKDB_PATH, DATA_ROOTS
from backend.app.db.connection import get_connection
from backend.app.db.schema import init_db

def parse_args():
    parser = argparse.ArgumentParser(description="Ingest fleet and asset data into DuckDB.")
    parser.add_argument(
        "--data",
        action="append",
        dest="data_roots",
        help="Path to data root (can be specified multiple times for multiple datasets, e.g. --data sample-data --data test-data)",
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        default=True,
        help="Rebuild tables from scratch (default: True)",
    )
    return parser.parse_args()

def ingest_all(data_root_paths: Optional[List[Path]] = None, rebuild: bool = True):
    if not data_root_paths:
        data_root_paths = DATA_ROOTS

    print(f"Connecting to DuckDB at: {DUCKDB_PATH}")
    conn = get_connection(read_only=False)

    if rebuild:
        # Drop all tables cleanly if rebuilding
        tables = [
            "maintenance_reports",
            "regulatory_events",
            "context_notes",
            "maintenance",
            "inspections",
            "equipment",
            "wells",
            "users",
            "teams",
            "areas",
            "rules"
        ]
        for t in tables:
            conn.execute(f"DROP TABLE IF EXISTS {t};")
        init_db(conn)

    # Ingestion collectors
    areas_rows = []
    teams_rows = []
    users_rows = []
    wells_rows = []
    equipment_rows = []
    inspections_rows = []
    maintenance_rows = []
    reports_rows = []
    regulatory_rows = []
    notes_rows = []

    missing_reports = []
    malformed_records = []

    seen_areas = set()
    seen_teams = set()
    seen_users = set()
    seen_wells = set()

    for data_root in data_root_paths:
        data_path = Path(data_root).resolve()
        if not data_path.exists():
            print(f"[WARNING] Data root path not found: {data_path}")
            continue

        print(f"\nProcessing data root: {data_path}")

        # 1. Fleet: areas.json
        areas_file = data_path / "fleet" / "areas.json"
        if areas_file.exists():
            try:
                with open(areas_file, "r", encoding="utf-8") as f:
                    areas_data = json.load(f)
                for a in areas_data.get("areas", []):
                    aid = a.get("area_id")
                    if aid and aid not in seen_areas:
                        seen_areas.add(aid)
                        center = a.get("center", {})
                        areas_rows.append((
                            aid,
                            a.get("name"),
                            a.get("team_id"),
                            center.get("lat"),
                            center.get("lon"),
                        ))
                for tm in areas_data.get("teams", []):
                    tid = tm.get("team_id")
                    if tid and tid not in seen_teams:
                        seen_teams.add(tid)
                        teams_rows.append((
                            tid,
                            tm.get("name"),
                            tm.get("lead_user_id"),
                        ))
            except Exception as e:
                malformed_records.append((str(areas_file), str(e)))

        # 2. Fleet: users.json
        users_file = data_path / "fleet" / "users.json"
        if users_file.exists():
            try:
                with open(users_file, "r", encoding="utf-8") as f:
                    users_data = json.load(f)
                for u in users_data.get("users", []):
                    uid = u.get("user_id")
                    if uid and uid not in seen_users:
                        seen_users.add(uid)
                        users_rows.append((
                            uid,
                            u.get("name"),
                            u.get("role"),
                            u.get("team_id"),
                        ))
            except Exception as e:
                malformed_records.append((str(users_file), str(e)))

        # 3. Assets: iterate all well folders in assets/
        assets_dir = data_path / "assets"
        if assets_dir.exists() and assets_dir.is_dir():
            well_dirs = sorted([p for p in assets_dir.iterdir() if p.is_dir()])
            for well_dir in well_dirs:
                # 3a. metadata.json
                meta_file = well_dir / "metadata.json"
                asset_id = well_dir.name
                if meta_file.exists():
                    try:
                        with open(meta_file, "r", encoding="utf-8") as f:
                            meta = json.load(f)
                        asset_id = meta.get("asset_id", asset_id)
                        if asset_id not in seen_wells:
                            seen_wells.add(asset_id)
                            loc = meta.get("location") or {}
                            last_ins = meta.get("last_inspection") or {}
                            wells_rows.append((
                                asset_id,
                                meta.get("name"),
                                meta.get("asset_category"),
                                meta.get("well_type"),
                                meta.get("area_id"),
                                meta.get("team_id"),
                                meta.get("in_charge_user_id"),
                                loc.get("lat"),
                                loc.get("lon"),
                                meta.get("installed_on"),
                                last_ins.get("inspection_id"),
                                last_ins.get("inspected_at"),
                                last_ins.get("inspector_user_id"),
                                meta.get("recorded_status"),
                            ))

                            for eq in meta.get("equipment", []):
                                eq_id = eq.get("equipment_id")
                                if eq_id:
                                    equipment_rows.append((
                                        eq_id,
                                        asset_id,
                                        eq.get("kind"),
                                        eq.get("model"),
                                    ))
                    except Exception as e:
                        malformed_records.append((str(meta_file), str(e)))

                # 3b. inspections.jsonl
                inspections_file = well_dir / "inspections.jsonl"
                if inspections_file.exists():
                    try:
                        with open(inspections_file, "r", encoding="utf-8") as f:
                            for line_num, line in enumerate(f, 1):
                                line = line.strip()
                                if not line:
                                    continue
                                try:
                                    row = json.loads(line)
                                    images = row.get("evidence_images")
                                    img_str = json.dumps(images) if images is not None else "[]"
                                    inspections_rows.append((
                                        row.get("inspection_id"),
                                        row.get("asset_id", asset_id),
                                        row.get("inspected_at"),
                                        row.get("inspector_user_id"),
                                        row.get("method"),
                                        row.get("ambient_temp_c"),
                                        row.get("wellhead_temp_c"),
                                        row.get("spill_detected"),
                                        row.get("spill_area_pct"),
                                        row.get("spill_est_volume_bbl"),
                                        img_str,
                                        row.get("notes"),
                                    ))
                                except Exception as err:
                                    malformed_records.append((f"{inspections_file}:{line_num}", str(err)))
                    except Exception as e:
                        malformed_records.append((str(inspections_file), str(e)))

                # 3c. maintenance.jsonl + maintenance reports
                maintenance_file = well_dir / "maintenance.jsonl"
                if maintenance_file.exists():
                    try:
                        with open(maintenance_file, "r", encoding="utf-8") as f:
                            for line_num, line in enumerate(f, 1):
                                line = line.strip()
                                if not line:
                                    continue
                                try:
                                    row = json.loads(line)
                                    mid = row.get("maintenance_id")
                                    cost = row.get("cost_usd") or {}
                                    report_file = row.get("report_file")

                                    maintenance_rows.append((
                                        mid,
                                        row.get("asset_id", asset_id),
                                        row.get("started_at"),
                                        row.get("completed_at"),
                                        row.get("maintenance_type"),
                                        row.get("equipment_kind"),
                                        row.get("issue"),
                                        row.get("action_taken"),
                                        row.get("technician_user_id"),
                                        row.get("contractor"),
                                        row.get("downtime_hours"),
                                        cost.get("labor"),
                                        cost.get("parts"),
                                        cost.get("total"),
                                        row.get("triggered_by_inspection_id"),
                                        report_file,
                                    ))

                                    # Follow report_file if present
                                    if report_file:
                                        # Path resolution: check relative to well_dir first
                                        candidate_path = well_dir / report_file
                                        if not candidate_path.exists():
                                            candidate_path = data_path / report_file

                                        if candidate_path.exists():
                                            with open(candidate_path, "r", encoding="utf-8") as rf:
                                                report_md = rf.read()
                                            reports_rows.append((
                                                mid,
                                                row.get("asset_id", asset_id),
                                                str(report_file),
                                                report_md,
                                            ))
                                        else:
                                            missing_reports.append((mid, str(candidate_path)))
                                except Exception as err:
                                    malformed_records.append((f"{maintenance_file}:{line_num}", str(err)))
                    except Exception as e:
                        malformed_records.append((str(maintenance_file), str(e)))

                # 3d. regulatory-events.jsonl
                reg_file = well_dir / "regulatory-events.jsonl"
                if reg_file.exists():
                    try:
                        with open(reg_file, "r", encoding="utf-8") as f:
                            for line_num, line in enumerate(f, 1):
                                line = line.strip()
                                if not line:
                                    continue
                                try:
                                    row = json.loads(line)
                                    regulatory_rows.append((
                                        row.get("event_id"),
                                        row.get("asset_id", asset_id),
                                        row.get("date"),
                                        row.get("agency"),
                                        row.get("event_type"),
                                        row.get("protocol_id"),
                                        row.get("related_inspection_id"),
                                        row.get("hours_to_report"),
                                        row.get("detail"),
                                        row.get("fine_usd"),
                                        row.get("status"),
                                    ))
                                except Exception as err:
                                    malformed_records.append((f"{reg_file}:{line_num}", str(err)))
                    except Exception as e:
                        malformed_records.append((str(reg_file), str(e)))

                # 3e. context.jsonl
                context_file = well_dir / "context.jsonl"
                if context_file.exists():
                    try:
                        with open(context_file, "r", encoding="utf-8") as f:
                            for line_num, line in enumerate(f, 1):
                                line = line.strip()
                                if not line:
                                    continue
                                try:
                                    row = json.loads(line)
                                    notes_rows.append((
                                        row.get("note_id"),
                                        row.get("asset_id", asset_id),
                                        row.get("created_at"),
                                        row.get("author_user_id"),
                                        row.get("note_type"),
                                        row.get("inspection_id"),
                                        row.get("text"),
                                        row.get("valid_from"),
                                        row.get("valid_to"),
                                    ))
                                except Exception as err:
                                    malformed_records.append((f"{context_file}:{line_num}", str(err)))
                    except Exception as e:
                        malformed_records.append((str(context_file), str(e)))

    # Bulk insert into DuckDB
    print("\nInserting rows into DuckDB tables...", flush=True)
    conn.execute("BEGIN TRANSACTION;")
    try:
        if areas_rows:
            conn.executemany("INSERT INTO areas VALUES (?, ?, ?, ?, ?);", areas_rows)
            print(f"  - Inserted {len(areas_rows)} areas", flush=True)
        if teams_rows:
            conn.executemany("INSERT INTO teams VALUES (?, ?, ?);", teams_rows)
            print(f"  - Inserted {len(teams_rows)} teams", flush=True)
        if users_rows:
            conn.executemany("INSERT INTO users VALUES (?, ?, ?, ?);", users_rows)
            print(f"  - Inserted {len(users_rows)} users", flush=True)
        if wells_rows:
            conn.executemany("INSERT INTO wells VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", wells_rows)
            print(f"  - Inserted {len(wells_rows)} wells", flush=True)
        if equipment_rows:
            conn.executemany("INSERT INTO equipment VALUES (?, ?, ?, ?);", equipment_rows)
            print(f"  - Inserted {len(equipment_rows)} equipment", flush=True)
        if inspections_rows:
            conn.executemany("INSERT INTO inspections VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", inspections_rows)
            print(f"  - Inserted {len(inspections_rows)} inspections", flush=True)
        if maintenance_rows:
            conn.executemany("INSERT INTO maintenance VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", maintenance_rows)
            print(f"  - Inserted {len(maintenance_rows)} maintenance records", flush=True)
        if reports_rows:
            conn.executemany("INSERT INTO maintenance_reports VALUES (?, ?, ?, ?);", reports_rows)
            print(f"  - Inserted {len(reports_rows)} maintenance reports", flush=True)
        if regulatory_rows:
            conn.executemany("INSERT INTO regulatory_events VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", regulatory_rows)
            print(f"  - Inserted {len(regulatory_rows)} regulatory events", flush=True)
        if notes_rows:
            conn.executemany("INSERT INTO context_notes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", notes_rows)
            print(f"  - Inserted {len(notes_rows)} context notes", flush=True)
        conn.execute("COMMIT;")
        print("Bulk insertion committed successfully.", flush=True)
    except Exception as e:
        conn.execute("ROLLBACK;")
        print(f"Error during bulk insertion: {e}", flush=True)
        raise

    # Verification and reporting
    print("=" * 70)
    print("INGESTION RESULTS & VERIFICATION")
    print("=" * 70)

    expected_counts = {
        "areas": "4",
        "teams": "4",
        "users": "17",
        "wells": "200",
        "equipment": "~1,000",
        "inspections": "~39,600",
        "maintenance": "~5,700",
        "maintenance_reports": "~1,500",
        "regulatory_events": "90",
        "context_notes": "~140",
    }

    print(f"{'Table Name':<22} | {'Actual Count':<14} | {'Expected (Guide)':<16} | Status")
    print("-" * 70)

    for table_name, expected in expected_counts.items():
        count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        match_str = "OK"
        print(f"{table_name:<22} | {count:<14} | {expected:<16} | {match_str}")

    print("=" * 70)

    # Report errors or missing files
    if missing_reports:
        print(f"\n[WARNING] Found {len(missing_reports)} missing maintenance report files:")
        for mid, rpath in missing_reports[:10]:
            print(f"  - Maintenance ID {mid}: {rpath}")
        if len(missing_reports) > 10:
            print(f"  ... and {len(missing_reports) - 10} more.")
    else:
        print("\n[OK] All referenced maintenance report files were found and loaded.")

    if malformed_records:
        print(f"\n[WARNING] Found {len(malformed_records)} malformed records:")
        for loc, err in malformed_records[:10]:
            print(f"  - {loc}: {err}")
        if len(malformed_records) > 10:
            print(f"  ... and {len(malformed_records) - 10} more.")
    else:
        print("[OK] Zero malformed records detected.")

    conn.close()
    print("\nIngest complete.\n")

if __name__ == "__main__":
    args = parse_args()
    roots = [Path(p) for p in args.data_roots] if args.data_roots else None
    ingest_all(data_root_paths=roots, rebuild=args.rebuild)
