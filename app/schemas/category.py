from pydantic import BaseModel
from typing import List
from datetime import datetime

class Category(BaseModel):
    id: int
    title: str
    slug: str
    description: str
    is_subcategory: bool
    created_date: datetime
    modified_date: datetime
    
    top_categories: List["Category"]
    sub_categories: List["Category"]
    products = List["Product"] | None
