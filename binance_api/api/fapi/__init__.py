from binance_api.api.base import API as BaseAPI
from binance_api.api.fapi.fapi import Category as FapiCategory
from binance_api.api.fapi.futures import Category as FuturesCategory

__all__ = ["API"]


class API(BaseAPI):
    _url = "https://fapi.binance.com"

    @property
    def fapi(self) -> FapiCategory:
        return FapiCategory(self)

    @property
    def futures(self) -> FuturesCategory:
        return FuturesCategory(self)
