from abc import ABC as _ABC
from abc import abstractmethod as _abstractmethod
from collections.abc import Mapping as _Mapping
from typing import Any as _Any
from typing import Optional as _Optional


class Client(_ABC):
    @_abstractmethod
    async def request(
        self,
        method: str,
        url: str,
        *,
        headers: _Optional[_Mapping[str, str]] = None,
    ) -> _Any:
        pass
