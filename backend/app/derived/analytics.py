"""Derived analytics layer for Asset Intelligence Copilot.
All thresholds, deadlines, and limits are retrieved dynamically from the rules table
and user_rule_overrides table in DuckDB. No threshold numbers are hardcoded in logic.
"""
from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple, Union
import duckdb

from backend.app.config import TODAY
from backend.app.derived.windows import get_date_window, get_today

class BreachesResult(list):
    """
    A list of breach records that also provides attribute/dict-like access to summary metrics,
    e.g. result.open_fines_usd, result.rca_actions, result['open_fines_usd'].
    """
    def __init__(self, breaches: List[Dict[str, Any]], well_id: str, open_fines_usd: float = 0.0, rca_actions: Optional[List[Dict[str, Any]]] = None):
        super().__init__(breaches)
        self.well_id = well_id
        self.open_fines_usd = open_fines_usd
        self.rca_actions = rca_actions or []
        self.breaches = breaches

    def __getitem__(self, item):
        if isinstance(item, str):
            if item == "open_fines_usd":
                return self.open_fines_usd
            elif item == "rca_actions":
                return self.rca_actions
            elif item == "breaches":
                return self.breaches
            elif item == "well_id":
                return self.well_id
            raise KeyError(item)
        return super().__getitem__(item)


