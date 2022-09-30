import logging

import uvloop
from aiohttp import web

from app.db import init_database
from app.routes import routes

logger = logging.getLogger(__name__)


class Server:
    def __init__(self):
        self.app = web.Application()
        self.app.add_routes(routes)
        # app.middlewares.extend()
        # app.cleanup_ctx.extend()

        init_database()

        uvloop.install()  # Use fast event loop implementation

    def run(self, host: str, port: int):
        web.run_app(
            app=self.app,
            host=host,
            port=port,
        )
