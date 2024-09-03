from fastapi import APIRouter, Depends

from app.auth import get_current_user
from app.schemas.user import UserCreate, UserUpdate, User
from app.schemas.utils import DeleteResponse
from app.services.user import create_user_service, get_user_service, update_user_service, delete_user_service, \
    list_users_service

router = APIRouter()


@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return await create_user_service(user)


@router.get("/{user_id}", response_model=User, dependencies=[Depends(get_current_user)])
async def get_user(user_id: str):
    return await get_user_service(user_id)


@router.put("/{user_id}", response_model=User, dependencies=[Depends(get_current_user)])
async def update_user(user_id: str, user: UserUpdate):
    return await update_user_service(user_id, user)


@router.delete("/{user_id}", response_model=DeleteResponse, dependencies=[Depends(get_current_user)])
async def delete_user(user_id: str):
    return await delete_user_service(user_id)


@router.get("/", response_model=list[User], dependencies=[Depends(get_current_user)])
async def list_users(skip: int = 0, limit: int = 10):
    return await list_users_service(skip, limit)
