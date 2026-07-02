"""Template portável — copie para schemas/sp_datetime.py."""

from datetime import datetime
from typing import Annotated

from pydantic import PlainSerializer

from core.datetime_utils import serialize_datetime_to_app_tz

SPDateTime = Annotated[
    datetime,
    PlainSerializer(serialize_datetime_to_app_tz, when_used="always"),
]

OptionalSPDateTime = Annotated[
    datetime | None,
    PlainSerializer(serialize_datetime_to_app_tz, when_used="always"),
]
