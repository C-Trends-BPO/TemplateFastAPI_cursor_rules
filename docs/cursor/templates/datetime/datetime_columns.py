"""Template portável — copie para db/datetime_columns.py."""

from sqlalchemy import Column, DateTime, func

from core.datetime_utils import utc_now


def dt_created(*, index: bool = False) -> Column:
    kwargs: dict = {"nullable": False, "default": utc_now, "server_default": func.now()}
    if index:
        kwargs["index"] = True
    return Column(DateTime(timezone=True), **kwargs)


def dt_updated() -> Column:
    return Column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
        onupdate=utc_now,
        server_default=func.now(),
    )


def dt_nullable(*, index: bool = False) -> Column:
    kwargs: dict = {"nullable": True}
    if index:
        kwargs["index"] = True
    return Column(DateTime(timezone=True), **kwargs)


def dt_required(*, index: bool = False) -> Column:
    kwargs: dict = {"nullable": False}
    if index:
        kwargs["index"] = True
    return Column(DateTime(timezone=True), **kwargs)
