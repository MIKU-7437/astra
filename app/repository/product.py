from .sqlalchemy_repository import SqlAlchemyRepository
from sqlalchemy.future import select
from ..models.product import Product
from typing import List

# Если схемы не нужны, лучше не указывать None.
# В данном случае стоит изменить SqlAlchemyRepository, чтобы работать только с ModelType

class ProductRepository(SqlAlchemyRepository[Product, None, None]):
    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Product]:
        async with self._session_factory() as session:
            stmt = select(self.model).limit(limit).offset(offset)
            result = await session.execute(stmt)
            return result.scalars().all()  # Возвращаем все записи в виде списка
from ..models.product import Product
from typing import List

# Если схемы не нужны, лучше не указывать None.
# В данном случае стоит изменить SqlAlchemyRepository, чтобы работать только с ModelType

class ProductRepository(SqlAlchemyRepository[Product, None, None]):
    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Product]:
        async with self._session_factory() as session:
            stmt = select(self.model).limit(limit).offset(offset)
            result = await session.execute(stmt)
            return result.scalars().all()  # Возвращаем все записи в виде списка
