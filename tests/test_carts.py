import pytest


@pytest.mark.asyncio
async def test_create_cart(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/carts/", json={"user_id": "1"})
        assert response.status_code == 200
        assert response.json()["user_id"] == "1"


@pytest.mark.asyncio
async def test_get_cart(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/carts/", json={"user_id": "1"})
        assert response.status_code == 200
        cart_id = response.json()["id"]

        response = await client.get(f"/carts/{cart_id}")
        assert response.status_code == 200
        assert response.json()["user_id"] == "1"


@pytest.mark.asyncio
async def test_update_cart(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/carts/", json={"user_id": "1"})
        assert response.status_code == 200
        cart_id = response.json()["id"]

        update_data = {
            "user_id": "test",
            "items": [{"test": "test"}]
        }
        response = await client.put(f"/carts/{cart_id}", json=update_data)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_cart(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/carts/", json={"user_id": "1"})
        assert response.status_code == 200
        cart_id = response.json()["id"]

        response = await client.delete(f"/carts/{cart_id}")
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_list_carts(authenticated_client):
    async for client in authenticated_client:
        for i in range(5):
            response = await client.post("/carts/", json={"user_id": f"{i + 1}"})
            assert response.status_code == 200

        response = await client.get("/carts/")
        assert response.status_code == 200
        carts = response.json()
        assert len(carts) >= 5
