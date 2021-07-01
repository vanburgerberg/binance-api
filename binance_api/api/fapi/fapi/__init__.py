from binance_api.api.fapi.fapi.v1 import Category as _V1Category
from binance_api.category import Category as _BaseCategory


class Category(_BaseCategory):
    _path = "fapi"

    @property
    def v1(self) -> _V1Category:
        return _V1Category(self)
