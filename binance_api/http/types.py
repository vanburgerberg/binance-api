from enum import auto

from binance_api.types import StrEnum

__all__ = ["Method"]


class Method(StrEnum):
    GET = auto()
