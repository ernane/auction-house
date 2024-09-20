from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

from src.drivers.rest.main import app


@pytest.fixture(scope='session')
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client
