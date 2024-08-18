from typing import Type, TypeVar, Optional, Generic

from pydantic import BaseModel
from sqlalchemy import delete, select, update, text
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from .base_repository import AbstractRepository
from ..schemas.base_schema import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=Optional[BaseModel])
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=Optional[BaseModel])



class SqlAlchemyRepository(AbstractRepository, Generic[ModelType]):

    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self._session_factory = db_session
        self.model = model

    async def create(self, data: dict) -> ModelType:
        async with self._session_factory as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def update(self, data: dict, **filters) -> ModelType:
        async with self._session_factory as session:
            stmt = update(self.model).values(**data).filter_by(**filters).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete(self, **filters) -> None:
        async with self._session_factory as session:
            await session.execute(delete(self.model).filter_by(**filters))
            await session.commit()

    async def get_single(self, **filters) -> Optional[ModelType]:
        async with self._session_factory as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            return row.scalar_one_or_none()

    
    async def get_multi(
        self,
        order="id",
        limit: int = 100,
        offset: int = 0
    ) -> list[ModelType]:
        async with self._session_factory as session:
            # Принудительно загружаем связанные данные
            stmt = (
                select(self.model)
                .options(joinedload(self.model.category))
                .order_by(text(order))
                .limit(limit)
                .offset(offset)
            )
            row = await session.execute(stmt)
            return row.scalars().all()
