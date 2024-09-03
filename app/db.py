from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"

client = None
db = None


async def connect_db():
    global client, db
    client = AsyncIOMotorClient(MONGO_DETAILS)
    db = client.ecommerce_db
    return db


async def close_db():
    global client
    if client:
        client.close()
