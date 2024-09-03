import pytest


@pytest.mark.asyncio
async def test_create_product(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/products/",
                                     json={"name": "testproduct", "description": "testdescription", "price": 100.0,
                                           "stock": 10})
        assert response.status_code == 200
        assert response.json()["name"] == "testproduct"


@pytest.mark.asyncio
async def test_get_product(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/products/",
                                     json={"name": "testproduct", "description": "testdescription", "price": 100.0,
                                           "stock": 10})
        assert response.status_code == 200
        product_id = response.json()["id"]

        response = await client.get(f"/products/{product_id}")
        assert response.status_code == 200
        assert response.json()["name"] == "testproduct"


@pytest.mark.asyncio
async def test_update_product(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/products/",
                                     json={"name": "testproduct", "description": "testdescription", "price": 100.0,
                                           "stock": 10})
        assert response.status_code == 200
        product_id = response.json()["id"]

        update_data = {"name": "updatedproduct",
                       "description": "updateddescription",
                       "price": 10,
                       "stock": 10}
        response = await client.put(f"/products/{product_id}", json=update_data)
        assert response.status_code == 200
        assert response.json()["name"] == "updatedproduct"


@pytest.mark.asyncio
async def test_delete_product(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/products/",
                                     json={"name": "testproduct", "description": "testdescription", "price": 100.0,
                                           "stock": 10})
        assert response.status_code == 200
        product_id = response.json()["id"]

        response = await client.delete(f"/products/{product_id}")
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_list_products(authenticated_client):
    async for client in authenticated_client:
        for i in range(5):
            response = await client.post("/products/",
                                         json={"name": f"testproduct{i}", "description": "testdescription",
                                               "price": 100.0,
                                               "stock": 10})
            assert response.status_code == 200

        response = await client.get("/products/")
        assert response.status_code == 200
        products = response.json()
        assert len(products) >= 5
