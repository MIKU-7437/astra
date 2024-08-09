from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, String, Text
from sqlalchemy import UUID as SQL_UUID

from typing import Optional
from uuid import UUID
from datetime import datetime



class Base(DeclarativeBase):
    __abstract__ = True



class IdMixin:
    id: Mapped[UUID] = mapped_column(
        SQL_UUID,
        primary_key=True,
        index=True,
        nullable=False,
    )


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


class NameDescriptiveMixin:
    title: Mapped[str] = mapped_column(
        String(63),
        nullable=False
    )
    slug: Mapped[str] = mapped_column(
        String(63),
        nullable=False
    )
    description: Mapped[Optional[str]] = mapped_column(Text)