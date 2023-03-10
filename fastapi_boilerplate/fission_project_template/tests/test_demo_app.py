import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status


@pytest.mark.anyio
async def test_hello_world(client: AsyncClient, fastapi_app: FastAPI) -> None:
    """
    Checks the hello_world endpoint.

    :param client: client for the app.
    :param fastapi_app: current FastAPI application.
    """
    url = fastapi_app.url_path_for("hello_world")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
