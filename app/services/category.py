from .base_service import BaseService
from sqlalchemy.orm import joinedload
from ..schemas.category import Category
from ..models.category import Category as CategoryModel
from ..repository.category import CategoryRepository
from typing import List

class CategoryService(BaseService):
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def get_category(self, category_id: int) -> Category:
        category = await self.repository.get_single(id=category_id)
        return Category.from_orm(category)


    
    async def get_category_list(self, **filters) -> List[Category]:
        return await self.repository.get_multi(
            filters=filters,
            load_options=[joinedload(CategoryModel.category)]
        )

    asyne def get_subcategories(self) -> Li
