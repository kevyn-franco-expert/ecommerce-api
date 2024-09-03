from pydantic import BaseModel

from app.db import connect_db


class Cart(BaseModel):
    id: str = None
    user_id: str
    items: list = []


async def get_cart_collection():
    db = await connect_db()
    return db["carts"]
