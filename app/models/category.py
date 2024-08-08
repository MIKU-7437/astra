from sqlalchemy import Table, ForeignKey, Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List, Optional
from datetime import datetime

from app.core.database import Base


category_links = Table(
    'category_links',
    Base.metadata,
    Column('top_category_id', Integer, ForeignKey('category.id'), primary_key=True),
    Column('sub_category_id', Integer, ForeignKey('category.id'), primary_key=True)
)


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String)
    is_subcategory: Mapped[bool] = mapped_column(Boolean, default=False)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    modified_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

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


