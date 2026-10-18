"""Agent tools for Asset Intelligence Copilot.
All tools are deterministic and typed. Each tool returns a ToolResult with:
- rows: structured data rows
- citations: citations (id, kind, label, detail)
- flags: flags (kind, text, source_ids)
- visual: UI_CONTRACT.md compliant visual spec
- summary_text: plain-text summary of findings for grounded LLM answer generation
"""
import re
from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple, Union
import duckdb
from pydantic import BaseModel, Field

from backend.app.config import TODAY
from backend.app.derived.windows import get_date_window, get_today
from backend.app.derived.analytics import (
    spills_query as derived_spills_query,
    uncontained_spills_query as derived_uncontained_spills_query,
    breaches_check as derived_breaches_check,
    repairs_cost as derived_repairs_cost,
    well_timeseries as derived_well_timeseries,
    rca_wells_query as derived_rca_wells_query,
    get_rule_threshold,
)
from backend.app.derived.views import (
    calculate_downtime_days,
    rank_downtime_wells_in_area,
)

class ToolResult(BaseModel):
    tool_name: str
    summary_text: str
    rows: List[Dict[str, Any]] = Field(default_factory=list)
    citations: List[Dict[str, Any]] = Field(default_factory=list)
    flags: List[Dict[str, Any]] = Field(default_factory=list)
    visual: Optional[Dict[str, Any]] = None


# Entity resolution helpers

def resolve_well_id(input_str: Optional[str], conn: duckdb.DuckDBPyConnection) -> Optional[str]:
    """Resolves fuzzy well identifier to canonical WELL-xxxx format."""
    if not input_str:
        return None
    s = str(input_str).strip()

    # If it contains area terms, it's an area, NOT a well
    s_lower = s.lower()
    if "block" in s_lower or "area" in s_lower or "southwest" in s_lower or "northeast" in s_lower or s_lower == "fleet":
        return None

    # Exact pattern WELL-xxxx
    match = re.search(r'WELL-(\d{1,4})', s, re.IGNORECASE)
    if match:
        num = int(match.group(1))
        canonical = f"WELL-{num:04d}"
        exists = conn.execute("SELECT 1 FROM wells WHERE asset_id = ?", [canonical]).fetchone()
        if exists:
            return canonical

    # Pattern "well 1", "well-1", "w-1"
    match = re.search(r'\b(?:well|w)[-_ ]*(\d{1,4})\b', s, re.IGNORECASE)
    if match:
        num = int(match.group(1))
        canonical = f"WELL-{num:04d}"
        exists = conn.execute("SELECT 1 FROM wells WHERE asset_id = ?", [canonical]).fetchone()
        if exists:
            return canonical

    # Standalone digits ONLY if entire string is digits e.g. "1", "121", "0082"
    if s.isdigit():
        num = int(s)
        canonical = f"WELL-{num:04d}"
        exists = conn.execute("SELECT 1 FROM wells WHERE asset_id = ?", [canonical]).fetchone()
        if exists:
            return canonical

    # Database lookup
    row = conn.execute("SELECT asset_id FROM wells WHERE LOWER(asset_id) = LOWER(?) OR LOWER(name) = LOWER(?)", [s, s]).fetchone()
    return row[0] if row else None


def resolve_area_name(input_str: Optional[str], conn: duckdb.DuckDBPyConnection) -> Optional[str]:
    """Resolves fuzzy area input to canonical area name (e.g. 'Northeast Block 8')."""
    if not input_str:
        return None
    s = str(input_str).strip().lower()

    if "sw 24" in s or "southwest 24" in s or ("southwest" in s and "24" in s) or "block 24" in s:
        return "Southwest Block 24"
    if "sw 23" in s or "southwest 23" in s or ("southwest" in s and "23" in s) or "block 23" in s:
        return "Southwest Block 23"
    if "ne 8" in s or "northeast 8" in s or ("northeast" in s and "8" in s) or "block 8" in s:
        return "Northeast Block 8"
    if "ne 7" in s or "northeast 7" in s or ("northeast" in s and "7" in s) or "block 7" in s:
        return "Northeast Block 7"

    # Search in DB
    areas = conn.execute("SELECT DISTINCT name FROM areas").fetchall()
    for (a_name,) in areas:
        if a_name.lower() in s or s in a_name.lower():
            return a_name

    return None


def determine_visual_type(
    user_query: str,
    default_type: Optional[str] = None,
    visual_hint: Optional[str] = None,
) -> Optional[str]:
    """Selects visual type based on explicit user prompt request or sensible default."""
    q = user_query.lower()
    if "status card" in q or "status_card" in q:
        return "status_card"
    if "line chart" in q or "line_chart" in q or "chart of" in q:
        return "line_chart"
    if "bar chart" in q or "bar_chart" in q:
        return "bar_chart"
    if "heatmap" in q:
        return "heatmap"
    if "map" in q:
        return "map"
    if "table" in q:
        return "table"
    if "no visual" in q or "short answer" in q:
        return None

    if visual_hint:
        return visual_hint
    return default_type


# Tool implementations

