from datetime import datetime

import pydantic


class CreateObservationRequest(pydantic.BaseModel):
    species_id: int
    timestamp: datetime
    latitude: float
    longitude: float
