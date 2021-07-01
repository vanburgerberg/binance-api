from abc import ABC as _ABC
from abc import abstractmethod as _abstractmethod
from typing import Optional as _Optional
from typing import Type as _Type
from typing import TypeVar as _TypeVar

from pydantic import BaseModel as _BaseModel

from binance_api.types import SecurityLevel as _SecurityLevel

ResponseModel = _TypeVar("ResponseModel")


class API(_ABC):
    @_abstractmethod
    async def request(
        self,
        method: str,
        path: str,
        security_level: _SecurityLevel,
        response_model: _Type[ResponseModel],
        request: _Optional[_BaseModel] = None,
    ) -> ResponseModel:
        pass
