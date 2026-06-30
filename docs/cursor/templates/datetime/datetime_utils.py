"""Template portável — copie para core/datetime_utils.py e ajuste o import de settings."""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from core.config import settings

APP_TIMEZONE = ZoneInfo(settings.APP_TIMEZONE)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def serialize_datetime_to_app_tz(dt: datetime | None) -> str | None:
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(APP_TIMEZONE).isoformat()
