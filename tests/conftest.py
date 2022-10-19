import asyncio

import peewee_async
import pytest
import pytest_asyncio
import uvloop
from aiohttp.pytest_plugin import AiohttpClient

from app import models
from app.db import init_database
from app.server import Server
from app.stomp import init_stomp_client


@pytest.fixture(scope='session', autouse=True)
def manager() -> peewee_async.Manager:
    db = init_database(skip_data_migrations=True)
    yield peewee_async.Manager(db)
    db.close()


@pytest.fixture(scope='session', autouse=True)
def event_loop():
    uvloop.install()  # Use fast event loop implementation
    yield asyncio.new_event_loop()


@pytest.fixture(scope='session')
def stomp_client():
    client = init_stomp_client()
    yield client
    client.close()


@pytest_asyncio.fixture(autouse=True)
async def clean_db(manager: peewee_async.Manager) -> None:
    with manager.allow_sync():
        for model in (models.Observation, models.Species, models.Genus):
            model.truncate_table(cascade=True)


@pytest_asyncio.fixture
async def api_client(aiohttp_client) -> AiohttpClient:
    app = Server().app
    yield await aiohttp_client(app)


@pytest.fixture
def observations_endpoint() -> str:
    return '/api/v1/observations'


@pytest_asyncio.fixture
async def genus(manager: peewee_async.Manager) -> models.Genus:
    yield await manager.create(models.Genus, caption='Пёстрые дятлы')


@pytest_asyncio.fixture
async def species(manager: peewee_async.Manager, genus: models.Genus) -> models.Species:
    yield await manager.create(models.Species, genus=genus, caption='Большой пёстрый дятел')


@pytest_asyncio.fixture
async def observation(manager: peewee_async.Manager, species: models.Species) -> models.Observation:
    yield await manager.create(
        models.Observation,
        species=species,
        timestamp='2022-10-03 05:31:43',
        latitude=56.435,
        longitude=84.982,
    )
