from bson import ObjectId

from app.models.cart import Cart, get_cart_collection


async def create_cart(cart: Cart):
    collection = await get_cart_collection()
    cart_data = cart.dict()
    result = await collection.insert_one(cart_data)
    cart = Cart(**cart_data)
    cart.id = str(result.inserted_id)
    return cart


async def get_cart_by_id(cart_id: str):
    collection = await get_cart_collection()
    cart_data = await collection.find_one({"_id": ObjectId(cart_id)})
    if cart_data:
        cart_data['id'] = str(cart_data['_id'])
        del cart_data['_id']
        return Cart(**cart_data)


async def update_cart(cart_id: str, cart_data: dict):
    collection = await get_cart_collection()
    await collection.update_one({"_id": ObjectId(cart_id)}, {"$set": cart_data})
    return await get_cart_by_id(cart_id)


async def delete_cart(cart_id: str):
    collection = await get_cart_collection()
    result = await collection.delete_one({"_id": ObjectId(cart_id)})
    if result.deleted_count:
        return {"status": "success", "message": "Cart deleted successfully"}
    else:
        return {"status": "error", "message": "Cart not found"}


async def list_carts(skip: int = 0, limit: int = 10):
    collection = await get_cart_collection()
    carts_data = await collection.find().skip(skip).limit(limit).to_list(length=limit)
    carts = []
    for cart_data in carts_data:
        cart_data['id'] = str(cart_data['_id'])
        del cart_data['_id']
        carts.append(Cart(**cart_data))
    return carts
