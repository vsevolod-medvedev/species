import logging

import uvloop
from aiohttp import web

from app.db import init_database
from app.routes import routes
from app.stomp import init_stomp_client

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

    async def _do_startup(self, _: web.Application):
        logger.info('Starting service...')
        uvloop.install()  # Use fast event loop implementation
        logger.info('Connecting to database...')
        self.database = init_database()
        logger.info('Connecting to ActiveMQ...')
        self.stomp_client = init_stomp_client()

    async def _do_cleanup(self, _: web.Application):
        logger.info('Stopping service...')
        self.stomp_client.close()
        self.database.close()
