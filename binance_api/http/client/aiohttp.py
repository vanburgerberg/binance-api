from collections.abc import Mapping
from typing import Any, Optional

import ujson
from aiohttp import ClientSession
from loguru import logger

from binance_api.http.client.abc import Client as ABCClient

__all__ = ["Client"]


class Client(ABCClient):
    async def request(
        self,
        method: str,
        url: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        logger.debug(f"{method} request to {url}")

        async with ClientSession(
            headers=headers, json_serialize=ujson.dumps
        ) as session:
            async with session.request(method, url) as response:
                json = await response.json()

        logger.debug(f"Response: {json}")

        return json
