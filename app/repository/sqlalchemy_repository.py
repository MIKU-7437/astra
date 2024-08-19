from typing import Type, TypeVar, Optional, Generic, List, Any
from pydantic import BaseModel
from sqlalchemy import delete, select, update, insert
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from .base_repository import AbstractRepository
from ..core.database import async_session
from ..schemas.base_schema import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=Optional[BaseModel])
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=Optional[BaseModel])


class SqlAlchemyRepository(AbstractRepository, Generic[ModelType]):
    model = None

    async def create(self, data: dict) -> ModelType:
        async with async_session() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()  # Предполагается, что возвращается объект модели

    async def update(self, data: dict, **filters) -> ModelType:
        async with async_session() as session:
            stmt = update(self.model).filter_by(**filters).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()  # Или другой метод получения результата

    async def delete(self, **filters) -> bool:
        async with async_session() as session:
            stmt = delete(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            await session.commit()
            return bool(res.rowcount)

    async def get_single(self, **filters) -> Optional[ModelType]:
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            return res.scalar_one_or_none()


    async def get_multi(self, filters: Optional[dict] = None, load_options: Optional[List[Any]] = None) -> List[ModelType]:
        filters = filters or {}
        async with async_session() as session:
            stmt = select(self.model)
            if load_options:
                for option in load_options:
                    stmt = stmt.options(option)
            if filters:
                stmt = stmt.filter_by(**filters)
            res = await session.execute(stmt)
            return res.scalars().all()

