from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID

from .base_schema import Base

class Category(Base):
    id: UUID
    title: str
    slug: str
    description: Optional[str]
    is_subcategory: bool
    created_date: datetime
    updated_date: datetime

    top_categories: Optional[List["Category"]]
    sub_categories: Optional[List["Category"]]
    products: Optional[List["Product"]]


class CategoryOfProduct(Base):
    id: UUID
    title: str
    slug: str
    description: Optional[str]


class SubCategoryTree(Base):
    title: str
    slug: str
    sub_categories: Optional[List["SubCategoryTree"] | "SubCategoryTree"]
