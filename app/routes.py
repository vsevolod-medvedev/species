from aiohttp import web

from app.views import ObservationView, SpeciesView

routes = [
    web.view('/api/v1/observations', ObservationView),
    web.view('/api/v1/species', SpeciesView),
]
