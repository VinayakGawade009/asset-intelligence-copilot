"""Date window helpers for period-based analytical queries."""
from datetime import date, datetime, timedelta
from typing import Tuple, Optional
import calendar
import re

from backend.app.config import TODAY

def get_today() -> date:
    """Returns configured TODAY date."""
    if isinstance(TODAY, str):
        try:
            return datetime.strptime(TODAY, "%Y-%m-%d").date()
        except ValueError:
            pass
    elif isinstance(TODAY, (datetime, date)):
        return TODAY if isinstance(TODAY, date) else TODAY.date()
    return date.today()

def _subtract_months(dt: date, months: int) -> date:
    """Subtracts N calendar months from a date."""
    year = dt.year
    month = dt.month - months
    while month < 1:
        month += 12
        year -= 1
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
    """
    if today is None:
        today = get_today()

    p = period.strip().lower()

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
    
    # Dynamic 4-digit year matching
    m = re.search(r"\b(19\d\d|20\d\d)\b", p)
    if m:
        yr = int(m.group(1))
        if yr == today.year:
            return (date(yr, 1, 1), today)
        else:
            return (date(yr, 1, 1), date(yr, 12, 31))

    # Default fallback to 1 year window ending today
    return (_subtract_years(today, 1), today)
