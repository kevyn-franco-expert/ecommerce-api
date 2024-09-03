from app.repositories.product import create_product, get_product_by_id, update_product, delete_product, list_products
from app.schemas.product import ProductCreate, ProductUpdate


async def create_product_service(product_data: ProductCreate):
    product_in_db = ProductCreate(**product_data.dict())
    product = await create_product(product_in_db)
    return product


async def get_product_service(product_id: str):
    return await get_product_by_id(product_id)


async def update_product_service(product_id: str, product_data: ProductUpdate):
    update_data = product_data.dict(exclude_unset=True)
    return await update_product(product_id, update_data)


async def delete_product_service(product_id: str):
    return await delete_product(product_id)


async def list_products_service(skip: int, limit: int):
    return await list_products(skip, limit)
