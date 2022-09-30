import pytest

from app.domain import get_species


@pytest.mark.asyncio
async def test_get_species(db):
    assert await get_species(db) == [
        {'species': 'Снегирь', 'genus': 'Снегири'},
        {'species': 'Певчий дрозд', 'genus': 'Настоящие дрозды'},
    ]
