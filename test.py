#! /home/miku/projects/astra/.venv/bin/python
from typing import Type, TypeVar, Optional, Generic, List, Any
from pydantic import BaseModel
from sqlalchemy import delete, select, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.repository.base_repository import AbstractRepository
from app.core.database import async_session
from app.schemas.base_schema import Base
from app.models.category import Category
from app.models.product import *
from app.schemas.category import SubCategoryTree
import asyncio

# Создаем тип для модели
ModelType = TypeVar("ModelType", bound=Base)

# Общий репозиторий для SQLAlchemy моделей
class SqlAlchemyRepository(AbstractRepository, Generic[ModelType]):
    model: Type[ModelType]  # Это SQLAlchemy модель

    def _model_to_schema(self, model_instance: ModelType, schema: Type[BaseModel]) -> BaseModel:
        """Конвертация SQLAlchemy модели в Pydantic схему."""
        return schema.from_orm(model_instance)

    async def create(self, schema_in: BaseModel, schema_out: Type[BaseModel]) -> BaseModel:
        async with async_session() as session:
            data = schema_in.dict(exclude_unset=True)
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return self._model_to_schema(res.scalar_one(), schema_out)

    async def update(self, schema_in: BaseModel, schema_out: Type[BaseModel], **filters) -> BaseModel:
        async with async_session() as session:
            data = schema_in.dict(exclude_unset=True)
            stmt = update(self.model).filter_by(**filters).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return self._model_to_schema(res.scalar_one(), schema_out)

    async def delete(self, **filters) -> bool:
        async with async_session() as session:
            stmt = delete(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            await session.commit()
            return bool(res.rowcount)

    async def get_single(self, schema_out: Type[BaseModel], **filters) -> Optional[BaseModel]:
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filters).options(selectinload(self.model.sub_categories))
            res = await session.execute(stmt)
            result = res.scalar_one_or_none()
            return self._model_to_schema(result, schema_out) if result else None

    async def get_multi(self, schema_out: Type[BaseModel], filters: Optional[dict] = None, load_options: Optional[List[Any]] = None) -> List[BaseModel]:
        filters = filters or {}
        async with async_session() as session:
            stmt = select(self.model)
            if load_options:
                for option in load_options:
                    stmt = stmt.options(option)
            else:
                stmt = stmt.options(selectinload(self.model.sub_categories))  # Загружаем связанные данные
            if filters:
                stmt = stmt.filter_by(**filters)
            res = await session.execute(stmt)
            return [self._model_to_schema(model, schema_out) for model in res.scalars().all()]

# Конкретный репозиторий для модели Category
class CatRepository(SqlAlchemyRepository[Category]):
    model = Category

repo = CatRepository()

async def m():
    categories = await repo.get_multi(SubCategoryTree)
    from pprint import pprint 
    pprint(categories)


# Запуск асинхронной функции
asyncio.run(m())
