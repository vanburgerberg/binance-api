from binance_api.api.base import API as _BaseAPI
from binance_api.api.fapi.fapi import Category as _FapiCategory
from binance_api.api.fapi.futures import Category as _FuturesCategory


class API(_BaseAPI):
    _url = "https://fapi.binance.com"

    @property
    def fapi(self) -> _FapiCategory:
        return _FapiCategory(self)

    @property
    def futures(self) -> _FuturesCategory:
        return _FuturesCategory(self)
