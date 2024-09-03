from app.repositories.cart import create_cart, get_cart_by_id, update_cart, delete_cart, list_carts
from app.schemas.cart import CartCreate


async def create_cart_service(cart_data: CartCreate):
    cart_in_db = CartCreate(**cart_data.dict())
    cart = await create_cart(cart_in_db)
    return cart


async def get_cart_service(cart_id: str):
    return await get_cart_by_id(cart_id)


async def update_cart_service(cart_id: str, cart_data: dict):
    update_data = cart_data.dict(exclude_unset=True)
    return await update_cart(cart_id, update_data)


async def delete_cart_service(cart_id: str):
    return await delete_cart(cart_id)


async def list_carts_service(skip: int, limit: int):
    return await list_carts(skip, limit)
