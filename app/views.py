import json

import pydantic
from aiohttp import web

from app.domain import create_observation, get_observations, get_species_list
from app.serializers import serialize_ext


class ObservationView(web.View):
    async def get(self):
        result = await get_observations()
        return web.json_response(text=json.dumps(result), status=200)

    async def post(self):
        data = await self.request.post()
        try:
            result = await create_observation(**data)
        except pydantic.error_wrappers.ValidationError as e:
            return web.json_response(text=str(e), status=400)
        return web.json_response(text=json.dumps(result.to_dict(), default=serialize_ext), status=200)


class SpeciesView(web.View):
    async def get(self):
        result = await get_species_list()
        return web.json_response(text=json.dumps(result), status=200)
