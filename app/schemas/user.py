from typing import Optional

from pydantic import BaseModel


class UserBaseCreds(BaseModel):
    username: str
    email: str


class UserBase(UserBaseCreds):
    id: Optional[str] = ''


class UserCreate(UserBaseCreds):
    password: str


class UserUpdate(UserBaseCreds):
    password: str | None = None


class UserInDB(UserBaseCreds):
    hashed_password: str


class User(UserBaseCreds):
    id: str
