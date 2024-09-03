from contextlib import asynccontextmanager

from fastapi import Depends
from fastapi import FastAPI

from app.api.v1.endpoints import users, products, carts
from app.auth import get_current_user
from app.auth import router as auth_router
from app.db import connect_db, close_db

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await close_db()


app.include_router(auth_router)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(products.router, prefix="/products", tags=["products"], dependencies=[Depends(get_current_user)])
app.include_router(carts.router, prefix="/carts", tags=["carts"], dependencies=[Depends(get_current_user)])
