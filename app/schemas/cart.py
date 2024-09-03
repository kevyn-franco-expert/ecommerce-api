from typing import Optional

from pydantic import BaseModel


class CartItem(BaseModel):
    id: Optional[str] = ''
    product_id: str
    quantity: int


class Cart(BaseModel):
    id: str
    user_id: str
    items: list[CartItem] = []


class CartCreate(BaseModel):
    # id: Optional[str] = ''
    user_id: str
