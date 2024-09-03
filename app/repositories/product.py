from bson import ObjectId

from app.models.product import Product, get_product_collection


async def create_product(product: Product):
    collection = await get_product_collection()
    product_data = product.dict()
    result = await collection.insert_one(product_data)
    product = Product(**product_data)
    product.id = str(result.inserted_id)
    return product


async def get_product_by_id(product_id: str):
    collection = await get_product_collection()
    product_data = await collection.find_one({"_id": ObjectId(product_id)})
    if product_data:
        return Product(**product_data)


async def update_product(product_id: str, product_data: dict):
    collection = await get_product_collection()
    await collection.update_one({"_id": ObjectId(product_id)}, {"$set": product_data})
    return await get_product_by_id(product_id)


async def delete_product(product_id: str):
    collection = await get_product_collection()
    result = await collection.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count:
        return {"status": "success", "message": "Product deleted successfully"}
    else:
        return {"status": "error", "message": "Product not found"}


async def list_products(skip: int = 0, limit: int = 10):
    collection = await get_product_collection()
    product_data = await collection.find().skip(skip).limit(limit).to_list(length=limit)
    products = []
    for product_data in product_data:
        product_data['id'] = str(product_data['_id'])
        del product_data['_id']
        products.append(Product(**product_data))
    return products