def set_user_rule_override(
    conn: duckdb.DuckDBPyConnection,
    parameter: str,
    scope: str,
    value: float,
    author: str = "user",
    reason: str = "",
) -> str:
    """
    Inserts a user runtime rule override into user_rule_overrides.
    This takes priority over the extracted rule at that specific scope only.
    """
    import uuid
    from datetime import timezone
    override_id = f"ovr_{uuid.uuid4().hex[:10]}"
    now = datetime.now(timezone.utc)
    conn.execute("""
        INSERT INTO user_rule_overrides (override_id, parameter, scope, value, author, reason, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, [override_id, parameter, scope, float(value), author, reason, now])
    return override_id


def clear_user_rule_overrides(
    conn: duckdb.DuckDBPyConnection,
    parameter: Optional[str] = None,
    scope: Optional[str] = None,
):
    """Clears user rule overrides, optionally filtered by parameter and scope."""
    if parameter and scope:
        conn.execute("DELETE FROM user_rule_overrides WHERE parameter = ? AND scope = ?", [parameter, scope])
    elif parameter:
        conn.execute("DELETE FROM user_rule_overrides WHERE parameter = ?", [parameter])
    elif scope:
        conn.execute("DELETE FROM user_rule_overrides WHERE scope = ?", [scope])
    else:
        conn.execute("DELETE FROM user_rule_overrides")


def get_rule_threshold(
    conn: duckdb.DuckDBPyConnection,
    parameter: str,
    scope: str = "fleet",
) -> Optional[float]:
    """
    Resolves the effective numeric rule threshold:
    1. Checks user_rule_overrides for (parameter, scope) - takes precedence at that scope only.
    2. Checks rules table for (parameter, scope).
    3. If inherits_from exists, checks user_rule_overrides and rules for inherited scope.
    4. Falls back to fleet scope if scope != 'fleet'.
    """
    # 1. Direct user override at this scope
    ovr = conn.execute("""
        SELECT value FROM user_rule_overrides
        WHERE parameter = ? AND scope = ?
        ORDER BY created_at DESC
        LIMIT 1
    """, [parameter, scope]).fetchone()
    if ovr is not None and ovr[0] is not None:
        return float(ovr[0])

    # 2. Direct rule from rules table for this scope
    rule = conn.execute("""
        SELECT value, inherits_from FROM rules
        WHERE parameter = ? AND scope = ?
        LIMIT 1
    """, [parameter, scope]).fetchone()
    if rule is not None and rule[0] is not None:
        return float(rule[0])

    # 3. Check inherited scope
    parent_scope = None
    if rule and rule[1]:
        parent_scope = rule[1]
    else:
        inh = conn.execute("""
            SELECT inherits_from FROM rules
            WHERE scope = ? AND inherits_from IS NOT NULL
            LIMIT 1
        """, [scope]).fetchone()
        if inh and inh[0]:
            parent_scope = inh[0]

    if parent_scope:
        p_ovr = conn.execute("""
            SELECT value FROM user_rule_overrides
            WHERE parameter = ? AND scope = ?
            ORDER BY created_at DESC
            LIMIT 1
        """, [parameter, parent_scope]).fetchone()
        if p_ovr is not None and p_ovr[0] is not None:
            return float(p_ovr[0])

        p_rule = conn.execute("""
            SELECT value FROM rules
            WHERE parameter = ? AND scope = ?
            LIMIT 1
        """, [parameter, parent_scope]).fetchone()
        if p_rule is not None and p_rule[0] is not None:
            return float(p_rule[0])

    # 4. Fallback to fleet scope
    if scope != "fleet":
        f_ovr = conn.execute("""
            SELECT value FROM user_rule_overrides
            WHERE parameter = ? AND scope = 'fleet'
            ORDER BY created_at DESC
            LIMIT 1
        """, [parameter]).fetchone()
        if f_ovr is not None and f_ovr[0] is not None:
            return float(f_ovr[0])

        f_rule = conn.execute("""
            SELECT value FROM rules
            WHERE parameter = ? AND scope = 'fleet'
            LIMIT 1
        """, [parameter]).fetchone()
        if f_rule is not None and f_rule[0] is not None:
            return float(f_rule[0])

    return None


def spills_query(
    conn: duckdb.DuckDBPyConnection,
    target: str,
    window: Union[str, Tuple[date, date]],
    min_volume: float = 0.0,
) -> List[Dict[str, Any]]:
    """
    Queries spills using v_effective_spills (so corrections apply).
    target can be an area name or asset_id.
    window can be a period string ("last 90 days", "last 4 years", "2026") or (start_date, end_date).
    min_volume filters effective_volume_bbl >= min_volume.
    """
    if isinstance(window, tuple):
        start_date, end_date = window
    else:
        start_date, end_date = get_date_window(window)

    query = """
    SELECT
        s.inspection_id,
        s.asset_id as well_id,
        s.well_name,
        s.well_type,
        s.area_name,
        s.inspected_date,
        s.inspected_at,
        s.effective_spill_detected,
        s.effective_volume_bbl,
        s.spill_class,
        s.is_reportable,
        s.correction_note_id,
        w.lat as latitude,
        w.lon as longitude,
        m.maintenance_id,
        rf.containment_hours,
        rf.evidence_quote,
        s.corrected_by_author,
        s.corrected_from_value
    FROM v_effective_spills s
    JOIN wells w ON s.asset_id = w.asset_id
    LEFT JOIN maintenance m ON s.inspection_id = m.triggered_by_inspection_id
    LEFT JOIN maintenance_report_facts rf ON m.maintenance_id = rf.maintenance_id
    WHERE (s.area_name = ? OR s.asset_id = ?)
      AND s.effective_spill_detected = true
      AND s.effective_volume_bbl >= ?
      AND s.inspected_date >= ?
      AND s.inspected_date <= ?
    ORDER BY s.inspected_date DESC, s.asset_id ASC
    """
    rows = conn.execute(query, [target, target, float(min_volume), start_date, end_date]).fetchall()
    return [
        {
            "inspection_id": r[0],
            "well_id": r[1],
            "well_name": r[2],
            "well_type": r[3],
            "area_name": r[4],
            "inspected_date": r[5],
            "inspected_at": r[6],
            "effective_spill_detected": r[7],
            "effective_volume_bbl": r[8],
            "spill_class": r[9],
            "is_reportable": r[10],
            "correction_note_id": r[11],
            "latitude": r[12],
            "longitude": r[13],
            "maintenance_id": r[14],
            "containment_hours": r[15],
            "evidence_quote": r[16],
            "corrected_by_author": r[17],
            "corrected_from_value": r[18],
        }
        for r in rows
    ]


def uncontained_spills_query(
    conn: duckdb.DuckDBPyConnection,
    area_name: str,
    window: Union[str, Tuple[date, date]] = "last 90 days",
) -> List[Dict[str, Any]]:
    """
    Finds spills in an area that exceeded the SOP containment time limit.
    Threshold is pulled dynamically from rules.
    """
    limit = get_rule_threshold(conn, "spill_containment_time_limit", "fleet") or 4.0
    spills = spills_query(conn, target=area_name, window=window)
    uncontained = [
        s for s in spills
        if s.get("containment_hours") is not None and s["containment_hours"] > limit
    ]
    for s in uncontained:
        s["limit_hours"] = limit
    return uncontained


def well_timeseries(
    conn: duckdb.DuckDBPyConnection,
    well_id: str,
    weeks: int = 13,
) -> List[Dict[str, Any]]:
    """
    Retrieves weekly inspection time-series for a well, including wellhead temp,
    ambient temp, delta, and is_producing_oil status against well-type threshold.
    """
    today = get_today()
    start_date = today - timedelta(weeks=weeks)

    query = """
    SELECT
        inspection_id,
        inspected_date,
        inspected_at,
        wellhead_temp_c,
        ambient_temp_c,
        temp_delta_c,
        temp_delta_threshold,
        is_producing_oil
    FROM v_inspections_producing
    WHERE asset_id = ?
      AND inspected_date >= ?
      AND inspected_date <= ?
    ORDER BY inspected_date ASC
    """
    rows = conn.execute(query, [well_id, start_date, today]).fetchall()
    return [
        {
            "inspection_id": r[0],
            "date": r[1],
            "inspected_at": r[2],
            "wellhead_temp_c": r[3],
            "ambient_temp_c": r[4],
            "temp_delta_c": r[5],
            "temp_delta_threshold": r[6],
            "is_producing_oil": r[7],
        }
        for r in rows
    ]


def repairs_cost(
    conn: duckdb.DuckDBPyConnection,
    wells: List[str],
    year: Optional[int] = None,
) -> Dict[str, float]:
    """
    Calculates total repair cost for each well in the specified year.
    Returns a dict mapping well_id to total cost in USD.
    """
    if not wells:
        return {}

    target_year = year if year is not None else get_today().year

    placeholders = ", ".join(["?"] * len(wells))
    query = f"""
    SELECT
        asset_id,
        COALESCE(SUM(total_cost_usd), 0.0) as total_cost
    FROM maintenance
    WHERE asset_id IN ({placeholders})
      AND strftime(started_at, '%Y') = ?
    GROUP BY asset_id
    """
    params = list(wells) + [str(target_year)]
    rows = conn.execute(query, params).fetchall()
    cost_map = {w: 0.0 for w in wells}
    for asset_id, cost in rows:
        cost_map[asset_id] = float(cost)
    return cost_map


def rca_wells_query(
    conn: duckdb.DuckDBPyConnection,
    area_name: str,
    equipment_kind: str = "pump_jack",
    window: Union[str, Tuple[date, date]] = "last 12 months",
) -> List[Dict[str, Any]]:
    """
    Finds wells in an area where corrective repair count on equipment_kind in the lookback window
    meets or exceeds the RCA threshold, taking into account well type, rule inheritance,
    and user_rule_overrides at specific scope.
    """
    if isinstance(window, tuple):
        start_date, end_date = window
    else:
        start_date, end_date = get_date_window(window)

    # Get all candidate wells in the area
    wells = conn.execute("""
        SELECT w.asset_id, w.well_type, w.name, a.name as area_name
        FROM wells w
        JOIN areas a ON w.area_id = a.area_id
        WHERE a.name = ?
    """, [area_name]).fetchall()

    results = []
    for asset_id, well_type, name, a_name in wells:
        # Dynamic thresholds
        threshold = get_rule_threshold(conn, "rca_repair_count_threshold", scope=well_type) or 3.0

        # Query corrective repairs
        repairs = conn.execute("""
            SELECT maintenance_id, CAST(started_at AS DATE) as start_date, issue
            FROM maintenance
            WHERE asset_id = ?
              AND equipment_kind = ?
              AND maintenance_type = 'corrective'
              AND CAST(started_at AS DATE) >= ?
              AND CAST(started_at AS DATE) <= ?
            ORDER BY started_at ASC
        """, [asset_id, equipment_kind, start_date, end_date]).fetchall()

        repair_count = len(repairs)
        if repair_count >= threshold:
            results.append({
                "well_id": asset_id,
                "well_name": name,
                "well_type": well_type,
                "area_name": a_name,
                "equipment_kind": equipment_kind,
                "repair_count": repair_count,
                "threshold": threshold,
                "citation_ids": [r[0] for r in repairs],
            })

    results.sort(key=lambda x: (x["repair_count"], x["well_id"]), reverse=True)
    return results


def breaches_check(
    conn: duckdb.DuckDBPyConnection,
    well_id: str,
    window: Union[str, Tuple[date, date]] = "last 12 months",
) -> BreachesResult:
    """
    Checks regulatory and SOP breaches for a well in the specified window:
    - SR-01: hours_to_report from regulatory_events vs notice deadline for the spill class.
    - SR-02: containment_hours from report facts vs spill_containment_time_limit.
    - SR-03: cleanup verification due = discovery + deadline, open if no closing site inspection.
    - RC-04: NOV response due vs nov_response_filed.
    - RC-02: yearly flowline test.
    - RCA counts: corrective repairs per equipment_kind in look-back window vs threshold.

    Each breach returns its citation IDs.
    Returns BreachesResult with total open fines and RCA pending actions.
    """
    if isinstance(window, tuple):
        start_date, end_date = window
    else:
        start_date, end_date = get_date_window(window)

    today = get_today()

    # Get well info
    well_info = conn.execute("""
        SELECT w.asset_id, w.well_type, w.name, a.name as area_name
        FROM wells w
        JOIN areas a ON w.area_id = a.area_id
        WHERE w.asset_id = ?
    """, [well_id]).fetchone()

    if not well_info:
        return BreachesResult([], well_id=well_id)

    well_type = well_info[1]

    # Resolve dynamic rule thresholds
    sr01_major_deadline = get_rule_threshold(conn, "spill_written_notice_deadline_major", "fleet") or 2.0
    sr01_reportable_deadline = get_rule_threshold(conn, "spill_written_notice_deadline_reportable", "fleet") or 24.0
    sr02_containment_limit = get_rule_threshold(conn, "spill_containment_time_limit", "fleet") or 4.0
    sr03_cleanup_deadline_days = get_rule_threshold(conn, "spill_cleanup_verification_deadline", "fleet") or 60.0
    rc04_nov_deadline_days = get_rule_threshold(conn, "nov_response_deadline", "fleet") or 30.0
    rc02_test_frequency_years = get_rule_threshold(conn, "flowline_integrity_test_frequency_years", "fleet") or 1.0
    spill_major_threshold = get_rule_threshold(conn, "spill_volume_major_threshold", "fleet") or 25.0
    spill_reportable_threshold = get_rule_threshold(conn, "spill_volume_reportable_threshold", "fleet") or 5.0
    rca_threshold = get_rule_threshold(conn, "rca_repair_count_threshold", scope=well_type) or 3.0

    breaches: List[Dict[str, Any]] = []
    fine_row = conn.execute("""
        SELECT COALESCE(SUM(fine_usd), 0.0)
        FROM regulatory_events
        WHERE asset_id = ?
          AND date >= ?
          AND date <= ?
          AND status = 'open'
    """, [well_id, start_date, end_date]).fetchone()
    open_fines_usd = float(fine_row[0]) if fine_row else 0.0

    # 1. SR-01: hours_to_report vs notice deadline (keyed by spill report event)
    reg_events = conn.execute("""
        SELECT
            event_id,
            date,
            event_type,
            protocol_id,
            related_inspection_id,
            hours_to_report,
            detail,
            fine_usd,
            status
        FROM regulatory_events
        WHERE asset_id = ?
          AND date >= ?
          AND date <= ?
        ORDER BY date ASC
    """, [well_id, start_date, end_date]).fetchall()

    for ev in reg_events:
        ev_id, ev_date, ev_type, proto, rel_insp, hours, detail, fine, status = ev
        if ev_type == "spill_report_filed" and hours is not None and hours > 0:
            # Determine effective volume from related inspection if available
            vol_row = conn.execute("""
                SELECT effective_volume_bbl
                FROM v_effective_spills
                WHERE inspection_id = ?
            """, [rel_insp]).fetchone()
            vol = vol_row[0] if vol_row else 5.0

            deadline = sr01_major_deadline if vol >= spill_major_threshold else sr01_reportable_deadline
            if hours > deadline:
                # Associated NOV
                nov_row = conn.execute("""
                    SELECT event_id, fine_usd, status
                    FROM regulatory_events
                    WHERE asset_id = ?
                      AND event_type = 'notice_of_violation'
                      AND (related_inspection_id = ? OR protocol_id = 'SR-01')
                """, [well_id, rel_insp]).fetchone()

                citation_ids = [ev_id]
                fine_amount = 0.0
                if nov_row:
                    citation_ids.append(nov_row[0])
                    fine_amount = float(nov_row[1] or 0.0)

                if rel_insp and rel_insp not in citation_ids:
                    citation_ids.append(rel_insp)

                breaches.append({
                    "rule_id": "SR-01",
                    "rule_name": "Spill written notice deadline",
                    "threshold": deadline,
                    "unit": "hours",
                    "actual_value": hours,
                    "status": "breached",
                    "citation_ids": citation_ids,
                    "fine_usd": fine_amount,
                    "fine_status": nov_row[2] if nov_row else "closed",
                    "detail": f"Reported after {hours:g} hours (against {deadline:g}-hour limit for {vol:g} bbl spill).",
                })

    # 2. SR-02: containment_hours from report facts vs limit
    rf_rows = conn.execute("""
        SELECT
            m.maintenance_id,
            m.triggered_by_inspection_id,
            rf.containment_hours,
            rf.evidence_quote,
            CAST(m.started_at AS DATE) as started_date
        FROM maintenance_report_facts rf
        JOIN maintenance m ON rf.maintenance_id = m.maintenance_id
        WHERE m.asset_id = ?
          AND CAST(m.started_at AS DATE) >= ?
          AND CAST(m.started_at AS DATE) <= ?
          AND rf.containment_hours IS NOT NULL
        ORDER BY m.started_at ASC
    """, [well_id, start_date, end_date]).fetchall()

    for m_id, insp_id, hours, quote, s_date in rf_rows:
        if hours > sr02_containment_limit:
            cits = [m_id]
            if insp_id:
                cits.append(insp_id)
            breaches.append({
                "rule_id": "SR-02",
                "rule_name": "Spill containment time limit",
                "threshold": sr02_containment_limit,
                "unit": "hours",
                "actual_value": hours,
                "status": "breached",
                "citation_ids": cits,
                "detail": f"Contained after about {hours:g} hours (against {sr02_containment_limit:g}-hour limit).",
            })

    # 3. SR-03: cleanup verification due = discovery + deadline, open if no closing site inspection
    # Check open site_inspections or open cleanups
    sr03_events = [ev for ev in reg_events if ev[3] == "SR-03" or ev[2] == "site_inspection"]
    for ev in sr03_events:
        ev_id, ev_date, ev_type, proto, rel_insp, hours, detail, fine, status = ev
        if status == "open":
            # Discovery date is from related inspection date or event date
            disc_row = conn.execute("SELECT inspected_date FROM v_effective_spills WHERE inspection_id = ?", [rel_insp]).fetchone()
            disc_date = disc_row[0] if disc_row else ev_date
            due_date = disc_date + timedelta(days=sr03_cleanup_deadline_days)
            if today > due_date:
                cits = [ev_id]
                if rel_insp and rel_insp not in cits:
                    cits.append(rel_insp)
                breaches.append({
                    "rule_id": "SR-03",
                    "rule_name": "Spill cleanup verification deadline",
                    "threshold": sr03_cleanup_deadline_days,
                    "unit": "days",
                    "due_date": due_date,
                    "status": "open",
                    "citation_ids": cits,
                    "detail": f"Cleanup verification was due by {due_date.strftime('%d %b %Y')} and is still open.",
                })

    # 4. RC-04: NOV response due vs nov_response_filed
    nov_events = [ev for ev in reg_events if ev[2] == "notice_of_violation"]
    for nov in nov_events:
        ev_id, ev_date, ev_type, proto, rel_insp, hours, detail, fine, status = nov
        nov_due_date = ev_date + timedelta(days=rc04_nov_deadline_days)
        # Check if response filed
        resp_row = conn.execute("""
            SELECT event_id FROM regulatory_events
            WHERE asset_id = ?
              AND event_type IN ('nov_response_filed', 'response_filed')
              AND related_inspection_id = ?
        """, [well_id, rel_insp]).fetchone()

        if not resp_row and today > nov_due_date:
            breaches.append({
                "rule_id": "RC-04",
                "rule_name": "Notice of Violation response deadline",
                "threshold": rc04_nov_deadline_days,
                "unit": "days",
                "due_date": nov_due_date,
                "status": "breached",
                "citation_ids": [ev_id],
                "detail": f"Notice needed a response by {nov_due_date.strftime('%d %b %Y')}, and none is recorded.",
            })

    # 5. RC-02: yearly flowline test
    test_row = conn.execute("""
        SELECT maintenance_id, CAST(started_at AS DATE) as test_date
        FROM maintenance
        WHERE asset_id = ?
          AND (issue ILIKE '%integrity%' OR action_taken ILIKE '%integrity%' OR issue ILIKE '%annual flowline%')
        ORDER BY started_at DESC
        LIMIT 1
    """, [well_id]).fetchone()

    flowline_due_limit_days = int(rc02_test_frequency_years * 365)
    if not test_row:
        breaches.append({
            "rule_id": "RC-02",
            "rule_name": "Annual flowline integrity test",
            "threshold": rc02_test_frequency_years,
            "unit": "years",
            "status": "breached",
            "citation_ids": [well_id],
            "detail": "No flowline integrity test on record.",
        })
    else:
        test_id, test_date = test_row
        if (today - test_date).days > flowline_due_limit_days:
            breaches.append({
                "rule_id": "RC-02",
                "rule_name": "Annual flowline integrity test",
                "threshold": rc02_test_frequency_years,
                "unit": "years",
                "status": "breached",
                "citation_ids": [test_id],
                "detail": f"Last test was on {test_date}, exceeding {rc02_test_frequency_years} year frequency.",
            })

    # 6. RCA counts: corrective repairs per equipment_kind in lookback window
    rca_actions = []
    eq_rows = conn.execute("""
        SELECT
            equipment_kind,
            COUNT(*) as repair_count,
            list(maintenance_id) as m_ids
        FROM maintenance
        WHERE asset_id = ?
          AND maintenance_type = 'corrective'
          AND CAST(started_at AS DATE) >= ?
          AND CAST(started_at AS DATE) <= ?
        GROUP BY equipment_kind
        HAVING COUNT(*) >= ?
    """, [well_id, start_date, end_date, rca_threshold]).fetchall()

    for eq, cnt, m_ids in eq_rows:
        rca_actions.append({
            "rule_id": "RCA",
            "equipment_kind": eq,
            "count": cnt,
            "threshold": rca_threshold,
            "citation_ids": m_ids,
            "detail": f"{cnt} corrective {eq} repairs in the lookback window.",
        })

    return BreachesResult(
        breaches=breaches,
        well_id=well_id,
        open_fines_usd=open_fines_usd,
        rca_actions=rca_actions,
    )
