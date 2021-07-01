from typing import Optional as _Optional
from typing import overload as _overload

import binance_api.api.fapi.fapi.v1.ticker.models as _models
from binance_api.category import Category as _BaseCategory
from binance_api.http import Method as _Method
from binance_api.types import SecurityLevel as _SecurityLevel


class Category(_BaseCategory):
    _path = "ticker"

    @_overload
    async def ticker_24hr(self) -> _models.Ticker24hrNoSymbolResponse:
        ...

    @_overload
    async def ticker_24hr(self, symbol: str) -> _models.Ticker24hr:
        ...

    async def ticker_24hr(
        self, symbol: _Optional[str] = None
    ) -> _models.Ticker24hrResponse:
        request = _models.Ticker24hrRequest(symbol=symbol)
        return await self.request(
            _Method.GET,
            "24hr",
            _SecurityLevel.NONE,
            _models.Ticker24hrResponse,  # type: ignore
            request,
        )

    @_overload
    async def price(self) -> _models.PriceInfoNoSymbolResponse:
        ...

    @_overload
    async def price(self, symbol: str) -> _models.PriceInfo:
        ...

    async def price(
        self, symbol: _Optional[str] = None
    ) -> _models.PriceInfoResponse:
        request = _models.PriceInfoRequest(symbol=symbol)
        return await self.request(
            _Method.GET,
            "price",
            _SecurityLevel.NONE,
            _models.PriceInfoResponse,  # type: ignore
            request,
        )

    @_overload
    async def book(self) -> _models.BookNoSymbolResponse:
        ...

    @_overload
    async def book(self, symbol: str) -> _models.Book:
        ...

    async def book(
        self, symbol: _Optional[str] = None
    ) -> _models.BookResponse:
        request = _models.BookRequest(symbol=symbol)
        return await self.request(
            _Method.GET,
            "bookTicker",
            _SecurityLevel.NONE,
            _models.BookResponse,  # type: ignore
            request,
        )
