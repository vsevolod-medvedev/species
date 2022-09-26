from typing import List

from app.models import Genus, Species


async def get_species(manager) -> List[dict]:
    query = Species.select(Species.caption, Genus.caption).join(Genus)
    all_objects = await manager.execute(query)
    return [{'species': species.caption, 'genus': species.genus.caption} for species in all_objects]
