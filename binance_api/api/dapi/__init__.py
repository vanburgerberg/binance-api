from binance_api.api.base import API as BaseAPI

__all__ = ["API"]


class API(BaseAPI):
    _url = "https://dapi.binance.com"
