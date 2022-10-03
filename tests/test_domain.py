import pytest

from app.domain import get_observations, get_species


@pytest.mark.asyncio
async def test_get_observations(db):
    assert await get_observations(db) == [{'observation': '2022-10-03 12:31:43', 'species': 'Снегирь'}]


@pytest.mark.asyncio
async def test_get_species(db):
    assert await get_species(db) == [
        {'species': 'Снегирь', 'genus': 'Снегири'},
        {'species': 'Певчий дрозд', 'genus': 'Настоящие дрозды'},
    ]
