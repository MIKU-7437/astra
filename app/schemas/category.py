from pydantic import BaseModel
from typing import List
from datetime import datetime

class Category(BaseModel):
    id: int
    title: str
    slug: str
    description: Optional[str]
    is_subcategory: bool
    created_date: datetime
    modified_date: datetime

    top_categories: Optional[List["Category"]]
    sub_categories: Optional[List["Category"]]
    products: Optional[List[Product]]

    class Config:
        orm_mode = True

