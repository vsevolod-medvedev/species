import json
import logging
from typing import Optional

from aiostomp import AioStomp

from app import config

logger = logging.getLogger(__name__)
stomp_client: Optional['_StompClient'] = None


class _StompClient:
    def __init__(self):
        self.client = AioStomp(
            config.AMQ_HOST, config.AMQ_PORT, error_handler=self._report_stomp_error)
        self.client.subscribe('/queue/channel', handler=self._on_message)

    def close(self):
        self.client.close()

    async def send_message(self, body: str):
        await self.client.connect()
        self.client.send('/queue/channel', body=body, headers={})
        self.client.close()

    @staticmethod
    async def _report_stomp_error(error):
        logger.error(f'STOMP error: {error}')

    @staticmethod
    async def _on_message(frame, message) -> bool:
        logger.info(f'on_message: {message}')
        return True


def init_stomp_client() -> _StompClient:
    global stomp_client
    stomp_client = _StompClient()
    return stomp_client


async def send_stomp_message(data: dict):
    await stomp_client.send_message(body=json.dumps(data))
