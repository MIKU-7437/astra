from .sqlalchemy_repository import SqlAlchemyRepository
from ..models.product import Product

# Если схемы не нужны, лучше не указывать None.
# В данном случае стоит изменить SqlAlchemyRepository, чтобы работать только с ModelType

class ProductRepository(SqlAlchemyRepository[Product, None, None]):
    pass
