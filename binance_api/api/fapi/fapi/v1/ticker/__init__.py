from typing import Optional, overload

from binance_api.api.fapi.fapi.v1.ticker import models
from binance_api.category import Category as BaseCategory
from binance_api.http import Method
from binance_api.types import SecurityLevel

__all__ = ["Category"]


class Category(BaseCategory):
    _path = "ticker"

    @overload
    async def ticker_24hr(self) -> models.Ticker24hrNoSymbolResponse:
        ...

    @overload
    async def ticker_24hr(self, symbol: str) -> models.Ticker24hr:
        ...

    async def ticker_24hr(
        self, symbol: Optional[str] = None
    ) -> models.Ticker24hrResponse:
        request = models.Ticker24hrRequest(symbol=symbol)
        return await self.request(
            Method.GET,
            "24hr",
            SecurityLevel.NONE,
            models.Ticker24hrResponse,  # type: ignore
            request,
        )

    @overload
    async def price(self) -> models.PriceInfoNoSymbolResponse:
        ...

    @overload
    async def price(self, symbol: str) -> models.PriceInfo:
        ...

    async def price(
        self, symbol: Optional[str] = None
    ) -> models.PriceInfoResponse:
        request = models.PriceInfoRequest(symbol=symbol)
        return await self.request(
            Method.GET,
            "price",
            SecurityLevel.NONE,
            models.PriceInfoResponse,  # type: ignore
            request,
        )

    @overload
    async def book(self) -> models.BookNoSymbolResponse:
        ...

    @overload
    async def book(self, symbol: str) -> models.Book:
        ...

    async def book(self, symbol: Optional[str] = None) -> models.BookResponse:
        request = models.BookRequest(symbol=symbol)
        return await self.request(
            Method.GET,
            "bookTicker",
            SecurityLevel.NONE,
            models.BookResponse,  # type: ignore
            request,
        )
