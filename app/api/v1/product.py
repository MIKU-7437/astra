# api.v1.product

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, HTTPException, status

from app.repository.product import ProductRepository
from app.services.product import ProductService
from app.schemas.product import Product, ProductListResponse
from app.core.database import async_session

router = APIRouter(
    prefix="/products",
    tags=["products"],
)

# Зависимость для получения сервиса с репозиторием
def get_product_service(db: AsyncSession = Depends(async_session)):
    repository = ProductRepository(Product, db)
    return ProductService(repository)

@router.get(
    '/list',
    response_model=ProductListResponse,
    status_code=status.HTTP_200_OK,
)
async def get_products(service: ProductService = Depends(get_product_service)):
    products = await service.get_product_list()
    return ProductListResponse(products=products)


@router.get(
    '/{product_id}',
    response_model=Product,
    status_code=status.HTTP_200_OK,
)
async def get_product(product_id: int, service: ProductService = Depends(get_product_service)):
    product = await service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product
