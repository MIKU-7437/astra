from pydantic import BaseModel
from typing import List
from datetime import datetime


class Product(BaseModel):
    id: int
    title: str
    slug: str
    description: str
    price: int
    is_available: bool
    stock: int
    created_date: datetime
    modified_date: datetime
    photo: str | None

    category: "Category"

