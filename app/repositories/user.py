from bson import ObjectId

from app.models.user import User, get_user_collection


async def get_user_by_username(username: str):
    collection = await get_user_collection()
    user_data = await collection.find_one({"username": username})
    if user_data:
        return User(**user_data)


async def create_user(user: User):
    collection = await get_user_collection()
    user_data = user.dict(exclude={"id"})
    result = await collection.insert_one(user_data)
    user = User(**user_data)
    user.id = str(result.inserted_id)
    return user


async def get_user_by_id(user_id: str):
    collection = await get_user_collection()
    user_data = await collection.find_one({"_id": ObjectId(user_id)})
    if user_data:
        user_data['id'] = str(user_data['_id'])
        del user_data['_id']
        return User(**user_data)


async def update_user(user_id: str, user_data: dict):
    collection = await get_user_collection()
    await collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})
    return await get_user_by_id(user_id)


async def delete_user(user_id: str):
    collection = await get_user_collection()
    result = await collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count:
        return {"status": "success", "message": "User deleted successfully"}
    else:
        return {"status": "error", "message": "User not found"}


async def list_users(skip: int = 0, limit: int = 10):
    collection = await get_user_collection()
    users = await collection.find().skip(skip).limit(limit).to_list(length=limit)
    user_list = []
    for user in users:
        user_data = {
            **user,
            "id": str(user["_id"]),
            "hashed_password": user.get("hashed_password", "")
        }
        user_list.append(User(**user_data))

    return user_list
