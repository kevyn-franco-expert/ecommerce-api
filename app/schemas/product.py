from typing import Optional

from pydantic import BaseModel


class ProductInDB(BaseModel):
    name: str
    description: str
    price: float
    stock: int


class ProductBase(ProductInDB):
    id: Optional[str] = ''


class ProductCreate(ProductInDB):
    pass


class ProductUpdate(ProductInDB):
    pass
