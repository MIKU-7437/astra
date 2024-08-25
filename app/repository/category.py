from .sqlalchemy_repository import SqlAlchemyRepository
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from ..models.product import Category
from typing import List

class CategoryRepository(SqlAlchemyRepository[Category]):
    model = Category
