from sqlalchemy import Table, ForeignKey, Column, String, Integer, Boolean, DateTime, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List, Optional
from datetime import datetime

from app.models.base import Base, IdMixin, TimestampMixin, NameDescriptiveMixin



category_links = Table(
    'category_links',
    Base.metadata,
    Column('top_category_id', UUID, ForeignKey('category.id'), primary_key=True),
    Column('sub_category_id', UUID, ForeignKey('category.id'), primary_key=True)
)


class Category(Base, IdMixin, TimestampMixin, NameDescriptiveMixin):
    __tablename__ = 'category'

    is_subcategory: Mapped[bool] = mapped_column(Boolean, default=False)

    sub_categories: Mapped[List["Category"]] = relationship(
        'Category',
        secondary=category_links,
        primaryjoin=id == category_links.c.top_category_id,
        secondaryjoin=id == category_links.c.sub_category_id,
        back_populates='top_categories',
        viewonly=True,
    )
    top_categories: Mapped[List["Category"]] = relationship(
        'Category',
        secondary=category_links,
        primaryjoin=id == category_links.c.sub_category_id,
        secondaryjoin=id == category_links.c.top_category_id,
        back_populates='sub_categories',
        viewonly=True,
    )
    products: Mapped[List["Product"]] = relationship(
        "Product",
        back_populates='category',
    )



