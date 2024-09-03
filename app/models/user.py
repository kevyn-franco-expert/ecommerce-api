from pydantic import BaseModel, EmailStr
from typing import Optional
from app.db import connect_db


class User(BaseModel):
    id: str = None
    username: str
    email: Optional[EmailStr] = None
    hashed_password: Optional[str] = None

    def verify_password(self, password: str):
        if self.hashed_password is None:
            return self.hashed_password == password  # Placeholder for actual password hashing


async def get_user_collection():
    db = await connect_db()
    return db["users"]
