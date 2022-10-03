from typing import List

from app.models import Genus, Observation, Species


async def get_species(manager) -> List[dict]:
    query = Species.select(Species.caption, Genus.caption).join(Genus)
    all_objects = await manager.execute(query)
    return [{'species': species.caption, 'genus': species.genus.caption} for species in all_objects]


async def get_observations(manager) -> List[dict]:
    query = Observation.select(
        Observation.timestamp, Species.caption).join(Species)
    all_objects = await manager.execute(query)
    return [
        {
            'observation': str(observation.timestamp),
            'species': observation.species.caption
        }
        for observation in all_objects
    ]
