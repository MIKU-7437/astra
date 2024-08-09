from abc import ABC, abstractmethod

from sqlalchemy import insert, create, delete, update, select

from app.settings.database import async_url


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, **kwargs):
        raise NotImplementedError


    @abstractmethod
    async def get_one(self, **kwargs):
        raise NotImplementedError


    @abstractmethod
    async def edit_one(self, **kwargs):
        raise NotImplementedError


    @abstractmethod
    async def delete_one(self, **kwargs):
        raise NotImplementedError


    @abstractmethod
    async def get_all(self, **kwargs):
        raise NotImplementedError
