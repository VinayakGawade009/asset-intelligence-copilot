SCHEMA_SQL = """
-- Fleet geographic areas
CREATE TABLE IF NOT EXISTS areas (
    area_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    team_id VARCHAR,
    center_lat DOUBLE,
    center_lon DOUBLE
);

-- Teams operating the fields
CREATE TABLE IF NOT EXISTS teams (
    team_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    lead_user_id VARCHAR
);

-- People / Copilot users
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    role VARCHAR,
    team_id VARCHAR
);

-- Oil wells (assets)
CREATE TABLE IF NOT EXISTS wells (
    asset_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    asset_category VARCHAR,
    well_type VARCHAR,
    area_id VARCHAR,
    team_id VARCHAR,
    in_charge_user_id VARCHAR,
    lat DOUBLE,
    lon DOUBLE,
    installed_on DATE,
    last_inspection_id VARCHAR,
    last_inspected_at TIMESTAMP,
    last_inspector_user_id VARCHAR,
    recorded_status VARCHAR
);

-- Equipment attached to wells
CREATE TABLE IF NOT EXISTS equipment (
    equipment_id VARCHAR PRIMARY KEY,
    asset_id VARCHAR,
    kind VARCHAR,
    model VARCHAR
);

-- Weekly drone / manual inspections
CREATE TABLE IF NOT EXISTS inspections (
    inspection_id VARCHAR PRIMARY KEY,
    asset_id VARCHAR,
    inspected_at TIMESTAMP,
    inspector_user_id VARCHAR,
    method VARCHAR,
    ambient_temp_c DOUBLE,
    wellhead_temp_c DOUBLE,
    spill_detected BOOLEAN,
    spill_area_pct DOUBLE,
    spill_est_volume_bbl DOUBLE,
    evidence_images VARCHAR,
    notes VARCHAR
);

-- Scheduled & corrective maintenance jobs
CREATE TABLE IF NOT EXISTS maintenance (
    maintenance_id VARCHAR PRIMARY KEY,
    asset_id VARCHAR,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    maintenance_type VARCHAR,
    equipment_kind VARCHAR,
    issue VARCHAR,
    action_taken VARCHAR,
    technician_user_id VARCHAR,
    contractor VARCHAR,
    downtime_hours DOUBLE,
    labor_cost_usd DOUBLE,
    parts_cost_usd DOUBLE,
    total_cost_usd DOUBLE,
    triggered_by_inspection_id VARCHAR,
    report_file VARCHAR
);

-- Raw markdown reports for corrective maintenance jobs
CREATE TABLE IF NOT EXISTS maintenance_reports (
    maintenance_id VARCHAR PRIMARY KEY,
    asset_id VARCHAR,
    report_path VARCHAR,
    raw_markdown VARCHAR
);

-- External regulatory notices, spill reports, and inspections
CREATE TABLE IF NOT EXISTS regulatory_events (
    event_id VARCHAR PRIMARY KEY,
    asset_id VARCHAR,
    date DATE,
    agency VARCHAR,
    event_type VARCHAR,
    protocol_id VARCHAR,
    related_inspection_id VARCHAR,
    hours_to_report DOUBLE,
    detail VARCHAR,
    fine_usd DOUBLE,
    status VARCHAR
);

-- Human context notes, feedback, and raw data corrections
CREATE TABLE IF NOT EXISTS context_notes (
    note_id VARCHAR PRIMARY KEY,
    asset_id VARCHAR,
    created_at TIMESTAMP,
    author_user_id VARCHAR,
    note_type VARCHAR,
    inspection_id VARCHAR,
    text VARCHAR,
    valid_from DATE,
    valid_to DATE
);

-- Operating rules and thresholds extracted from manuals & SOPs
CREATE TABLE IF NOT EXISTS rules (
    rule_id VARCHAR PRIMARY KEY,
    scope VARCHAR,
    parameter VARCHAR,
    value DOUBLE,
    unit VARCHAR,
    description VARCHAR,
    source_file VARCHAR,
    section VARCHAR,
    extracted_by VARCHAR,
    overridden_by_user VARCHAR,
    inherits_from VARCHAR
);

-- LLM call audit and observability log
CREATE TABLE IF NOT EXISTS llm_calls (
    call_id VARCHAR PRIMARY KEY,
    role VARCHAR,
    model VARCHAR,
    prompt_hash VARCHAR,
    prompt_preview VARCHAR,
    latency_ms DOUBLE,
    input_tokens INT,
    output_tokens INT,
    created_at TIMESTAMP,
    cached BOOLEAN
);

-- Maintenance report facts extracted by Gemma
CREATE TABLE IF NOT EXISTS maintenance_report_facts (
    maintenance_id VARCHAR PRIMARY KEY,
    containment_hours DOUBLE,
    root_cause VARCHAR,
    action_required BOOLEAN,
    stated_spill_class VARCHAR,
    reporting_duty_listed BOOLEAN,
    evidence_quote VARCHAR,
    source_file VARCHAR,
    extracted_by VARCHAR
);

-- User runtime rule overrides taking priority at specific scope
CREATE TABLE IF NOT EXISTS user_rule_overrides (
    override_id VARCHAR PRIMARY KEY,
    parameter VARCHAR,
    scope VARCHAR,
    value DOUBLE,
    author VARCHAR,
    reason VARCHAR,
    created_at TIMESTAMP
);
"""

def init_db(conn):
    """Initializes the database schema."""
    conn.execute(SCHEMA_SQL)

