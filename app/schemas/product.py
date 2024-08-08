from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Product(BaseModel):
    id: int
    title: str
    slug: str
    description: Optional[str]
    price: int
    is_available: bool
    stock: int
    created_date: datetime
    modified_date: datetime
    photo: Optional[str]

    category: "Category"

    class Config:
        orm_mode = True
