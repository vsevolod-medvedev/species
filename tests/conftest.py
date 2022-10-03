import asyncio

import pytest
import uvloop

from app.db import init_database, manager


@pytest.fixture(scope='session', autouse=True)
def db():
    db = init_database()
    yield manager
    db.close()


@pytest.fixture(scope='session', autouse=True)
def event_loop():
    uvloop.install()  # Use fast event loop implementation
    yield asyncio.get_event_loop()
