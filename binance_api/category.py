from typing import Optional as _Optional
from typing import Type as _Type
from typing import TypeVar as _TypeVar

from pydantic import BaseModel as _BaseModel

from binance_api.api import ABCAPI as _ABCAPI
from binance_api.types import SecurityLevel as _SecurityLevel

_ResponseModel = _TypeVar("_ResponseModel")


class Category(_ABCAPI):
    _path: str

    def __init__(self, api: _ABCAPI):
        self._api = api

    async def request(
        self,
        method: str,
        endpoint: str,
        security_level: _SecurityLevel,
        response_model: _Type[_ResponseModel],
        request: _Optional[_BaseModel] = None,
    ) -> _ResponseModel:
        return await self._api.request(
            method,
            f"{self._path}/{endpoint}",
            security_level,
            response_model,
            request,
        )
