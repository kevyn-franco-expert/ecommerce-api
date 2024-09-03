import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/",
                                 json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


@pytest.mark.asyncio
async def test_get_user_by_id(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/users/", json={
            "username": "testuser2",
            "password": "test",
            "email": "testuser2@example.com",
        })
        assert response.status_code == 200
        user_id = response.json()["id"]

        response = await client.get(f"/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["username"] == "testuser2"


@pytest.mark.asyncio
async def test_update_user(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/users/", json={
            "username": "testuser3",
            "password": "test",
            "email": "testuser3@example.com",
        })
        assert response.status_code == 200
        user_id = response.json()["id"]

        response = await client.put(f"/users/{user_id}",
                                    json={"username": "updateduser", "email": "updateduser@test.com"})
        assert response.status_code == 200
        assert response.json()["username"] == "updateduser"


@pytest.mark.asyncio
async def test_delete_user(authenticated_client):
    async for client in authenticated_client:
        response = await client.post("/users/", json={
            "username": "testuser4",
            "password": "test",
            "email": "testuser4@example.com",
        })
        assert response.status_code == 200
        user_id = response.json()["id"]

        response = await client.delete(f"/users/{user_id}")
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_list_users(authenticated_client):
    async for client in authenticated_client:
        for i in range(5):
            response = await client.post("/users/", json={
                "username": f"testuser{i}",
                "password": "test",
                "email": f"testuser{i}@example.com",
            })
            assert response.status_code == 200

        response = await client.get("/users/")
        assert response.status_code == 200
        users = response.json()
        assert len(users) >= 5
