# api.v1.product

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.repository.product import ProductRepository
from app.repository.product2 import ProductRepository as Product2Repository
from app.services.product import ProductService
from app.schemas.product import Product, ProductListResponse
from app.core.database import async_session, get_async_session, sync_engine

router = APIRouter(
    prefix="/products",
    tags=["products"],
)
from sqlalchemy.orm import sessionmaker


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    '/list',
    response_model=ProductListResponse,
    status_code=status.HTTP_200_OK,
)
async def list():
    service = ProductService(ProductRepository())
    products = await service.get_product_list()
    return ProductListResponse(products=products)