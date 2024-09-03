from fastapi import APIRouter

from app.schemas.cart import CartCreate, Cart
from app.schemas.utils import DeleteResponse
from app.services.cart import (
    create_cart_service,
    get_cart_service,
    update_cart_service,
    delete_cart_service,
    list_carts_service,
)

router = APIRouter()


@router.post("/", response_model=Cart)
async def create_cart(cart: CartCreate):
    return await create_cart_service(cart)


@router.get("/{cart_id}", response_model=Cart)
async def get_cart(cart_id: str):
    return await get_cart_service(cart_id)


@router.put("/{cart_id}", response_model=Cart)
async def update_cart(cart_id: str, cart: CartCreate):
    return await update_cart_service(cart_id, cart)


@router.delete("/{cart_id}", response_model=DeleteResponse)
async def delete_cart(cart_id: str):
    return await delete_cart_service(cart_id)


@router.get("/", response_model=list[Cart])
async def list_carts(skip: int = 0, limit: int = 10):
    return await list_carts_service(skip, limit)
