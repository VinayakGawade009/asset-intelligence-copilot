"""Unit and integration tests for derived analytics layer (Stage 3 Part B).
Tests against 03-evaluation-queries.md:
- Q3: Time-series of temperatures for WELL-0001 (13 readings, non-producing on 8 Oct and 15 Oct).
- Q7: Northeast Block 8 spills map with coordinates (4 wells).
- Q8: Heatmap of 2026 spills by area (row totals 35, 43, 37, 26).
- Q9: WELL-0001 breaches (4 breaches, USD 5,000 fine open).
- Q10: Southwest Block 24 uncontained spills (WELL-0082 ~7.1h, WELL-0100 ~8.1h).
- Q11: 2026 repair costs (WELL-0121 25,794, WELL-0138 46,942, WELL-0107 5,176).
- Q14: Pump jack RCA counts and user rule override (T350 override of 2 adds WELL-0120 and not WELL-0102).
"""
import sys
from pathlib import Path
from datetime import date
import pytest

# Ensure project root in sys.path
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from backend.app.db.connection import get_connection
from backend.app.derived import (
    create_derived_views,
    spills_query,
    uncontained_spills_query,
    breaches_check,
    repairs_cost,
    well_timeseries,
    rca_wells_query,
    set_user_rule_override,
    get_rule_threshold,
    clear_user_rule_overrides,
)

@pytest.fixture(scope="module")
def db():
    conn = get_connection(read_only=False)
    create_derived_views(conn)
    yield conn
    clear_user_rule_overrides(conn)
    conn.close()


def test_q3_well_0001_timeseries(db):
    """
    Q3: Show a line chart of WELL-0001's wellhead temperature against air temperature
    for the last 13 weeks, and mark when it was not producing oil.
    Expected: 13 readings (23 Jul to 15 Oct 2026). Not producing oil on 8 Oct and 15 Oct.
    """
    series = well_timeseries(db, "WELL-0001", weeks=13)
    assert len(series) == 13, f"Expected 13 weekly readings, got {len(series)}"

    dates = [s["date"] for s in series]
    assert dates[0] == date(2026, 7, 23), f"Expected first date 2026-07-23, got {dates[0]}"
    assert dates[-1] == date(2026, 10, 15), f"Expected last date 2026-10-15, got {dates[-1]}"

    non_producing_dates = [s["date"] for s in series if not s["is_producing_oil"]]
    assert non_producing_dates == [date(2026, 10, 8), date(2026, 10, 15)], (
        f"Expected non-producing on 8 Oct and 15 Oct, got {non_producing_dates}"
    )

    producing_dates = [s["date"] for s in series if s["is_producing_oil"]]
    assert len(producing_dates) == 11, f"Expected 11 producing readings, got {len(producing_dates)}"


def test_q7_northeast_block_8_spills_map(db):
    """
    Q7: Show on a map every well in Northeast Block 8 with a real spill in the last 90 days.
    Expected: 4 wells with coordinates:
    - WELL-0151 (24 Sep 2026, 4.5 bbl, lat 32.12246, lon -102.18445)
    - WELL-0165 (30 Jul 2026, 1.2 bbl, lat 32.15665, lon -102.14522)
    - WELL-0175 (30 Jul 2026, 3.9 bbl, lat 32.18020, lon -102.14790)
    - WELL-0186 (23 Jul 2026, 0.6 bbl, lat 32.17552, lon -102.17775)
    """
    spills = spills_query(db, target="Northeast Block 8", window="last 90 days")
    well_ids = [s["well_id"] for s in spills]
    assert sorted(well_ids) == ["WELL-0151", "WELL-0165", "WELL-0175", "WELL-0186"], (
        f"Expected 4 wells in Block 8, got {sorted(well_ids)}"
    )

    by_id = {s["well_id"]: s for s in spills}

    # Verify coordinates and volumes
    assert round(by_id["WELL-0151"]["effective_volume_bbl"], 1) == 4.5
    assert round(by_id["WELL-0151"]["latitude"], 5) == 32.12246
    assert round(by_id["WELL-0151"]["longitude"], 5) == -102.18445

    assert round(by_id["WELL-0165"]["effective_volume_bbl"], 1) == 1.2
    assert round(by_id["WELL-0165"]["latitude"], 5) == 32.15665
    assert round(by_id["WELL-0165"]["longitude"], 5) == -102.14522

    assert round(by_id["WELL-0175"]["effective_volume_bbl"], 1) == 3.9
    assert round(by_id["WELL-0175"]["latitude"], 5) == 32.18020
    assert round(by_id["WELL-0175"]["longitude"], 5) == -102.14790

    assert round(by_id["WELL-0186"]["effective_volume_bbl"], 1) == 0.6
    assert round(by_id["WELL-0186"]["latitude"], 5) == 32.17552
    assert round(by_id["WELL-0186"]["longitude"], 5) == -102.17775


