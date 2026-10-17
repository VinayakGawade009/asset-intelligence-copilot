from pathlib import Path
import duckdb
from backend.app.config import DUCKDB_PATH

def get_connection(read_only: bool = False) -> duckdb.DuckDBPyConnection:
    """Returns a DuckDB connection. Ensures the parent directory exists."""
    DUCKDB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(DUCKDB_PATH), read_only=read_only)
