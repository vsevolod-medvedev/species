from aiohttp import web

from app.views import SpeciesView

routes = [
    web.view('/api/v1/species', SpeciesView),
]
