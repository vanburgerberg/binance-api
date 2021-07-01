from collections.abc import Mapping as _Mapping
from typing import Any as _Any
from typing import Optional as _Optional

import ujson as _ujson
from aiohttp import ClientSession as _ClientSession
from loguru import logger as _logger

from binance_api.http.client.abc import Client as _ABCClient


class Client(_ABCClient):
    async def request(
        self,
        method: str,
        url: str,
        *,
        headers: _Optional[_Mapping[str, str]] = None,
    ) -> _Any:
        _logger.debug(f"{method} request to {url}")

        async with _ClientSession(
            headers=headers, json_serialize=_ujson.dumps
        ) as session:
            async with session.request(method, url) as response:
                json = await response.json()

        _logger.debug(f"Response: {json}")

        return json
