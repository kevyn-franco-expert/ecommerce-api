from pydantic import BaseModel

from app.db import connect_db


class Product(BaseModel):
    id: str = None
    name: str
    description: str
    price: float
    stock: int


async def get_product_collection():
    db = await connect_db()
    return db["products"]
