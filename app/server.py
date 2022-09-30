import logging

import uvloop
from aiohttp import web

from app.db import database, init_database
from app.routes import routes

logger = logging.getLogger(__name__)


class Server:
    def __init__(self):
        self.app = web.Application()
        self.app.add_routes(routes)
        self.app.on_startup.append(self._do_startup)
        self.app.on_cleanup.append(self._do_cleanup)

    def run(self, host: str, port: int):
        web.run_app(
            app=self.app,
            host=host,
            port=port,
        )

    @staticmethod
    async def _do_startup(_: web.Application):
        logger.info('Starting...')
        init_database()
        uvloop.install()  # Use fast event loop implementation

    @staticmethod
    async def _do_cleanup(_: web.Application):
        logger.info('Cleaning up...')
        database.close()
