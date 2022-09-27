import logging

import uvloop
from aiohttp import web

from app.app import init_data
from app.database import init_database, database
from app.routes import routes

logger = logging.getLogger(__name__)


class Server:
    def __init__(self):
        self.app = web.Application()
        self.app.add_routes(routes)
        # app.middlewares.extend()
        # app.cleanup_ctx.extend()

        init_database()
        init_data()
        database.set_allow_sync(False)
        uvloop.install()  # Use fast event loop implementation

    def run(self, host: str, port: int):
        web.run_app(
            app=self.app,
            host=host,
            port=port,
        )
