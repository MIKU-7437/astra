from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List, Optional
from datetime import datetime

from app.models.base import Base, IdMixin, TimestampMixin, NameDescriptiveMixin


class Product(Base, IdMixin, TimestampMixin, NameDescriptiveMixin):
    __tablename__ = "product"

    price: Mapped[int] = mapped_column(Integer, nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    stock: Mapped[int] = mapped_column(Integer)
    photo: Mapped[Optional[str]] = mapped_column(Text)

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products",
    )
