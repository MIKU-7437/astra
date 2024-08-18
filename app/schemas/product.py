from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID

from .base_schema import Base
from .category import CategoryOfProduct

class Product(Base):
    id: UUID
    title: str
    slug: str
    description: Optional[str]
    price: int
    is_available: bool
    stock: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    photo: Optional[str]

    category: "CategoryOfProduct"


class ProductListResponse(Base):
    products: List[Product]