def test_q8_heatmap_2026_spills_row_totals(db):
    """
    Q8: Show a heatmap of 2026 spills by geographic area and month.
    Expected row totals:
    - Southwest Block 23: 35
    - Southwest Block 24: 43
    - Northeast Block 7: 37
    - Northeast Block 8: 26
    """
    rows = db.execute("""
        SELECT
            area_name,
            COUNT(*) as total_spills
        FROM v_effective_spills
        WHERE effective_spill_detected = true
          AND strftime(inspected_date, '%Y') = '2026'
        GROUP BY area_name
    """).fetchall()

    area_totals = {r[0]: r[1] for r in rows}

    assert area_totals["Southwest Block 23"] == 35, f"Expected 35 for SW23, got {area_totals.get('Southwest Block 23')}"
    assert area_totals["Southwest Block 24"] == 43, f"Expected 43 for SW24, got {area_totals.get('Southwest Block 24')}"
    assert area_totals["Northeast Block 7"] == 37, f"Expected 37 for NE7, got {area_totals.get('Northeast Block 7')}"
    assert area_totals["Northeast Block 8"] == 26, f"Expected 26 for NE8, got {area_totals.get('Northeast Block 8')}"


def test_q9_well_0001_breaches_and_open_fine(db):
    """
    Q9: Which rules has WELL-0001 broken in the last 12 months, and what is still open?
    Expected: four breaches, all from the 11 Jun 2026 spill of 6.8 bbl. USD 5,000 in fines, still open.
    - SR-01: reported after 41 hours (REG-0001-001) vs 24-hour limit. Led to NOV REG-0001-002 with USD 5,000 fine.
    - SR-02: contained after about 7 hours vs 4-hour limit (MNT-0001-029).
    - SR-03: cleanup verification was due by 10 Aug 2026 and is still open (REG-0001-003).
    - RC-04: notice needed a response by 30 Jul 2026, none is recorded.
    """
    res = breaches_check(db, "WELL-0001", window="last 12 months")

    assert len(res) == 4, f"Expected exactly 4 breaches for WELL-0001, got {len(res)}: {[b['rule_id'] for b in res]}"
    assert res.open_fines_usd == 5000.0, f"Expected USD 5,000 open fine, got {res.open_fines_usd}"

    rule_ids = {b["rule_id"]: b for b in res}
    assert "SR-01" in rule_ids, "Missing SR-01 breach"
    assert "SR-02" in rule_ids, "Missing SR-02 breach"
    assert "SR-03" in rule_ids, "Missing SR-03 breach"
    assert "RC-04" in rule_ids, "Missing RC-04 breach"

    # Citations check
    sr01 = rule_ids["SR-01"]
    assert "REG-0001-001" in sr01["citation_ids"], f"SR-01 citations missing REG-0001-001: {sr01['citation_ids']}"
    assert "REG-0001-002" in sr01["citation_ids"], f"SR-01 citations missing REG-0001-002: {sr01['citation_ids']}"
    assert sr01["actual_value"] == 41.0
    assert sr01["threshold"] == 24.0

    sr02 = rule_ids["SR-02"]
    assert "MNT-0001-029" in sr02["citation_ids"], f"SR-02 citations missing MNT-0001-029: {sr02['citation_ids']}"
    assert sr02["actual_value"] == 7.0
    assert sr02["threshold"] == 4.0

    sr03 = rule_ids["SR-03"]
    assert "REG-0001-003" in sr03["citation_ids"], f"SR-03 citations missing REG-0001-003: {sr03['citation_ids']}"
    assert sr03["status"] == "open"

    rc04 = rule_ids["RC-04"]
    assert "REG-0001-002" in rc04["citation_ids"], f"RC-04 citations missing REG-0001-002: {rc04['citation_ids']}"

    # Flowline integrity test (RC-02) was passed on 7 Mar 2026, so NOT a breach
    assert "RC-02" not in rule_ids, "RC-02 flowline test should not be flagged as a breach"

    # RCA pending actions: 3 corrective flowline repairs
    assert len(res.rca_actions) >= 1
    flowline_rca = next((a for a in res.rca_actions if a["equipment_kind"] == "flowline"), None)
    assert flowline_rca is not None, "Expected RCA pending action for flowline"
    assert flowline_rca["count"] == 3
    assert "MNT-0001-028" in flowline_rca["citation_ids"]
    assert "MNT-0001-029" in flowline_rca["citation_ids"]
    assert "MNT-0001-032" in flowline_rca["citation_ids"]


