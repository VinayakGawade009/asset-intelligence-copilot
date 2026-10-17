import sys
from pathlib import Path
import pytest

# Ensure project root in sys.path
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from backend.app.db.connection import get_connection

@pytest.fixture(scope="module")
def db_conn():
    conn = get_connection(read_only=True)
    yield conn
    conn.close()

def find_rule(conn, scope=None, param_substr=None):
    """Helper to query the rules table with flexible matching."""
    query = "SELECT rule_id, scope, parameter, value, unit, description FROM rules WHERE 1=1"
    params = []
    if scope:
        query += " AND scope = ?"
        params.append(scope)
    if param_substr:
        query += " AND LOWER(parameter) LIKE ?"
        params.append(f"%{param_substr.lower()}%")
    
    return conn.execute(query, params).fetchall()

def test_t200_producing_temp_delta(db_conn):
    """Fact: T200 producing delta is 15 degrees C."""
    matches = find_rule(db_conn, scope="T200", param_substr="producing")
    assert matches, "No rule found for T200 producing temperature delta"
    # Find matching rule with value 15.0
    matched_values = [r[3] for r in matches]
    assert 15.0 in matched_values, f"Expected 15.0 °C delta for T200, got: {matches}"

def test_t350_producing_temp_delta(db_conn):
    """Fact: T350 producing delta is 20 degrees C."""
    matches = find_rule(db_conn, scope="T350", param_substr="producing")
    assert matches, "No rule found for T350 producing temperature delta"
    matched_values = [r[3] for r in matches]
    assert 20.0 in matched_values, f"Expected 20.0 °C delta for T350, got: {matches}"

def test_reportable_spill_threshold_and_notice(db_conn):
    """Fact: Reportable spill threshold is 5 bbl with a 24-hour written notice."""
    # Check volume threshold = 5 bbl
    vol_matches = find_rule(db_conn, scope="fleet", param_substr="reportable")
    vol_values = [r[3] for r in vol_matches if "notice" not in r[2].lower()]
    assert 5.0 in vol_values, f"Expected 5.0 bbl threshold for reportable spill, got: {vol_matches}"

    # Check written notice deadline = 24 hours
    notice_matches = find_rule(db_conn, scope="fleet", param_substr="notice")
    reportable_notice = [r[3] for r in notice_matches if "reportable" in r[2].lower() or "sr_01" in r[0].lower()]
    assert 24.0 in reportable_notice or 24.0 in [r[3] for r in notice_matches], (
        f"Expected 24-hour written notice deadline for reportable spill, got: {notice_matches}"
    )

def test_major_spill_threshold_and_notice(db_conn):
    """Fact: Major spill is 25 bbl with 2 hours."""
    # Check volume threshold = 25 bbl
    major_matches = find_rule(db_conn, scope="fleet", param_substr="major")
    major_vols = [r[3] for r in major_matches if "notice" not in r[2].lower()]
    assert 25.0 in major_vols, f"Expected 25.0 bbl threshold for major spill, got: {major_matches}"

    # Check written notice deadline = 2 hours
    major_notice = [r[3] for r in major_matches if "notice" in r[2].lower() or "hour" in r[4].lower()]
    assert 2.0 in major_notice or 2.0 in [r[3] for r in major_matches], (
        f"Expected 2-hour report deadline for major spill, got: {major_matches}"
    )

def test_containment_limit(db_conn):
    """Fact: Containment limit is 4 hours."""
    matches = find_rule(db_conn, scope="fleet", param_substr="containment")
    assert matches, "No containment rule found in fleet rules"
    matched_values = [r[3] for r in matches]
    assert 4.0 in matched_values, f"Expected 4.0 hours containment limit, got: {matches}"

def test_cleanup_verification_deadline(db_conn):
    """Fact: Cleanup verification is 60 days."""
    matches = find_rule(db_conn, scope="fleet", param_substr="cleanup")
    if not matches:
        matches = find_rule(db_conn, scope="fleet", param_substr="verification")
    assert matches, "No cleanup verification rule found in fleet rules"
    matched_values = [r[3] for r in matches]
    assert 60.0 in matched_values, f"Expected 60.0 days cleanup verification deadline, got: {matches}"

def test_nov_response_deadline(db_conn):
    """Fact: NOV response is 30 days."""
    matches = find_rule(db_conn, scope="fleet", param_substr="nov")
    if not matches:
        matches = find_rule(db_conn, scope="fleet", param_substr="violation")
    assert matches, "No NOV response deadline found in fleet rules"
    matched_values = [r[3] for r in matches]
    assert 30.0 in matched_values, f"Expected 30.0 days for NOV response, got: {matches}"

def test_root_cause_threshold_and_window(db_conn):
    """Fact: Root-cause threshold is 3 corrective repairs in 12 months."""
    rca_matches = find_rule(db_conn, param_substr="rca")
    if not rca_matches:
        rca_matches = find_rule(db_conn, param_substr="root_cause")
    if not rca_matches:
        rca_matches = find_rule(db_conn, param_substr="repair")
    
    assert rca_matches, "No root-cause analysis rule found"
    matched_values = [r[3] for r in rca_matches]
    assert 3.0 in matched_values, f"Expected 3 repairs threshold for RCA, got: {rca_matches}"
    assert 12.0 in matched_values, f"Expected 12 months look-back window for RCA, got: {rca_matches}"

def test_rule_scoping_no_mismatches(db_conn):
    """Check: A rule's scope must be the well type it applies to, without parameter/scope mismatch."""
    rows = db_conn.execute("SELECT rule_id, scope, parameter, description FROM rules").fetchall()
    mismatches = []
    for r_id, scope, param, desc in rows:
        p_lower = (param or "").lower()
        id_lower = (r_id or "").lower()
        if (p_lower.startswith("t200") or id_lower.startswith("t200")) and scope == "T350":
            mismatches.append((r_id, scope, param, "T200 rule in T350 scope"))
        if (p_lower.startswith("t350") or id_lower.startswith("t350")) and scope == "T200":
            mismatches.append((r_id, scope, param, "T350 rule in T200 scope"))

    assert len(mismatches) == 0, f"Found scope mismatches in rules: {mismatches}"

def test_t350_rule_inheritance(db_conn):
    """Check: T350 records inherits_from = 'T200' for rules that follow T200 by default (e.g. RCA)."""
    rows = db_conn.execute(
        "SELECT rule_id, scope, parameter, value, inherits_from FROM rules WHERE scope = 'T350' AND inherits_from = 'T200'"
    ).fetchall()
    assert len(rows) > 0, "Expected at least one T350 rule with inherits_from = 'T200'"
    
    # Check that RCA or scope inheritance is present
    rca_inherited = [r for r in rows if "rca" in (r[2] or "").lower() or "escalation" in (r[2] or "").lower() or "scope" in (r[2] or "").lower()]
    assert len(rca_inherited) > 0, f"Expected RCA or scope inheritance for T350, got: {rows}"

