from binance_api.api.fapi.futures.data import Category as _DataCategory
from binance_api.category import Category as _BaseCategory


class Category(_BaseCategory):
    _path = "futures"

    @property
    def data(self) -> _DataCategory:
        return _DataCategory(self)
