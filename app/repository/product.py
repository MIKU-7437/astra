from .sqlalchemy_repository import SqlAlchemyRepository
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from ..models.product import Product
from typing import List

class ProductRepository(SqlAlchemyRepository[Product]):
    model = Product