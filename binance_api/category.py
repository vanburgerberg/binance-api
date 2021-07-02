from typing import Optional, Type

from pydantic import BaseModel

from binance_api.api import ABCAPI
from binance_api.api.abc import ResponseModel
from binance_api.types import SecurityLevel

__all__ = ["Category"]


class Category(ABCAPI):
    _path: str

    def __init__(self, api: ABCAPI):
        self._api = api

    async def request(
        self,
        method: str,
        endpoint: str,
        security_level: SecurityLevel,
        response_model: Type[ResponseModel],
        request: Optional[BaseModel] = None,
    ) -> ResponseModel:
        return await self._api.request(
            method,
            f"{self._path}/{endpoint}",
            security_level,
            response_model,
            request,
        )
