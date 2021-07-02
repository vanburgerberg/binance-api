from binance_api.api.fapi.fapi.v1.position_side import models
from binance_api.category import Category as BaseCategory
from binance_api.http import Method
from binance_api.types import SecurityLevel

__all__ = ["Category"]


class Category(BaseCategory):
    _path = "positionSide"
