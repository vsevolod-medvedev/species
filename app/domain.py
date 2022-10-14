from datetime import datetime
from typing import List

import peewee_async

from app.models import Genus, Observation, Species


async def get_species_list(manager: peewee_async.Manager) -> List[dict]:
    query = Species.select(Species.caption, Genus.caption).join(Genus)
    all_objects = await manager.execute(query)
    return [{'species': species.caption, 'genus': species.genus.caption} for species in all_objects]


async def get_observations(manager: peewee_async.Manager) -> List[dict]:
    query = Observation.select(
        Observation.timestamp, Species.caption).join(Species)
    all_objects = await manager.execute(query)
    return [
        {
            'timestamp': str(observation.timestamp),
            'species': observation.species.caption
        }
        for observation in all_objects
    ]


async def create_observation(
    manager: peewee_async.Manager,
    species_id: int,
    timestamp: datetime,
    latitude: float,
    longitude: float,
) -> Observation:
    return await manager.create(
        Observation,
        species_id=species_id,
        timestamp=timestamp,
        latitude=latitude,
        longitude=longitude,
    )
