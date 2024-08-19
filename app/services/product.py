from .base_service import BaseService
from sqlalchemy.orm import joinedload
from ..schemas.product import Product
from ..models.product import Product as ProductModel
from ..repository.product import ProductRepository
from typing import List

class ProductService(BaseService):
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def get_product(self, product_id: int) -> Product:
        product = await self.repository.get_single(id=product_id)
        return Product.from_orm(product)


    
    async def get_product_list(self, **filters) -> List[Product]:
        return await self.repository.get_multi(
            filters=filters,
            load_options=[joinedload(ProductModel.category)]
        )

