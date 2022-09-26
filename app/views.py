import json

from aiohttp import web

from app.database import manager
from app.domain import get_species


class SpeciesView(web.View):
    async def get(self):
        result = await get_species(manager)
        return web.json_response(text=json.dumps(result), status=200)