def test_q10_southwest_block_24_uncontained_spills(db):
    """
    Q10: In Southwest Block 24, which spills in the last 90 days were not contained within the SOP time limit?
    Expected: 2 spills:
    - WELL-0082: contained after about 7.1 hours (report MNT-0082-028, inspection INS-0082-0198).
    - WELL-0100: contained after about 8.1 hours (report MNT-0100-034, inspection INS-0100-0196).
    """
    uncontained = uncontained_spills_query(db, "Southwest Block 24", window="last 90 days")
    assert len(uncontained) == 2, f"Expected exactly 2 uncontained spills in SW24, got {len(uncontained)}"

    by_id = {s["well_id"]: s for s in uncontained}
    assert "WELL-0082" in by_id, "Missing WELL-0082 in uncontained spills"
    assert "WELL-0100" in by_id, "Missing WELL-0100 in uncontained spills"

    assert round(by_id["WELL-0082"]["containment_hours"], 1) == 7.1
    assert by_id["WELL-0082"]["maintenance_id"] == "MNT-0082-028"
    assert by_id["WELL-0082"]["inspection_id"] == "INS-0082-0198"

    assert round(by_id["WELL-0100"]["containment_hours"], 1) == 8.1
    assert by_id["WELL-0100"]["maintenance_id"] == "MNT-0100-034"
    assert by_id["WELL-0100"]["inspection_id"] == "INS-0100-0196"


def test_q11_repair_costs_2026(db):
    """
    Q11: What have repairs cost this year for WELL-0121, WELL-0138, and WELL-0107?
    Expected:
    - WELL-0121: USD 25,794
    - WELL-0138: USD 46,942
    - WELL-0107: USD 5,176
    """
    wells = ["WELL-0121", "WELL-0138", "WELL-0107"]
    costs = repairs_cost(db, wells=wells, year=2026)

    assert costs["WELL-0121"] == 25794.0, f"Expected 25794.0 for WELL-0121, got {costs['WELL-0121']}"
    assert costs["WELL-0138"] == 46942.0, f"Expected 46942.0 for WELL-0138, got {costs['WELL-0138']}"
    assert costs["WELL-0107"] == 5176.0, f"Expected 5176.0 for WELL-0107, got {costs['WELL-0107']}"


def test_q14_rca_pump_jack_rules_and_user_override(db):
    """
    Q14:
    First half: Which wells in Northeast Block 7 need a root-cause analysis on their pump jack?
    Expected: WELL-0108 (3, T350), WELL-0121 (3, T200), WELL-0138 (3, T350).

    Second half: User sets rule override for all T350 wells: threshold = 2 repairs.
    Expected: WELL-0108, WELL-0120, WELL-0121, WELL-0138.
    - WELL-0120 (T350 with 2 repairs) is now added.
    - WELL-0102 (T200 with 2 repairs) is NOT added because T200 rule is untouched.
    """
    try:
        clear_user_rule_overrides(db)

        # Baseline: default rules (threshold 3)
        res_before = rca_wells_query(db, area_name="Northeast Block 7", equipment_kind="pump_jack", window="last 12 months")
        wells_before = sorted([w["well_id"] for w in res_before])
        assert wells_before == ["WELL-0108", "WELL-0121", "WELL-0138"], (
            f"Expected ['WELL-0108', 'WELL-0121', 'WELL-0138'] before override, got {wells_before}"
        )

        # Apply user rule override at scope 'T350' ONLY
        set_user_rule_override(
            conn=db,
            parameter="rca_repair_count_threshold",
            scope="T350",
            value=2.0,
            author="Michael Turner",
            reason="Our team now wants a pump jack root-cause analysis after 2 repairs, not 3.",
        )

        # Verify threshold lookup isolation:
        # T350 must be 2.0 (from override)
        assert get_rule_threshold(db, "rca_repair_count_threshold", scope="T350") == 2.0
        # T200 must remain 3.0 (from extracted rule, unaffected by T350 override)
        assert get_rule_threshold(db, "rca_repair_count_threshold", scope="T200") == 3.0

        # Query with override active
        res_after = rca_wells_query(db, area_name="Northeast Block 7", equipment_kind="pump_jack", window="last 12 months")
        wells_after = sorted([w["well_id"] for w in res_after])

        assert wells_after == ["WELL-0108", "WELL-0120", "WELL-0121", "WELL-0138"], (
            f"Expected ['WELL-0108', 'WELL-0120', 'WELL-0121', 'WELL-0138'] after T350 override, got {wells_after}"
        )
        assert "WELL-0120" in wells_after, "WELL-0120 (T350) should be included under threshold=2"
        assert "WELL-0102" not in wells_after, "WELL-0102 (T200) must NOT be included as T200 threshold remains 3"

    finally:
        clear_user_rule_overrides(db)
