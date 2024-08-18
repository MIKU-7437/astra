#! /home/miku/projects/astra/.venv/bin/python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.database import async_session
from app.services.product import ProductService
from app.repository.product import ProductRepository
from app.models.product import Product  # Убедитесь, что модель Product импортирована

async def main():
    # Настройка соединения с базой данных
    async with async_session() as session:
        repository = ProductRepository(model=Product, db_session=session)  # Передаем модель и сессию
        service = ProductService(repository)
        
        # Вызов метода get_product_list для получения списка продуктов
        products = await service.get_product_list()
        from pprint import pprint
        pprint(products)


# Запуск основного асинхронного кода
asyncio.run(main())
