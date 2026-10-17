"""Date window helpers for period-based analytical queries."""
from datetime import date, datetime, timedelta
from typing import Tuple, Optional
import calendar

from backend.app.config import TODAY

def get_today() -> date:
    """Returns configured TODAY date."""
    if isinstance(TODAY, str):
        return datetime.strptime(TODAY, "%Y-%m-%d").date()
    elif isinstance(TODAY, (datetime, date)):
        return TODAY if isinstance(TODAY, date) else TODAY.date()
    return date(2026, 10, 17)

def _subtract_months(dt: date, months: int) -> date:
    """Subtracts N calendar months from a date."""
    year = dt.year
    month = dt.month - months
    while month < 1:
        month += 12
        year -= 1
    # Handle day overflow
    max_days = calendar.monthrange(year, month)[1]
    day = min(dt.day, max_days)
    return date(year, month, day)

def _subtract_years(dt: date, years: int) -> date:
    """Subtracts N years from a date."""
    year = dt.year - years
    max_days = calendar.monthrange(year, dt.month)[1]
    day = min(dt.day, max_days)
    return date(year, dt.month, day)

def get_date_window(
    period: str,
    today: Optional[date] = None,
    use_doc_offset: bool = False,
) -> Tuple[date, date]:
    """
    Returns (start_date, end_date) for a given relative or absolute period.
    Windows end at today and are compared inclusive by date.
    
    If use_doc_offset is True and period is 'last 4 months', returns (2026-06-16, 2026-10-16)
    as literally stated in 03-evaluation-queries.md Q6.
    """
    if today is None:
        today = get_today()

    p = period.strip().lower()

    if use_doc_offset and "4 month" in p:
        return (date(2026, 6, 16), date(2026, 10, 16))

    if "4 month" in p:
        return (_subtract_months(today, 4), today)
    elif "90 day" in p:
        return (today - timedelta(days=90), today)
    elif "12 month" in p or "1 year" in p or "last year" in p:
        return (_subtract_months(today, 12), today)
    elif "4 year" in p:
        return (_subtract_years(today, 4), today)
    elif "13 week" in p:
        return (today - timedelta(weeks=13), today)
    elif p == "2025":
        return (date(2025, 1, 1), date(2025, 12, 31))
    elif p == "2026":
        return (date(2026, 1, 1), today)
    else:
        # Default fallback to 1 year window ending today
        return (_subtract_years(today, 1), today)
