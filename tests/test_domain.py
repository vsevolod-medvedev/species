from datetime import datetime

import peewee_async
import pytest

from app import models
from app.domain import create_observation, get_observations, get_species_list


@pytest.mark.asyncio
async def test_get_observations(observation: models.Observation):
    assert await get_observations() == [{'timestamp': '2022-10-03 05:31:43', 'species': 'Большой пёстрый дятел'}]


@pytest.mark.asyncio
async def test_get_species(species: models.Species):
    assert await get_species_list() == [{'species': 'Большой пёстрый дятел', 'genus': 'Пёстрые дятлы'}]


@pytest.mark.asyncio
async def test_create_observation(stomp_client, manager: peewee_async.Manager, species: models.Species):
    timestamp = datetime.utcnow()

    observation = await create_observation(
        species_id=species.id,
        timestamp=timestamp,
        latitude=56.435,
        longitude=84.982,
    )

    observation = await manager.get(models.Observation, id=observation.id)
    assert observation.species_id == species.id
    assert observation.timestamp == timestamp
    assert observation.latitude == 56.435
    assert observation.longitude == 84.982
