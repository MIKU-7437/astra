from sqlalchemy import Table, ForeignKey, Column, Boolean, UUID, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, foreign, remote
from typing import List, Optional
from app.models.base import Base, IdMixin, TimestampMixin, NameDescriptiveMixin

category_links = Table(
    'category_links',
    Base.metadata,
    Column('top_category_id', UUID  , ForeignKey('categories.id'), primary_key=True),
    Column('sub_category_id', UUID, ForeignKey('categories.id'), primary_key=True)
)



class Category(Base, IdMixin, TimestampMixin, NameDescriptiveMixin):
    __tablename__ = 'categories'

    # Additional fields specific to Category
    is_subcategory = Column(Boolean, default=False)

    # Relationship for subcategories
    sub_categories = relationship(
        "Category",
        secondary=category_links,
        primaryjoin="Category.id == category_links.c.top_category_id",
        secondaryjoin="Category.id == category_links.c.sub_category_id",
        back_populates="top_categories"
    )

    # Relationship for top categories
    top_categories = relationship(
        "Category",
        secondary=category_links,
        primaryjoin="Category.id == category_links.c.sub_category_id",
        secondaryjoin="Category.id == category_links.c.top_category_id",
        back_populates="sub_categories"
    )

    # Relationship for products (assuming Product model exists)
    products = relationship("Product", back_populates="category")

    def __str__(self):
        return self.title  # Assuming NameDescriptiveMixin has a `name` attribute
