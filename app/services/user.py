from app.repositories.user import create_user, get_user_by_id, update_user, delete_user, \
    list_users
from app.schemas.cart import CartCreate
from app.schemas.user import UserCreate, UserUpdate
from app.services.cart import create_cart_service


async def create_user_service(user_data: UserCreate):
    hashed_password = user_data.password
    user_in_db = UserCreate(**user_data.dict(), hashed_password=hashed_password)
    user = await create_user(user_in_db)
    await create_cart_service(CartCreate(user_id=user.id))
    return user


async def get_user_service(user_id: str):
    return await get_user_by_id(user_id)


async def update_user_service(user_id: str, user_data: UserUpdate):
    update_data = user_data.dict(exclude_unset=True)
    return await update_user(user_id, update_data)


async def delete_user_service(user_id: str):
    return await delete_user(user_id)


async def list_users_service(skip: int, limit: int):
    return await list_users(skip, limit)
