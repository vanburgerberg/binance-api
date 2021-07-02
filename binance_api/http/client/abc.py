from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any, Optional

__all__ = ["Client"]


class Client(ABC):
    @abstractmethod
    async def request(
        self,
        method: str,
        url: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        pass