def tool_well_status(
    conn: duckdb.DuckDBPyConnection,
    well_id: str,
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Retrieves current operational and production status of a well."""
    wid = resolve_well_id(well_id, conn)
    if not wid:
        return ToolResult(tool_name="well_status", summary_text=f"Well '{well_id}' could not be identified.")

    # 1. Latest inspection
    insp = conn.execute("""
        SELECT
            inspection_id,
            inspected_date,
            inspector_name,
            method,
            wellhead_temp_c,
            ambient_temp_c,
            temp_delta_c,
            temp_delta_threshold,
            is_producing_oil,
            well_name,
            area_name,
            well_type,
            recorded_status,
            raw_wellhead_temp_c,
            corrected_by_author,
            corrected_from_value,
            correction_reason,
            inspection_notes
        FROM v_inspections_producing
        WHERE asset_id = ?
        ORDER BY inspected_at DESC
        LIMIT 1
    """, [wid]).fetchone()

    if not insp:
        return ToolResult(tool_name="well_status", summary_text=f"No inspection records found for {wid}.")

    (
        insp_id,
        insp_date,
        insp_name,
        method,
        wh_temp,
        amb_temp,
        delta,
        threshold,
        is_prod,
        w_name,
        area_name,
        well_type,
        rec_status,
        raw_wh_temp,
        corrected_by_author,
        corrected_from_val,
        correction_reason,
        insp_notes,
    ) = insp

    # 2. Context notes
    notes = conn.execute("""
        SELECT note_id, author_user_id, note_type, text, created_at
        FROM context_notes
        WHERE asset_id = ?
        ORDER BY created_at DESC
    """, [wid]).fetchall()

    note_citations = []
    badges = []
    shut_in_explanation = ""

    for n_id, auth_id, n_type, n_text, created in notes:
        # Resolve author name
        u_name = conn.execute("SELECT name FROM users WHERE user_id = ?", [auth_id]).fetchone()
        author_name = u_name[0] if u_name else auth_id
        note_citations.append({
            "id": n_id,
            "kind": "note",
            "label": f"Note by {author_name}",
            "detail": n_text,
        })
        if "shut in" in n_text.lower() or "shut-in" in n_text.lower():
            badges.append({"text": "Planned shut-in", "tone": "warning"})
            shut_in_explanation = f"Note {n_id} by {author_name}: {n_text}"

    # Also check shared_facts for planned downtime or shared notes
    try:
        s_facts = conn.execute("""
            SELECT fact_id, author_user_id, author_name, text, status, created_at
            FROM shared_facts
            WHERE target_id = ?
            ORDER BY created_at DESC
        """, [wid]).fetchall()
        for f_id, auth_id, auth_name, f_text, f_stat, f_created in s_facts:
            note_citations.append({
                "id": f_id,
                "kind": "note",
                "label": f"Shared note by {auth_name}",
                "detail": f_text,
            })
            if "shut in" in f_text.lower() or "shut-in" in f_text.lower() or "workover" in f_text.lower() or "downtime" in f_text.lower():
                badges.append({"text": "Planned workover/shut-in", "tone": "warning"})
                shut_in_explanation = f"Yes, planned downtime is scheduled according to {auth_name}: {f_text}."
    except Exception:
        pass

    citations = [
        {
            "id": insp_id,
            "kind": "inspection",
            "label": f"Inspection {insp_date}",
            "detail": f"Wellhead {wh_temp:.1f} °C, Air {amb_temp:.1f} °C, Delta {delta:.1f} °C (threshold {threshold:.1f} °C) by {insp_name} via {method}.",
        }
    ] + note_citations

    # 3. Flags
    flags = []
    if rec_status == "active" and not is_prod:
        flag_source_ids = [insp_id]
        if note_citations:
            flag_source_ids.append(note_citations[0]["id"])
        flags.append({
            "kind": "conflict",
            "text": f"The recorded status still says '{rec_status}', which is out of date.",
            "source_ids": flag_source_ids,
        })

    if corrected_by_author:
        flags.append({
            "kind": "correction_applied",
            "text": f"Value corrected by {corrected_by_author}: wellhead temperature was updated to {wh_temp:.1f} °C (original: {corrected_from_val:.1f} °C).",
            "source_ids": [insp_id],
        })
        if insp_notes and ("not moving" in insp_notes.lower() or "stopped" in insp_notes.lower()):
            flags.append({
                "kind": "conflict",
                "text": f"Inspection note '{insp_notes}' by {insp_name} disagrees with the temperature correction.",
                "source_ids": [insp_id],
            })

    # Summary
    prod_str = "producing oil" if is_prod else "not producing oil"
    summary_parts = [
        f"{wid} is {prod_str}.",
        f"Latest inspection {insp_id} was conducted on {insp_date.strftime('%d %b %Y')} by {method} by {insp_name}.",
    ]
    if corrected_by_author:
        summary_parts.append(
            f"The wellhead reading was corrected by {corrected_by_author} from {corrected_from_val:.1f} °C to {wh_temp:.1f} °C. "
            f"At {wh_temp:.1f} °C against {amb_temp:.1f} °C air (delta {delta:.1f} °C, above the {well_type} threshold of {threshold:.1f} °C), {wid} is producing oil."
        )
        if insp_notes and ("not moving" in insp_notes.lower() or "stopped" in insp_notes.lower()):
            summary_parts.append(
                f"However, inspector {insp_name} noted '{insp_notes}', which disagrees with the correction."
            )
    else:
        if delta < threshold:
            summary_parts.append(f"The wellhead was {delta:.1f} °C warmer than the air (wellhead {wh_temp:.1f} °C vs air {amb_temp:.1f} °C), below the {well_type} threshold of {threshold:.1f} °C.")
        else:
            summary_parts.append(f"The wellhead was {delta:.1f} °C warmer than the air (wellhead {wh_temp:.1f} °C vs air {amb_temp:.1f} °C), meeting the {well_type} threshold of {threshold:.1f} °C.")

    if shut_in_explanation:
        summary_parts.append(shut_in_explanation)
    for fl in flags:
        if fl["text"] not in " ".join(summary_parts):
            summary_parts.append(fl["text"])

    summary_text = " ".join(summary_parts)

    # Visual spec
    vis_type = determine_visual_type(user_query, default_type="status_card", visual_hint=visual_hint)
    visual = None
    if vis_type == "status_card":
        if not badges and is_prod:
            badges.append({"text": "Operating normally", "tone": "ok"})
        elif not badges and not is_prod:
            badges.append({"text": "Not producing", "tone": "critical"})

        visual = {
            "type": "status_card",
            "well_id": wid,
            "name": w_name or wid,
            "area": area_name,
            "well_type": well_type,
            "producing": is_prod,
            "headline": "Producing oil" if is_prod else "Not producing oil",
            "recorded_status": rec_status,
            "metrics": [
                {"label": "Wellhead above air", "value": round(delta, 1), "unit": "°C"}
            ],
            "badges": badges,
            "last_inspection": {
                "id": insp_id,
                "date": str(insp_date),
                "by": insp_name,
            },
        }

    return ToolResult(
        tool_name="well_status",
        summary_text=summary_text,
        rows=[{
            "well_id": wid,
            "is_producing": is_prod,
            "delta_c": round(delta, 1),
            "threshold_c": round(threshold, 1),
            "last_inspection_id": insp_id,
            "inspected_date": str(insp_date),
            "inspector": insp_name,
            "method": method,
            "recorded_status": rec_status,
        }],
        citations=citations,
        flags=flags,
        visual=visual,
    )


def tool_area_wells_not_producing(
    conn: duckdb.DuckDBPyConnection,
    area_name: str,
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Finds wells in an area that are not producing oil right now and explains reasons."""
    area = resolve_area_name(area_name, conn)

    # Query latest inspection for each well in the area
    rows = conn.execute("""
        WITH ranked AS (
            SELECT *,
                   ROW_NUMBER() OVER (PARTITION BY asset_id ORDER BY inspected_at DESC) as rn
            FROM v_inspections_producing
            WHERE area_name = ?
        )
        SELECT
            asset_id,
            well_type,
            inspected_date,
            inspection_id,
            ROUND(temp_delta_c, 1) as delta,
            recorded_status,
            inspection_notes
        FROM ranked
        WHERE rn = 1 AND is_producing_oil = false
        ORDER BY asset_id ASC
    """, [area]).fetchall()

    table_rows = []
    citations = []
    flags = []

    today_dt = datetime.combine(get_today(), datetime.max.time())

    for wid, wtype, idate, i_id, delta, rec_stat, inotes in rows:
        citations.append({
            "id": i_id,
            "kind": "inspection",
            "label": f"Inspection {i_id}",
            "detail": f"{wid} inspected on {idate}: delta {delta} °C, notes: '{inotes or ''}'",
        })

        # Check for open repairs as of today (completed_at is null or in future)
        open_repair = conn.execute("""
            SELECT maintenance_id, issue, action_taken, CAST(started_at AS DATE) as s_date
            FROM maintenance
            WHERE asset_id = ?
              AND started_at <= ?
              AND (completed_at IS NULL OR completed_at > ?)
            ORDER BY started_at DESC
            LIMIT 1
        """, [wid, today_dt, today_dt]).fetchone()

        # Check for recent active context notes (within last 30 days)
        recent_date = get_today() - timedelta(days=30)
        ctx_note = conn.execute("""
            SELECT note_id, text FROM context_notes
            WHERE asset_id = ?
              AND CAST(created_at AS DATE) >= ?
            ORDER BY created_at DESC LIMIT 1
        """, [wid, recent_date]).fetchone()

        reason = "No recorded reason."
        if open_repair:
            m_id, issue, action, s_date = open_repair
            citations.append({
                "id": m_id,
                "kind": "maintenance",
                "label": f"Repair {m_id}",
                "detail": f"{issue}, started {s_date.strftime('%d %b')}, still open",
            })
            reason = f"Repair {m_id}, {issue.lower()}, started {s_date.strftime('%d %b')}, still open"
        elif ctx_note:
            citations.append({
                "id": ctx_note[0],
                "kind": "note",
                "label": f"Note {ctx_note[0]}",
                "detail": ctx_note[1],
            })
            reason = ctx_note[1]
        else:
            if inotes and ("not moving" in inotes.lower() or "pump" in inotes.lower()):
                reason = f"No recorded reason. The inspector noted \"{inotes.strip()}\"."
            flags.append({
                "kind": "no_cause",
                "text": f"{wid} is not producing with no recorded reason.",
                "source_ids": [wid, i_id],
            })

        rec_stat_display = f"{rec_stat} (out of date)" if rec_stat == "active" else rec_stat
        table_rows.append({
            "well": wid,
            "delta": f"{delta} °C",
            "status": rec_stat_display,
            "reason": reason,
        })

    summary_text = f"There are {len(rows)} wells in {area} not producing oil right now: " + ", ".join([f"{r['well']} ({r['delta']})" for r in table_rows]) + "."
    try:
        corr_rows = conn.execute("""
            SELECT DISTINCT i.asset_id, c.author_name, c.new_value
            FROM corrections c
            JOIN inspections i ON c.target_record = i.inspection_id
            JOIN wells w ON i.asset_id = w.asset_id
            JOIN areas a ON w.area_id = a.area_id
            WHERE a.name = ? AND c.field_name = 'wellhead_temp_c'
        """, [area]).fetchall()
        for c_wid, c_auth, c_val in corr_rows:
            summary_text += f" {c_wid} is no longer listed because it is producing oil based on {c_auth}'s correction of the wellhead reading to {c_val:.1f} °C."
            flags.append({
                "kind": "correction_applied",
                "text": f"{c_wid} removed from non-producing list following {c_auth}'s temperature correction.",
                "source_ids": [c_wid],
            })
    except Exception:
        pass

    vis_type = determine_visual_type(user_query, default_type="table", visual_hint=visual_hint)
    visual = None
    if vis_type == "table":
        visual = {
            "type": "table",
            "title": f"Non-Producing Wells in {area}",
            "columns": [
                {"key": "well", "label": "Well"},
                {"key": "delta", "label": "Wellhead above air"},
                {"key": "status", "label": "Recorded status"},
                {"key": "reason", "label": "Reason"},
            ],
            "rows": table_rows,
        }

    return ToolResult(
        tool_name="area_wells_not_producing",
        summary_text=summary_text,
        rows=table_rows,
        citations=citations,
        flags=flags,
        visual=visual,
    )


def tool_well_timeseries(
    conn: duckdb.DuckDBPyConnection,
    well_id: str,
    weeks: int = 13,
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Retrieves weekly inspection time-series for a well."""
    wid = resolve_well_id(well_id, conn)
    if not wid:
        return ToolResult(tool_name="well_timeseries", summary_text=f"Well '{well_id}' could not be identified.")

    series = derived_well_timeseries(conn, wid, weeks=weeks)
    if not series:
        return ToolResult(tool_name="well_timeseries", summary_text=f"No time-series data found for {wid}.")

    non_prod = [s for s in series if not s["is_producing_oil"]]
    non_prod_dates = [s["date"].strftime("%d %b %Y") for s in non_prod]

    citations = [
        {
            "id": s["inspection_id"],
            "kind": "inspection",
            "label": f"Inspection {s['date']}",
            "detail": f"Wellhead {s['wellhead_temp_c']:.1f} °C, Air {s['ambient_temp_c']:.1f} °C, Delta {s['temp_delta_c']:.1f} °C",
        }
        for s in series
    ]

    summary_text = (
        f"{wid} has {len(series)} readings over the last {weeks} weeks ({series[0]['date'].strftime('%d %b')} to {series[-1]['date'].strftime('%d %b %Y')}). "
        f"It was not producing oil on {', '.join(non_prod_dates)}."
    )

    vis_type = determine_visual_type(user_query, default_type="line_chart", visual_hint=visual_hint)
    visual = None
    if vis_type == "line_chart":
        visual = {
            "type": "line_chart",
            "title": f"Temperature History - {wid}",
            "x": [str(s["date"]) for s in series],
            "x_label": "Date",
            "y_label": "°C",
            "series": [
                {"name": "Wellhead", "values": [round(s["wellhead_temp_c"], 1) for s in series]},
                {"name": "Air", "values": [round(s["ambient_temp_c"], 1) for s in series]},
            ],
            "markers": [
                {"x": str(s["date"]), "label": "Not producing"}
                for s in non_prod
            ],
        }

    return ToolResult(
        tool_name="well_timeseries",
        summary_text=summary_text,
        rows=[{"date": str(s["date"]), "wellhead_c": s["wellhead_temp_c"], "air_c": s["ambient_temp_c"], "producing": s["is_producing_oil"]} for s in series],
        citations=citations,
        visual=visual,
    )


def tool_spills_query(
    conn: duckdb.DuckDBPyConnection,
    target: str,
    window: str = "last 90 days",
    min_volume: float = 0.0,
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Queries oil spills with effective volume corrections and visual options."""
    vis_type = determine_visual_type(user_query, default_type="table", visual_hint=visual_hint)

    # Special case: fleet heatmap
    if vis_type == "heatmap" or "heatmap" in user_query.lower() or "by geographic area and month" in user_query.lower():
        m_yr = re.search(r'\b(20\d\d)\b', user_query)
        year_str = m_yr.group(1) if m_yr else str(get_today().year)

        areas = [
            "Southwest Block 23",
            "Southwest Block 24",
            "Northeast Block 7",
            "Northeast Block 8",
        ]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
        heatmap_values = []
        area_totals = {}

        for area in areas:
            area_row = []
            for m_idx in range(1, len(months) + 1):
                cnt = conn.execute("""
                    SELECT COUNT(*)
                    FROM v_effective_spills
                    WHERE area_name = ?
                      AND effective_spill_detected = true
                      AND strftime(inspected_date, '%Y') = ?
                      AND CAST(strftime(inspected_date, '%m') AS INT) = ?
                """, [area, year_str, m_idx]).fetchone()[0]
                area_row.append(cnt)
            heatmap_values.append(area_row)
            area_totals[area] = sum(area_row)

        top_spills = conn.execute("""
            SELECT inspection_id, asset_id, inspected_date, effective_volume_bbl
            FROM v_effective_spills
            WHERE effective_spill_detected = true
              AND strftime(inspected_date, '%Y') = ?
            ORDER BY inspected_date DESC
            LIMIT 10
        """, [year_str]).fetchall()
        citations = [
            {
                "id": r[0],
                "kind": "inspection",
                "label": f"Inspection {r[0]}",
                "detail": f"{r[1]} spill {r[3]:.1f} bbl on {r[2]}",
            }
            for r in top_spills
        ]

        totals_summary = ", ".join([f"{a} ({area_totals[a]} total)" for a in areas])
        summary_text = f"Heatmap of {year_str} spills by area: {totals_summary}."
        return ToolResult(
            tool_name="spills_query",
            summary_text=summary_text,
            citations=citations,
            visual={
                "type": "heatmap",
                "title": f"{year_str} Spills by Geographic Area and Month",
                "rows": areas,
                "cols": months,
                "values": heatmap_values,
                "unit": "spills",
            },
        )

    # General spills query
    wid = resolve_well_id(target, conn)
    canonical_target = wid if wid else resolve_area_name(target, conn)
    if not canonical_target:
        if str(target).lower() == "fleet":
            canonical_target = "fleet"
        else:
            return ToolResult(
                tool_name="spills_query",
                summary_text=f"Target '{target}' could not be resolved in the database.",
                citations=[],
                flags=[],
                visual=None,
            )

    spills = derived_spills_query(conn, target=canonical_target, window=window, min_volume=min_volume)
    rep_thresh = get_rule_threshold(conn, "spill_volume_reportable_threshold", "fleet") or 5.0

    is_reportable_query = ("report" in user_query.lower() and "regulator" in user_query.lower()) or "reportable" in user_query.lower()
    if is_reportable_query:
        spills = [s for s in spills if s.get("is_reportable") or s["effective_volume_bbl"] >= rep_thresh]

    citations = []
    flags = []

    for s in spills:
        citations.append({
            "id": s["inspection_id"],
            "kind": "inspection",
            "label": f"Inspection {s['inspected_date']}",
            "detail": f"{s['well_id']} spill {s['effective_volume_bbl']} bbl ({s['spill_class']})",
        })
        if s.get("correction_note_id"):
            citations.append({
                "id": s["correction_note_id"],
                "kind": "note",
                "label": f"Correction {s['correction_note_id']}",
                "detail": "Corrected raw detection",
            })
            flags.append({
                "kind": "correction_applied",
                "text": f"Raw detection corrected: {s['inspection_id']}",
                "source_ids": [s["correction_note_id"]],
            })
        if s.get("corrected_by_author"):
            flags.append({
                "kind": "correction_applied",
                "text": f"Spill volume corrected to {s['effective_volume_bbl']:.1f} bbl by {s['corrected_by_author']} (original AI estimate: {s.get('corrected_from_value', 4.5):.1f} bbl).",
                "source_ids": [s["inspection_id"]],
            })
        if s["effective_volume_bbl"] >= rep_thresh:
            reg_notice = conn.execute("""
                SELECT event_id FROM regulatory_events
                WHERE asset_id = ? AND related_inspection_id = ?
            """, [s["well_id"], s["inspection_id"]]).fetchone()
            if not reg_notice:
                flags.append({
                    "kind": "overdue",
                    "text": f"Written notice to regulator (SR-01) for {s['well_id']} is overdue.",
                    "source_ids": [s["inspection_id"]],
                })

    # Summary
    total_bbl = sum(s["effective_volume_bbl"] for s in spills)
    if is_reportable_query:
        well_names_str = ", ".join(sorted(set(s["well_id"] for s in spills))) or "no wells"
        corr_notes = []
        for s in spills:
            if s.get("corrected_by_author"):
                corr_notes.append(
                    f"{s['well_id']} had a spill corrected to {s['effective_volume_bbl']:.1f} bbl (above the {rep_thresh:.1f} bbl reportable threshold)."
                )
        corr_summary = " ".join(corr_notes)
        summary_text = (
            f"In {canonical_target} in the {window}, {well_names_str} needed a report to the regulator. "
            f"{corr_summary} "
            f"No written notice is on record, so it is flagged as overdue. No other spill in that period reached {rep_thresh:.1f} bbl."
        )
    else:
        summary_text = (
            f"{canonical_target} had {len(spills)} oil spills in the {window}, totaling {total_bbl:.1f} barrels."
        )

    visual = None
    if vis_type == "map":
        pins = []
        lats, lons = [], []
        for s in spills:
            lat = s.get("latitude") or 0.0
            lon = s.get("longitude") or 0.0
            if lat and lon:
                lats.append(lat)
                lons.append(lon)
                pins.append({
                    "label": s["well_id"],
                    "lat": round(lat, 5),
                    "lon": round(lon, 5),
                    "detail": f"{s['effective_volume_bbl']} bbl, {s['inspected_date'].strftime('%d %b %Y')}",
                    "tone": "critical" if s["effective_volume_bbl"] >= rep_thresh else "warning",
                })
        c_lat = sum(lats) / len(lats) if lats else 32.15
        c_lon = sum(lons) / len(lons) if lons else -102.16
        visual = {
            "type": "map",
            "title": f"Spills in {canonical_target} ({window})",
            "center": {"lat": round(c_lat, 4), "lon": round(c_lon, 4)},
            "pins": pins,
        }
    elif vis_type == "table":
        visual = {
            "type": "table",
            "title": f"Spills for {canonical_target} ({window})",
            "columns": [
                {"key": "well", "label": "Well"},
                {"key": "date", "label": "Date"},
                {"key": "bbl", "label": "Barrels"},
                {"key": "class", "label": "Spill Class"},
            ],
            "rows": [
                {
                    "well": s["well_id"],
                    "date": s["inspected_date"].strftime("%d %b %Y"),
                    "bbl": round(s["effective_volume_bbl"], 1),
                    "class": s["spill_class"],
                }
                for s in spills
            ],
        }

    return ToolResult(
        tool_name="spills_query",
        summary_text=summary_text,
        rows=spills,
        citations=citations,
        flags=flags,
        visual=visual,
    )


def tool_downtime_ranking(
    conn: duckdb.DuckDBPyConnection,
    target: str,
    window: str = "last 4 months",
    limit: int = 3,
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Computes downtime days for a single well or ranks top downtime wells in an area."""
    # Check if target is a single well
    wid = resolve_well_id(target, conn)
    use_doc_offset = ("4 month" in window.lower())
    start_date, end_date = get_date_window(window, use_doc_offset=use_doc_offset)

    if wid:
        non_prod_count, downtime_days = calculate_downtime_days(conn, wid, start_date, end_date)
        # Maintenance records explaining downtime
        m_rows = conn.execute("""
            SELECT maintenance_id, issue, action_taken, CAST(started_at AS DATE) as s_date
            FROM maintenance
            WHERE asset_id = ?
              AND CAST(started_at AS DATE) >= ?
              AND CAST(started_at AS DATE) <= ?
            ORDER BY started_at ASC
        """, [wid, start_date, end_date]).fetchall()

        citations = []
        for m_id, issue, action, s_date in m_rows:
            citations.append({
                "id": m_id,
                "kind": "maintenance",
                "label": f"Repair {m_id}",
                "detail": f"{issue} on {s_date.strftime('%d %b %Y')}",
            })

        summary_text = (
            f"{wid} was down for {downtime_days} days in {window}, from {non_prod_count} weekly inspections "
            f"where it was not producing oil."
        )

        # Check shared facts for planned downtime / workovers
        try:
            s_facts = conn.execute("""
                SELECT fact_id, author_name, text, status
                FROM shared_facts
                WHERE target_id = ?
                ORDER BY created_at DESC
            """, [wid]).fetchall()
            for f_id, auth_name, f_text, f_stat in s_facts:
                citations.append({
                    "id": f_id,
                    "kind": "note",
                    "label": f"Shared note by {auth_name}",
                    "detail": f_text,
                })
                if any(w in f_text.lower() for w in ["shut in", "shut-in", "workover", "downtime", "planned"]):
                    summary_text += f" Yes, planned downtime is scheduled according to {auth_name}: {f_text}."
        except Exception:
            pass

        vis_type = determine_visual_type(user_query, default_type=None, visual_hint=visual_hint)
        visual = None
        if vis_type == "table":
            visual = {
                "type": "table",
                "title": f"Downtime for {wid} ({window})",
                "columns": [{"key": "metric", "label": "Metric"}, {"key": "value", "label": "Value"}],
                "rows": [
                    {"metric": "Non-producing inspections", "value": non_prod_count},
                    {"metric": "Total downtime days", "value": downtime_days},
                ],
            }

        return ToolResult(
            tool_name="downtime_ranking",
            summary_text=summary_text,
            rows=[{"well_id": wid, "downtime_days": downtime_days, "non_prod_inspections": non_prod_count}],
            citations=citations,
            visual=visual,
        )

    # Area ranking
    area = resolve_area_name(target, conn)
    ranked = rank_downtime_wells_in_area(conn, area, start_date, end_date, limit=limit)

    summary_text = (
        f"Top downtime wells in {area} for {window}: " +
        ", ".join([f"{r['asset_id']}: {r['downtime_days']} days ({r['well_type']})" for r in ranked]) + "."
    )

    vis_type = determine_visual_type(user_query, default_type="bar_chart", visual_hint=visual_hint)
    visual = None
    if vis_type == "bar_chart":
        visual = {
            "type": "bar_chart",
            "title": f"Top Downtime Wells in {area} ({window})",
            "categories": [r["asset_id"] for r in ranked],
            "unit": "days",
            "series": [
                {"name": "Downtime", "values": [r["downtime_days"] for r in ranked]}
            ],
        }

    # Fetch non-producing inspection citations for top downtime wells
    citations = []
    top_asset_ids = [r["asset_id"] for r in ranked]
    if top_asset_ids:
        placeholders = ", ".join(["?"] * len(top_asset_ids))
        insp_rows = conn.execute(f"""
            SELECT inspection_id, asset_id, inspected_date
            FROM v_inspections_producing
            WHERE asset_id IN ({placeholders})
              AND inspected_date >= ?
              AND inspected_date <= ?
              AND is_producing_oil = false
            ORDER BY inspected_date DESC
            LIMIT 10
        """, top_asset_ids + [start_date, end_date]).fetchall()
        for i_id, a_id, i_dt in insp_rows:
            citations.append({
                "id": i_id,
                "kind": "inspection",
                "label": f"Inspection {i_id}",
                "detail": f"{a_id} not producing on {i_dt}",
            })

    return ToolResult(
        tool_name="downtime_ranking",
        summary_text=summary_text,
        rows=ranked,
        citations=citations,
        visual=visual,
    )


def tool_breaches_check(
    conn: duckdb.DuckDBPyConnection,
    well_id: str,
    window: str = "last 12 months",
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Checks regulatory and SOP breaches for a well."""
    wid = resolve_well_id(well_id, conn)
    if not wid:
        return ToolResult(tool_name="breaches_check", summary_text=f"Well '{well_id}' could not be identified.")

    res = derived_breaches_check(conn, wid, window=window)

    all_citations = []
    flags = []

    for b in res:
        for c_id in b["citation_ids"]:
            kind = "regulatory" if c_id.startswith("REG-") else ("inspection" if c_id.startswith("INS-") else "maintenance")
            all_citations.append({
                "id": c_id,
                "kind": kind,
                "label": f"Record {c_id}",
                "detail": b["detail"],
            })

    if res.open_fines_usd > 0:
        flags.append({
            "kind": "overdue",
            "text": f"USD {res.open_fines_usd:,.0f} in regulatory fines remain open.",
            "source_ids": [c["id"] for c in all_citations if c["id"].startswith("REG-")],
        })

    summary_parts = [
        f"{wid} has {len(res)} breaches in the {window}.",
        f"Open fines total USD {res.open_fines_usd:,.0f}."
    ]
    for b in res:
        summary_parts.append(f"{b['rule_id']}: {b['detail']}")

    summary_text = " ".join(summary_parts)

    vis_type = determine_visual_type(user_query, default_type="table", visual_hint=visual_hint)
    visual = None
    if vis_type == "table":
        visual = {
            "type": "table",
            "title": f"Breaches and Compliance Status - {wid}",
            "columns": [
                {"key": "rule", "label": "Rule"},
                {"key": "status", "label": "Status"},
                {"key": "detail", "label": "Details"},
            ],
            "rows": [
                {"rule": b["rule_id"], "status": b["status"], "detail": b["detail"]}
                for b in res
            ],
        }

    return ToolResult(
        tool_name="breaches_check",
        summary_text=summary_text,
        rows=res.breaches,
        citations=all_citations,
        flags=flags,
        visual=visual,
    )


def tool_uncontained_spills_query(
    conn: duckdb.DuckDBPyConnection,
    area_name: str,
    window: str = "last 90 days",
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Finds spills in an area that were not contained within the SOP time limit."""
    area = resolve_area_name(area_name, conn)
    uncontained = derived_uncontained_spills_query(conn, area, window=window)

    citations = []
    for s in uncontained:
        if s.get("maintenance_id"):
            citations.append({
                "id": s["maintenance_id"],
                "kind": "maintenance",
                "label": f"Report {s['maintenance_id']}",
                "detail": f"Contained after {s['containment_hours']} hours (limit {s.get('limit_hours', 4.0)} h)",
            })
        if s.get("inspection_id"):
            citations.append({
                "id": s["inspection_id"],
                "kind": "inspection",
                "label": f"Inspection {s['inspection_id']}",
                "detail": f"Detected spill {s['effective_volume_bbl']} bbl on {s['inspected_date']}",
            })

    summary_text = (
        f"In {area}, {len(uncontained)} spills in the {window} were not contained within the {get_rule_threshold(conn, 'spill_containment_time_limit') or 4.0:g}-hour SOP limit: " +
        ", ".join([f"{s['well_id']} ({s['containment_hours']} h, report {s['maintenance_id']})" for s in uncontained]) + "."
    )

    vis_type = determine_visual_type(user_query, default_type="table", visual_hint=visual_hint)
    visual = None
    if vis_type == "table":
        visual = {
            "type": "table",
            "title": f"Uncontained Spills in {area} ({window})",
            "columns": [
                {"key": "well", "label": "Well"},
                {"key": "date", "label": "Date"},
                {"key": "containment", "label": "Containment Time"},
                {"key": "limit", "label": "SOP Limit"},
                {"key": "report", "label": "Maintenance Report"},
            ],
            "rows": [
                {
                    "well": s["well_id"],
                    "date": s["inspected_date"].strftime("%d %b %Y"),
                    "containment": f"{s['containment_hours']} hours",
                    "limit": f"{s.get('limit_hours', 4.0):g} hours",
                    "report": s.get("maintenance_id", ""),
                }
                for s in uncontained
            ],
        }

    return ToolResult(
        tool_name="uncontained_spills_query",
        summary_text=summary_text,
        rows=uncontained,
        citations=citations,
        visual=visual,
    )


def tool_repairs_cost(
    conn: duckdb.DuckDBPyConnection,
    wells: Union[List[str], str],
    year: Optional[int] = None,
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Calculates repair costs for specified wells in a given year."""
    target_year = year if year is not None else get_today().year

    if isinstance(wells, str):
        well_list = [w.strip() for w in wells.split(",")]
    else:
        well_list = list(wells)

    resolved_wells = [resolve_well_id(w, conn) for w in well_list]
    resolved_wells = [w for w in resolved_wells if w]

    costs = derived_repairs_cost(conn, resolved_wells, year=target_year)

    summary_text = (
        f"Repair costs in {target_year}: " +
        ", ".join([f"{w}: USD {costs.get(w, 0.0):,.0f}" for w in resolved_wells]) + "."
    )

    vis_type = determine_visual_type(user_query, default_type="bar_chart", visual_hint=visual_hint)
    visual = None
    if vis_type == "bar_chart":
        visual = {
            "type": "bar_chart",
            "title": f"Repair Costs {target_year}",
            "categories": resolved_wells,
            "unit": "USD",
            "series": [{"name": "Cost", "values": [int(costs.get(w, 0.0)) for w in resolved_wells]}],
        }

    citations = []
    if resolved_wells:
        placeholders = ", ".join(["?"] * len(resolved_wells))
        m_rows = conn.execute(f"""
            SELECT maintenance_id, asset_id, issue, total_cost_usd
            FROM maintenance
            WHERE asset_id IN ({placeholders})
              AND strftime(started_at, '%Y') = ?
            ORDER BY started_at DESC
            LIMIT 10
        """, resolved_wells + [str(year)]).fetchall()
        for m_id, a_id, issue, cost in m_rows:
            citations.append({
                "id": m_id,
                "kind": "maintenance",
                "label": f"Repair {m_id}",
                "detail": f"{a_id} {issue} (USD {cost:,.0f})",
            })

    return ToolResult(
        tool_name="repairs_cost",
        summary_text=summary_text,
        rows=[{"well_id": w, "cost_usd": costs.get(w, 0.0)} for w in resolved_wells],
        citations=citations,
        visual=visual,
    )


def tool_rca_wells_query(
    conn: duckdb.DuckDBPyConnection,
    area_name: str,
    equipment_kind: str = "pump_jack",
    window: str = "last 12 months",
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Identifies wells in an area needing root-cause analysis based on repeat repairs."""
    area = resolve_area_name(area_name, conn)
    wells = derived_rca_wells_query(conn, area, equipment_kind=equipment_kind, window=window)

    summary_text = (
        f"Wells in {area} needing a root-cause analysis on their {equipment_kind} ({window}): " +
        ", ".join([f"{w['well_id']} ({w['repair_count']} repairs)" for w in wells]) + "."
    )

    # Check if a well-type rule override is active
    try:
        t350_ovr = conn.execute("""
            SELECT author, value
            FROM user_rule_overrides
            WHERE parameter = 'rca_repair_count_threshold' AND scope = 'T350'
            ORDER BY created_at DESC
            LIMIT 1
        """,).fetchone()
        if t350_ovr:
            ovr_author, ovr_val = t350_ovr
            summary_text += f" Per {ovr_author}'s rule, not the manual, T350 wells require root-cause analysis after {int(ovr_val)} repairs."
    except Exception:
        pass

    citations = []
    for w in wells:
        for m_id in w["citation_ids"]:
            citations.append({
                "id": m_id,
                "kind": "maintenance",
                "label": f"Repair {m_id}",
                "detail": f"Corrective repair on {equipment_kind} for {w['well_id']}",
            })

    vis_type = determine_visual_type(user_query, default_type="table", visual_hint=visual_hint)
    visual = None
    if vis_type == "table":
        visual = {
            "type": "table",
            "title": f"RCA Required: {equipment_kind.replace('_', ' ').title()} in {area}",
            "columns": [
                {"key": "well", "label": "Well"},
                {"key": "type", "label": "Well Type"},
                {"key": "repairs", "label": "Repair Count"},
                {"key": "threshold", "label": "Threshold"},
            ],
            "rows": [
                {
                    "well": w["well_id"],
                    "type": w["well_type"],
                    "repairs": w["repair_count"],
                    "threshold": int(w["threshold"]),
                }
                for w in wells
            ],
        }

    return ToolResult(
        tool_name="rca_wells_query",
        summary_text=summary_text,
        rows=wells,
        citations=citations,
        visual=visual,
    )


def tool_get_well_context(
    conn: duckdb.DuckDBPyConnection,
    well_id: str,
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Retrieves human context notes, corrections, and comments for a well."""
    wid = resolve_well_id(well_id, conn)
    if not wid:
        return ToolResult(tool_name="get_well_context", summary_text=f"Well '{well_id}' could not be identified.")

    notes = conn.execute("""
        SELECT note_id, author_user_id, note_type, text, created_at
        FROM context_notes
        WHERE asset_id = ?
        ORDER BY created_at DESC
    """, [wid]).fetchall()

    citations = []
    rows = []
    for n_id, auth_id, n_type, n_text, created in notes:
        u_name = conn.execute("SELECT name FROM users WHERE user_id = ?", [auth_id]).fetchone()
        author_name = u_name[0] if u_name else auth_id
        citations.append({
            "id": n_id,
            "kind": "note",
            "label": f"Note {n_id}",
            "detail": f"{author_name}: {n_text}",
        })
        rows.append({
            "note_id": n_id,
            "author": author_name,
            "type": n_type,
            "text": n_text,
            "date": str(created),
        })

    # Also check shared_facts for well
    try:
        s_facts = conn.execute("""
            SELECT fact_id, author_user_id, author_name, text, status, created_at
            FROM shared_facts
            WHERE target_id = ?
            ORDER BY created_at DESC
        """, [wid]).fetchall()
        for f_id, auth_id, auth_name, f_text, f_stat, f_created in s_facts:
            citations.append({
                "id": f_id,
                "kind": "note",
                "label": f"Shared note by {auth_name}",
                "detail": f_text,
            })
            rows.append({
                "note_id": f_id,
                "author": auth_name,
                "type": "shared_fact",
                "text": f_text,
                "date": str(f_created),
            })
    except Exception:
        pass

    summary_text = f"Found {len(rows)} context notes and shared facts for {wid}."
    if rows:
        summary_text += " " + " ".join([f"[{r['author']}]: {r['text']}" for r in rows[:3]])
    return ToolResult(
        tool_name="get_well_context",
        summary_text=summary_text,
        rows=rows,
        citations=citations,
    )


def tool_search_documents(
    conn: duckdb.DuckDBPyConnection,
    query: str,
    user_query: str = "",
    visual_hint: Optional[str] = None,
) -> ToolResult:
    """Searches manuals, SOPs, rules, and reports for keyword matches."""
    q_like = f"%{query.strip()}%"
    rules = conn.execute("""
        SELECT rule_id, parameter, value, unit, source_file, section, description
        FROM rules
        WHERE parameter ILIKE ? OR description ILIKE ? OR section ILIKE ?
        LIMIT 5
    """, [q_like, q_like, q_like]).fetchall()

    citations = []
    rows = []
    for r_id, param, val, unit, src, sec, desc in rules:
        citations.append({
            "id": r_id,
            "kind": "document",
            "label": f"{sec} ({src})",
            "detail": desc or f"{param} = {val} {unit or ''}",
        })
        rows.append({
            "rule_id": r_id,
            "parameter": param,
            "value": f"{val} {unit or ''}".strip(),
            "source": f"{src} § {sec}",
        })

    summary_text = f"Found {len(rules)} document sections matching '{query}'."
    return ToolResult(
        tool_name="search_documents",
        summary_text=summary_text,
        rows=rows,
        citations=citations,
    )
