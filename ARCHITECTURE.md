# Asset Intelligence Copilot — Architecture

*Last updated: 2026-10-17*

## 1. Overview
The **Asset Intelligence Copilot** is an agentic AI assistant designed for oil field operators, engineers, and HSE officers. It combines high-performance analytical storage (DuckDB) with agentic orchestration using Google GenAI (Gemma 4 / Gemini models) and a generative UI (React + Vite) to provide grounded answers with explicit evidence citations.

---

## 2. System Architecture

```
┌────────────────────────────────────────────────────────┐
│               Frontend (React + Vite)                  │
│  - User Switcher (Private Session & RBAC Scope)        │
│  - Generative UI: StatusCard, Table, Line/Bar, Map... │
└───────────────────────────▲────────────────────────────┘
                            │ HTTP / JSON
┌───────────────────────────▼────────────────────────────┐
│               Backend (FastAPI)                        │
│  - Orchestrator (Google GenAI SDK)                     │
│  - Deterministic Typed Tools (No free-form SQL)        │
│  - Rules Engine (Reads rules table from DuckDB)        │
│  - Dual-Level Memory (Private User vs Shared Fleet)    │
└───────────────────────────▲────────────────────────────┘
                            │ SQL Queries / Vector / Text
┌───────────────────────────▼────────────────────────────┐
│               Storage Layer (DuckDB)                   │
│  - Analytical Tables: wells, inspections, maintenance  │
│  - Unstructured Data: maintenance_reports (raw MD)    │
│  - Compliance & Context: regulatory_events, notes      │
│  - Dynamic Rule Book: rules table                      │
└────────────────────────────────────────────────────────┘
```

---

## 3. Storage Layer (DuckDB)

### 3.1 Tables
- **`areas`**: Geographic blocks (`SW-23`, `NE-07`, etc.), team assignments, center lat/lon.
- **`teams`**: Field operational teams and team leads.
- **`users`**: Copilot users with roles (`production_supervisor`, `field_operator`, `field_inspector`, `maintenance_lead`, `maintenance_technician`, `hse_officer`).
- **`wells`**: Oil well metadata, installed date, well type (`T200`, `T350`), ownership, location, and cached status.
- **`equipment`**: Individual components attached to each well (`wellhead`, `pump_jack`, `rod_string`, `downhole_pump`, `flowline`, `separator`).
- **`inspections`**: ~39,600 weekly inspections with thermal readings (`wellhead_temp_c`, `ambient_temp_c`), spill detections, pad area %, estimated volume, and notes.
- **`maintenance`**: ~5,700 scheduled and corrective maintenance jobs, costs, technician info, and pointers to free-text reports (`report_file`).
- **`maintenance_reports`**: ~1,500 full raw markdown reports for corrective maintenance, capturing containment times and compliance checks.
- **`regulatory_events`**: 90 agency events (spill reports, notices of violation, site inspections) with fines, response times, and open/closed status.
- **`context_notes`**: ~140 human context notes, operator feedback, and raw data corrections with validity date ranges.
- **`rules`**: Operating rules, thermal thresholds, and SOP deadlines dynamically extracted from manuals and SOPs, extensible via user feedback at runtime.

---

## 4. Key Architectural Decisions

1. **Configurable Anchor Date ("Today")**:
   - Anchored to **17 Oct 2026** (configurable via `TODAY` environment variable in `config.py`).
   - Relative windows (`last 4 months`, `last 90 days`, `last 12 months`) are calculated backward from `TODAY`.
2. **Deterministic Typed Tools (No Free-Form SQL for Small Models)**:
   - Smaller runtime models (such as Gemma 4) will **not** write free-form SQL. Instead, the copilot calls deterministic, strictly typed tools (`well_status`, `downtime_ranking`, `spills_query`, `repairs_query`, `breaches_check`, `search_documents`, etc.) with validated parameters.
3. **Dynamic Rule Engine**:
   - Thresholds (e.g. 15 °C delta for T200, 20 °C delta for T350, 4-hour containment limit, 24-hour reporting limit, 3 corrective repairs for RCA) are stored in the DuckDB `rules` table, allowing type-wide runtime overrides from user feedback (e.g., Q14).
4. **Multi-Root Ingestion**:
   - The ingestion pipeline supports one or more data roots (e.g. `--data sample-data --data test-data`), allowing seamless loading of new test datasets alongside existing data.

---

## 5. Directory Structure

```
flytbase-ahc-swe-asset-intelligence-dataset/
├── backend/
│   ├── app/
│   │   ├── config.py              # Configuration & env variables (TODAY, DATA_ROOTS, etc.)
│   │   ├── db/
│   │   │   ├── connection.py      # DuckDB connection manager
│   │   │   ├── schema.py          # Table DDL definitions
│   │   │   └── ingest.py          # Multi-root data loader & verification
│   │   ├── agent/                 # LLM Orchestrator & typed tools (Stage 2)
│   │   └── models/                # Pydantic schemas & visual component definitions
│   ├── eval/                      # Evaluation suite for 03-evaluation-queries.md
│   ├── tests/                     # Unit and integration tests
│   └── data/                      # Local DuckDB database file
├── frontend/                      # React + Vite Generative UI
├── sample-data/                   # Fleet manuals, SOPs, and asset files
├── ARCHITECTURE.md                # System design & living documentation
└── requirements.txt               # Python package dependencies
```
