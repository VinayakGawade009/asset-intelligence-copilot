"""Unit and integration tests for derived analytics layer against evaluation queries Q1, Q2, Q4, Q5, Q6."""
import sys
from pathlib import Path
from datetime import date
import pytest

# Ensure project root in sys.path
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from backend.app.db.connection import get_connection
from backend.app.derived.views import (
    create_derived_views,
    calculate_downtime_days,
    rank_downtime_wells_in_area,
)
from backend.app.derived.windows import get_date_window

@pytest.fixture(scope="module")
def db():
    conn = get_connection(read_only=False)
    create_derived_views(conn)
    yield conn
    conn.close()

def test_q1_well_0001_status(db):
    """
    Q1: Is WELL-0001 producing oil right now?
    Expected: Not producing oil. Latest inspection INS-0001-0203 on 15 Oct 2026, by Ryan Brooks (U-104), drone.
    Delta is 3.2 °C (below T200 limit of 15 °C).
    """
    row = db.execute("""
        SELECT
            inspection_id,
            inspected_date,
            inspector_name,
            method,
            temp_delta_c,
            temp_delta_threshold,
            is_producing_oil
        FROM v_inspections_producing
        WHERE asset_id = 'WELL-0001'
        ORDER BY inspected_at DESC
        LIMIT 1
    """).fetchone()

    assert row is not None, "No inspection found for WELL-0001"
    insp_id, insp_date, insp_name, method, delta, threshold, is_prod = row

    assert insp_id == "INS-0001-0203"
    assert insp_date == date(2026, 10, 15)
    assert insp_name == "Ryan Brooks"
    assert method == "drone"
    assert round(delta, 1) == 3.2
    assert threshold == 15.0
    assert is_prod is False, "WELL-0001 should be non-producing based on temperature delta"

def test_q2_northeast_block_8_non_producing_wells(db):
    """
    Q2: Which wells in Northeast Block 8 are not producing oil right now?
    Expected: Exactly four T200 wells, all inspected on 15 Oct 2026:
    WELL-0164 (4.1 °C), WELL-0170 (2.9 °C), WELL-0172 (5.7 °C), WELL-0175 (0.4 °C).
    """
    rows = db.execute("""
        WITH latest_inspections AS (
            SELECT *,
                ROW_NUMBER() OVER (PARTITION BY asset_id ORDER BY inspected_at DESC) as rn
            FROM v_inspections_producing
            WHERE area_name = 'Northeast Block 8'
        )
        SELECT
            asset_id,
            well_type,
            inspected_date,
            ROUND(temp_delta_c, 1) as delta,
            is_producing_oil
        FROM latest_inspections
        WHERE rn = 1 AND is_producing_oil = false
        ORDER BY asset_id
    """).fetchall()

    non_producing_well_ids = [r[0] for r in rows]
    assert non_producing_well_ids == ["WELL-0164", "WELL-0170", "WELL-0172", "WELL-0175"], (
        f"Expected exactly 4 non-producing wells in Block 8, got: {non_producing_well_ids}"
    )

    deltas = {r[0]: r[3] for r in rows}
    assert deltas["WELL-0164"] == 4.1
    assert deltas["WELL-0170"] == 2.9
    assert deltas["WELL-0172"] == 5.7
    assert deltas["WELL-0175"] == 0.4

    for r in rows:
        assert r[1] == "T200"
        assert r[2] == date(2026, 10, 15)

