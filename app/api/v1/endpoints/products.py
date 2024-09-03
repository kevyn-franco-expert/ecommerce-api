from fastapi import APIRouter

from app.schemas.product import ProductCreate, ProductUpdate, ProductBase as Product, ProductInDB
from app.schemas.utils import DeleteResponse
from app.services.product import (
    create_product_service,
    get_product_service,
    update_product_service,
    delete_product_service,
    list_products_service,
)

router = APIRouter()


@router.post("/", response_model=Product)
async def create_product(product: ProductCreate):
    return await create_product_service(product)


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: str):
    return await get_product_service(product_id)


@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: str, product: ProductUpdate):
    return await update_product_service(product_id, product)


@router.delete("/{product_id}", response_model=DeleteResponse)
async def delete_product(product_id: str):
    return await delete_product_service(product_id)


@router.get("/", response_model=list[ProductInDB])
async def list_products(skip: int = 0, limit: int = 10):
    return await list_products_service(skip, limit)
