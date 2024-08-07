from pydantic import BaseModel
from typing import List

class Category(BaseModel):
    id: int
    title: str
    slug: str
    description: str
    is_subcategory: bool
    top_categories: List["Category"]
    sub_categories: List["Category"]
    products = List["Product"]
