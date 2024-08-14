from .base_service import BaseService

from ..schemas.product import Product
from ..repository.product import ProductRepository

class ProductService(BaseService):
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    # Пример метода сервиса
    async def get_product(self, product_id: int) -> Product:
        product = await self.repository.get_single(id=product_id)
        return Product.from_orm(product)
