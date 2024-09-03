import asyncio

import pytest
from main import app
from httpx import AsyncClient


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def authenticated_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        form_data = {
            "grant_type": "password",
            "username": "test2",
            "password": "test2",
            "scope": "",
            "client_id": "string",
            "client_secret": "string",
        }

        register_response = await client.post(
            "/token",
            headers={
                "accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data=form_data
        )

        assert register_response.status_code == 200

        token = register_response.json()["access_token"]

        client.headers = {"Authorization": f"Bearer {token}"}
        yield client