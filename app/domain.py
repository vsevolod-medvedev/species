from app.db import manager
from app.models import Genus, Observation, Species
from app.schemas import CreateObservationRequest
from app.stomp import send_stomp_message


async def get_species_list() -> list[dict]:
    query = Species.select(Species.caption, Genus.caption).join(Genus)
    all_objects = await manager.execute(query)
    return [{'species': species.caption, 'genus': species.genus.caption} for species in all_objects]


async def get_observations() -> list[dict]:
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


async def create_observation(**kwargs) -> Observation:
    """
    :raises pydantic.ValidationError
    """
    data = CreateObservationRequest.parse_obj(kwargs)
    result = await manager.create(Observation, **dict(data))
    await send_stomp_message(data={'event_type': 'create_observation', 'id': result.id})
    return result
