from binance_api.api.fapi.fapi.v1 import Category as V1Category
from binance_api.category import Category as BaseCategory

__all__ = ["Category"]


class Category(BaseCategory):
    _path = "fapi"

    @property
    def v1(self) -> V1Category:
        return V1Category(self)
