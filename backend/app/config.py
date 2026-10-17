import os
from pathlib import Path
from dotenv import load_dotenv

# Project root is the parent of backend/
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# Ground truth anchor date: 17 Oct 2026 (configurable via TODAY env var)
TODAY = os.getenv("TODAY", "2026-10-17")

# Database path
DEFAULT_DB_PATH = PROJECT_ROOT / "backend" / "data" / "copilot.duckdb"
DUCKDB_PATH = Path(os.getenv("DUCKDB_PATH", str(DEFAULT_DB_PATH)))

# Data roots (can contain multiple folders e.g. sample-data, test-data)
raw_data_roots = os.getenv("DATA_ROOTS", "sample-data")
DATA_ROOTS = [PROJECT_ROOT / p.strip() for p in raw_data_roots.split(",") if p.strip()]

# Model names and API keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
GEMMA_MODEL_FAST = os.getenv("GEMMA_MODEL_FAST", "gemma-4-26b-a4b-it")
GEMMA_MODEL_STRONG = os.getenv("GEMMA_MODEL_STRONG", "gemma-4-31b-it")
