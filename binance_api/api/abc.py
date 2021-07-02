from abc import ABC, abstractmethod
from typing import Optional, Type, TypeVar

from pydantic import BaseModel

from binance_api.types import SecurityLevel

__all__ = ["API", "ResponseModel"]


ResponseModel = TypeVar("ResponseModel")


class API(ABC):
    @abstractmethod
    async def request(
        self,
        method: str,
        path: str,
        security_level: SecurityLevel,
        response_model: Type[ResponseModel],
        request: Optional[BaseModel] = None,
    ) -> ResponseModel:
        pass
