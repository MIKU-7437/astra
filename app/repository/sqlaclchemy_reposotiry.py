from typing import List, TypeVar, Optional, Generic

from pydantic import BaseModel
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .base_repository import AbstractRepository
from ..models.base import Base


ModelType = TypeVar("ModelType", bound=Base)
CreatedSchemaType = TypeVar("ModelType", bound=Base)
CreatedSchemaType = TypeVar("ModelType", bound=Base)


class SqlSlchemyRepository(AbstractRepository, Generic[ModelType, CreatedSchemaType]):

