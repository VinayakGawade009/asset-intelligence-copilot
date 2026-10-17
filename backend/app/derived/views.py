"""Derived analytics layer for DuckDB.
Driven strictly by the rules table with no thresholds or magic numbers in code.
"""
from typing import Optional, List, Dict, Any, Tuple
from datetime import date
import duckdb

def create_derived_views(conn: duckdb.DuckDBPyConnection):
    """
    Creates or replaces SQL views in DuckDB for derived intelligence.
    All thresholds are joined dynamically from the rules table.
    """

    # 1. Well rules view: resolves operational rules per well, applying inheritance if needed
    conn.execute("""
    CREATE OR REPLACE VIEW v_well_rules AS
    WITH delta_by_scope AS (
        SELECT scope, MAX(value) as delta_val
        FROM rules
        WHERE LOWER(parameter) LIKE '%producing%temp%delta%'
          AND value IS NOT NULL
        GROUP BY scope
    ),
    inheritance_by_scope AS (
        SELECT scope, MAX(inherits_from) as parent_scope
        FROM rules
        WHERE inherits_from IS NOT NULL
        GROUP BY scope
    )
    SELECT
        w.asset_id,
        w.well_type,
        COALESCE(
            d_direct.delta_val,
            d_parent.delta_val,
            d_fleet.delta_val
        ) as producing_temp_delta
    FROM wells w
    LEFT JOIN delta_by_scope d_direct ON w.well_type = d_direct.scope
    LEFT JOIN inheritance_by_scope inh ON w.well_type = inh.scope
    LEFT JOIN delta_by_scope d_parent ON inh.parent_scope = d_parent.scope
    LEFT JOIN delta_by_scope d_fleet ON d_fleet.scope = 'fleet';
    """)

    # 2. Inspections producing view: computes delta and production status against well-type rule
    conn.execute("""
    CREATE OR REPLACE VIEW v_inspections_producing AS
    SELECT
        i.inspection_id,
        i.asset_id,
        w.well_type,
        w.name as well_name,
        w.area_id,
        a.name as area_name,
        w.in_charge_user_id,
        w.recorded_status,
        i.inspected_at,
        CAST(i.inspected_at AS DATE) as inspected_date,
        i.inspector_user_id,
        u.name as inspector_name,
        i.method,
        i.wellhead_temp_c as raw_wellhead_temp_c,
        COALESCE(corr.new_value, i.wellhead_temp_c) as wellhead_temp_c,
        corr.author_name as corrected_by_author,
        corr.original_value as corrected_from_value,
        corr.reason as correction_reason,
        i.ambient_temp_c,
        (COALESCE(corr.new_value, i.wellhead_temp_c) - i.ambient_temp_c) as temp_delta_c,
        wr.producing_temp_delta as temp_delta_threshold,
        CASE
            WHEN COALESCE(corr.new_value, i.wellhead_temp_c) IS NULL OR i.ambient_temp_c IS NULL THEN false
            WHEN (COALESCE(corr.new_value, i.wellhead_temp_c) - i.ambient_temp_c) >= wr.producing_temp_delta THEN true
            ELSE false
        END as is_producing_oil,
        i.notes as inspection_notes
    FROM inspections i
    JOIN wells w ON i.asset_id = w.asset_id
    JOIN areas a ON w.area_id = a.area_id
    LEFT JOIN users u ON i.inspector_user_id = u.user_id
    JOIN v_well_rules wr ON w.asset_id = wr.asset_id
    LEFT JOIN corrections corr
        ON corr.target_record = i.inspection_id
        AND corr.field_name = 'wellhead_temp_c';
    """)

    # 3. Effective spill detection and classification view:
    # Overrides raw detections where human correction note exists with inspection_id
    conn.execute("""
    CREATE OR REPLACE VIEW v_spill_rules AS
    SELECT
        MAX(CASE WHEN LOWER(parameter) LIKE '%minor_max%' AND unit = 'bbl' THEN value END) as minor_max,
        MAX(CASE WHEN LOWER(parameter) LIKE '%moderate_min%' AND unit = 'bbl' THEN value END) as moderate_min,
        MAX(CASE WHEN LOWER(parameter) LIKE '%moderate_max%' AND unit = 'bbl' THEN value END) as moderate_max,
        MAX(CASE WHEN LOWER(parameter) LIKE '%reportable%' AND unit = 'bbl' AND LOWER(parameter) NOT LIKE '%notice%' THEN value END) as reportable_threshold,
        MAX(CASE WHEN LOWER(parameter) LIKE '%major%' AND unit = 'bbl' AND LOWER(parameter) NOT LIKE '%notice%' THEN value END) as major_threshold
    FROM rules
    WHERE scope = 'fleet';
    """)

    conn.execute("""
    CREATE OR REPLACE VIEW v_effective_spills AS
    SELECT
        i.inspection_id,
        i.asset_id,
        w.name as well_name,
        w.well_type,
        w.area_id,
        a.name as area_name,
        i.inspected_at,
        CAST(i.inspected_at AS DATE) as inspected_date,
        i.inspector_user_id,
        i.method,
        i.spill_detected as raw_spill_detected,
        i.spill_est_volume_bbl as raw_volume_bbl,
        i.spill_area_pct,
        cn.note_id as correction_note_id,
        cn.text as correction_text,
        corr.author_name as corrected_by_author,
        corr.original_value as corrected_from_value,
        corr.reason as correction_reason,
        CASE
            WHEN cn.note_id IS NOT NULL THEN false
            ELSE i.spill_detected
        END as effective_spill_detected,
        CASE
            WHEN cn.note_id IS NOT NULL OR NOT i.spill_detected THEN 0.0
            ELSE COALESCE(corr.new_value, i.spill_est_volume_bbl, 0.0)
        END as effective_volume_bbl,
        CASE
            WHEN cn.note_id IS NOT NULL OR NOT i.spill_detected THEN 'none'
            WHEN COALESCE(corr.new_value, i.spill_est_volume_bbl, 0.0) >= sr.major_threshold THEN 'major'
            WHEN COALESCE(corr.new_value, i.spill_est_volume_bbl, 0.0) >= sr.reportable_threshold THEN 'reportable'
            WHEN COALESCE(corr.new_value, i.spill_est_volume_bbl, 0.0) >= sr.moderate_min THEN 'moderate'
            WHEN COALESCE(corr.new_value, i.spill_est_volume_bbl, 0.0) < sr.minor_max THEN 'minor'
            ELSE 'minor'
        END as spill_class,
        CASE
            WHEN cn.note_id IS NOT NULL OR NOT i.spill_detected THEN false
            WHEN COALESCE(corr.new_value, i.spill_est_volume_bbl, 0.0) >= sr.reportable_threshold THEN true
            ELSE false
        END as is_reportable
    FROM inspections i
    JOIN wells w ON i.asset_id = w.asset_id
    JOIN areas a ON w.area_id = a.area_id
    LEFT JOIN context_notes cn
        ON i.inspection_id = cn.inspection_id
        AND cn.note_type = 'correction'
    LEFT JOIN corrections corr
        ON corr.target_record = i.inspection_id
        AND corr.field_name = 'spill_est_volume_bbl'
    CROSS JOIN v_spill_rules sr;
    """)

    # 4. Maintenance / repairs view with period assignment by started_at
    conn.execute("""
    CREATE OR REPLACE VIEW v_repairs AS
    SELECT
        m.maintenance_id,
        m.asset_id,
        w.name as well_name,
        w.well_type,
        w.area_id,
        a.name as area_name,
        m.started_at,
        CAST(m.started_at AS DATE) as started_date,
        m.completed_at,
        CAST(m.completed_at AS DATE) as completed_date,
        m.maintenance_type,
        m.equipment_kind,
        m.issue,
        m.action_taken,
        m.technician_user_id,
        u.name as technician_name,
        m.contractor,
        m.labor_cost_usd,
        m.parts_cost_usd,
        m.total_cost_usd,
        m.triggered_by_inspection_id,
        m.report_file,
        CASE WHEN m.completed_at IS NULL THEN true ELSE false END as is_open
    FROM maintenance m
    JOIN wells w ON m.asset_id = w.asset_id
    JOIN areas a ON w.area_id = a.area_id
    LEFT JOIN users u ON m.technician_user_id = u.user_id;
    """)

