from abc import ABC, abstractmethod

# from sqlalchemy import insert, create, delete, update, select

from app.core.database import async_url


from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_single(self, **kwargs):
        raise NotImplementedError