def test_q4_well_0001_spills_after_rainwater_correction(db):
    """
    Q4: How many oil spills has WELL-0001 had in the last 4 years, and how much oil in total?
    Expected: 6 spills, 15.1 barrels total.
    7 raw detections, but INS-0001-0070 (0.9 bbl on 7 Mar 2024) was corrected as rainwater (CTX-0001-001).
    """
    start_date, end_date = get_date_window("last 4 years")

    rows = db.execute("""
        SELECT
            inspection_id,
            inspected_date,
            raw_spill_detected,
            effective_spill_detected,
            raw_volume_bbl,
            effective_volume_bbl,
            correction_note_id
        FROM v_effective_spills
        WHERE asset_id = 'WELL-0001'
          AND inspected_date >= ?
          AND inspected_date <= ?
          AND raw_spill_detected = true
        ORDER BY inspected_date
    """, [start_date, end_date]).fetchall()

    # Total raw detections in 4 years = 7
    assert len(rows) == 7, f"Expected 7 raw spill detections for WELL-0001, got {len(rows)}"

    # Effective spills (excluding corrected false positives) = 6
    effective_spills = [r for r in rows if r[3] is True]
    assert len(effective_spills) == 6, f"Expected 6 effective spills, got {len(effective_spills)}"

    # Check rainwater correction on INS-0001-0070
    corrected = [r for r in rows if r[0] == "INS-0001-0070"][0]
    assert corrected[2] is True, "Raw detection should be true"
    assert corrected[3] is False, "Effective detection should be false after correction"
    assert corrected[6] == "CTX-0001-001", "Should cite correction note CTX-0001-001"
    assert corrected[5] == 0.0, "Effective volume of false positive should be 0.0"

    # Total volume of effective spills = 15.1 barrels
    total_effective_bbl = sum(r[5] for r in effective_spills)
    assert round(total_effective_bbl, 1) == 15.1, f"Expected 15.1 bbl total volume, got {total_effective_bbl}"

def test_q5_well_0001_downtime_in_2025(db):
    """
    Q5: How many days was WELL-0001 down in 2025?
    Expected: 21 days from 3 weekly inspections where it was not producing oil:
    - 24 Jul 2025: delta 8.5 °C (air 43.1, wellhead 51.6)
    - 16 Oct 2025: delta 3.4 °C
    - 23 Oct 2025: delta -0.6 °C
    """
    start_date, end_date = get_date_window("2025")
    non_prod_count, downtime_days = calculate_downtime_days(db, "WELL-0001", start_date, end_date)

    assert non_prod_count == 3, f"Expected 3 non-producing inspections, got {non_prod_count}"
    assert downtime_days == 21, f"Expected 21 downtime days, got {downtime_days}"

def test_q6_northeast_block_7_top_downtime_both_windows(db):
    """
    Q6: Which 3 wells in Northeast Block 7 had the most downtime in the last 4 months?
    Expected: WELL-0121 (49 days), WELL-0138 (42 days), WELL-0107 (42 days).
    Tests both window interpretations:
    - Window A: 16 Jun 2026 to 16 Oct 2026 (literal text in document)
    - Window B: 17 Jun 2026 to 17 Oct 2026 (4 calendar months before TODAY = 17 Oct)
    """
    # Window A (document literal)
    start_a, end_a = get_date_window("last 4 months", use_doc_offset=True)
    ranked_a = rank_downtime_wells_in_area(db, "Northeast Block 7", start_a, end_a, limit=3)

    assert len(ranked_a) == 3
    assert ranked_a[0]["asset_id"] == "WELL-0121"
    assert ranked_a[0]["downtime_days"] == 49

    well_ids_a = {r["asset_id"] for r in ranked_a}
    assert well_ids_a == {"WELL-0121", "WELL-0138", "WELL-0107"}
    downtimes_a = {r["asset_id"]: r["downtime_days"] for r in ranked_a}
    assert downtimes_a["WELL-0121"] == 49
    assert downtimes_a["WELL-0138"] == 42
    assert downtimes_a["WELL-0107"] == 42

    # Window B (today = 17 Oct convention)
    start_b, end_b = get_date_window("last 4 months", use_doc_offset=False)
    ranked_b = rank_downtime_wells_in_area(db, "Northeast Block 7", start_b, end_b, limit=3)

    assert len(ranked_b) == 3
    well_ids_b = {r["asset_id"] for r in ranked_b}
    assert well_ids_b == {"WELL-0121", "WELL-0138", "WELL-0107"}
    downtimes_b = {r["asset_id"]: r["downtime_days"] for r in ranked_b}
    assert downtimes_b["WELL-0121"] == 49
    assert downtimes_b["WELL-0138"] == 42
    assert downtimes_b["WELL-0107"] == 42
