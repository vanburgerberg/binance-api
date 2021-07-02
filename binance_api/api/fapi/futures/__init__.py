from binance_api.api.fapi.futures.data import Category as DataCategory
from binance_api.category import Category as BaseCategory

__all__ = ["Category"]


class Category(BaseCategory):
    _path = "futures"

    @property
    def data(self) -> DataCategory:
        return DataCategory(self)