def get_days_per_inspection(conn: duckdb.DuckDBPyConnection) -> float:
    """Retrieves standard days represented per inspection from rules, defaulting to 7.0."""
    row = conn.execute("""
        SELECT value FROM rules
        WHERE LOWER(parameter) = 'days_per_inspection' AND value IS NOT NULL
        LIMIT 1
    """).fetchone()
    return float(row[0]) if row and row[0] is not None else 7.0

def calculate_downtime_days(
    conn: duckdb.DuckDBPyConnection,
    asset_id: str,
    start_date: date,
    end_date: date,
) -> Tuple[int, int]:
    """
    Computes downtime days in a window: 7 days per non-producing inspection.
    Missed inspections add nothing. Never uses maintenance.downtime_hours.
    Returns (non_producing_inspection_count, downtime_days).
    """
    days_factor = get_days_per_inspection(conn)
    query = """
    SELECT COUNT(*)
    FROM v_inspections_producing
    WHERE asset_id = ?
      AND inspected_date >= ?
      AND inspected_date <= ?
      AND is_producing_oil = false
    """
    count = conn.execute(query, [asset_id, start_date, end_date]).fetchone()[0]
    return count, int(count * days_factor)

def rank_downtime_wells_in_area(
    conn: duckdb.DuckDBPyConnection,
    area_name: str,
    start_date: date,
    end_date: date,
    limit: int = 3,
) -> List[Dict[str, Any]]:
    """
    Ranks wells in a given geographic area by total downtime days in the date window.
    """
    days_factor = get_days_per_inspection(conn)
    query = f"""
    SELECT
        asset_id,
        well_type,
        COUNT(*) as non_prod_inspections,
        CAST(COUNT(*) * {days_factor} AS INT) as downtime_days
    FROM v_inspections_producing
    WHERE area_name = ?
      AND inspected_date >= ?
      AND inspected_date <= ?
      AND is_producing_oil = false
    GROUP BY asset_id, well_type
    ORDER BY downtime_days DESC, asset_id ASC
    LIMIT ?
    """
    rows = conn.execute(query, [area_name, start_date, end_date, limit]).fetchall()
    return [
        {
            "asset_id": r[0],
            "well_type": r[1],
            "non_prod_inspections": r[2],
            "downtime_days": r[3],
        }
        for r in rows
    ]
