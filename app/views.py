import json

from aiohttp import web

from app.db import manager
from app.domain import get_observations, get_species_list


class ObservationView(web.View):
    async def get(self):
        result = await get_observations(manager)
        return web.json_response(text=json.dumps(result), status=200)


class SpeciesView(web.View):
    async def get(self):
        result = await get_species_list(manager)
        return web.json_response(text=json.dumps(result), status=200)
