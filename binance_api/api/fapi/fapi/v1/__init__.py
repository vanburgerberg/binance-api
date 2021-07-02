from typing import Optional, overload

from binance_api.api.fapi.fapi.v1 import models, types
from binance_api.api.fapi.fapi.v1.position_side import (
    Category as PositionSideCategory,
)
from binance_api.api.fapi.fapi.v1.ticker import Category as TickerCategory
from binance_api.category import Category as BaseCategory
from binance_api.http import Method
from binance_api.types import SecurityLevel, Time

__all__ = ["Category"]


class Category(BaseCategory):
    _path = "v1"

    @property
    def ticker(self) -> TickerCategory:
        return TickerCategory(self)

    @property
    def position_side(self) -> PositionSideCategory:
        return PositionSideCategory(self)

    async def ping(self) -> models.PingResponse:
        return await self.request(
            Method.GET, "ping", SecurityLevel.NONE, models.PingResponse
        )

    async def time(self) -> models.TimeResponse:
        return await self.request(
            Method.GET, "time", SecurityLevel.NONE, models.TimeResponse
        )

    async def exchange_info(self) -> models.ExchangeInfoResponse:
        return await self.request(
            Method.GET,
            "exchangeInfo",
            SecurityLevel.NONE,
            models.ExchangeInfoResponse,
        )

    async def depth(
        self, symbol: str, limit: Optional[types.DepthLimit] = None
    ) -> models.DepthResponse:
        request = models.DepthRequest(symbol=symbol, limit=limit)
        return await self.request(
            Method.GET,
            "depth",
            SecurityLevel.NONE,
            models.DepthResponse,
            request,
        )

    async def trades(
        self, symbol: str, limit: Optional[int] = None
    ) -> models.TradesResponse:
        request = models.TradesRequest(symbol=symbol, limit=limit)
        return await self.request(
            Method.GET,
            "trades",
            SecurityLevel.NONE,
            models.TradesResponse,
            request,
        )

    async def historical_trades(
        self,
        symbol: str,
        limit: Optional[int] = None,
        from_id: Optional[int] = None,
    ) -> models.TradesResponse:
        request = models.HistoricalTradesRequest(
            symbol=symbol, limit=limit, from_id=from_id
        )
        return await self.request(
            Method.GET,
            "historicalTrades",
            SecurityLevel.KEY,
            models.TradesResponse,
            request,
        )

    async def aggregate_trades(
        self,
        symbol: str,
        from_id: Optional[int] = None,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
        limit: Optional[int] = None,
    ) -> models.AggregateTradesResponse:
        request = models.AggregateTradesRequest(
            symbol=symbol,
            from_id=from_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            Method.GET,
            "aggTrades",
            SecurityLevel.NONE,
            models.AggregateTradesResponse,
            request,
        )

    async def klines(
        self,
        symbol: str,
        interval: str,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
        limit: Optional[int] = None,
    ) -> models.KlinesResponse:
        request = models.KlinesRequest(
            symbol=symbol,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            Method.GET,
            "klines",
            SecurityLevel.NONE,
            models.KlinesResponse,
            request,
        )

    async def continuous_klines(
        self,
        pair: str,
        contract_type: str,
        interval: str,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
        limit: Optional[int] = None,
    ) -> models.KlinesResponse:
        request = models.ContinuousKlinesRequest(
            pair=pair,
            contract_type=contract_type,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            Method.GET,
            "continuousKlines",
            SecurityLevel.NONE,
            models.KlinesResponse,
            request,
        )

    async def index_price_klines(
        self,
        pair: str,
        interval: str,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
        limit: Optional[int] = None,
    ) -> models.PriceKlinesResponse:
        request = models.IndexPriceKlinesRequest(
            pair=pair,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            Method.GET,
            "indexPriceKlines",
            SecurityLevel.NONE,
            models.PriceKlinesResponse,
            request,
        )

    async def mark_price_klines(
        self,
        symbol: str,
        interval: str,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
        limit: Optional[int] = None,
    ) -> models.PriceKlinesResponse:
        request = models.KlinesRequest(
            symbol=symbol,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            Method.GET,
            "markPriceKlines",
            SecurityLevel.NONE,
            models.PriceKlinesResponse,
            request,
        )

    @overload
    async def premium_index(self) -> models.PremiumIndexNoSymbolResponse:
        ...

    @overload
    async def premium_index(self, symbol: str) -> models.PremiumIndex:
        ...

    async def premium_index(
        self, symbol: Optional[str] = None
    ) -> models.PremiumIndexResponse:
        request = models.PremiumIndexRequest(symbol=symbol)
        return await self.request(
            Method.GET,
            "premiumIndex",
            SecurityLevel.NONE,
            models.PremiumIndexResponse,  # type: ignore[arg-type]
            request,
        )

    async def funding_rate(
        self, symbol: Optional[str] = None
    ) -> models.FundingRateResponse:
        request = models.FundingRateRequest(symbol=symbol)
        return await self.request(
            Method.GET,
            "fundingRate",
            SecurityLevel.NONE,
            models.FundingRateResponse,
            request,
        )

    async def open_interest(self, symbol: str) -> models.OpenInterestResponse:
        request = models.OpenInterestRequest(symbol=symbol)
        return await self.request(
            Method.GET,
            "openInterest",
            SecurityLevel.NONE,
            models.OpenInterestResponse,
            request,
        )

    async def lvt_klines(
        self,
        symbol: str,
        interval: str,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
        limit: Optional[int] = None,
    ) -> models.LvtKlinesResponse:
        request = models.LvtKlinesRequest(
            symbol=symbol,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            Method.GET,
            "lvtKlines",
            SecurityLevel.NONE,
            models.LvtKlinesResponse,
            request,
        )

    @overload
    async def index_info(self) -> models.IndexInfoNoSymbolResponse:
        ...

    @overload
    async def index_info(self, symbol: str) -> models.IndexInfo:
        ...

    async def index_info(
        self, symbol: Optional[str] = None
    ) -> models.IndexInfoResponse:
        request = models.IndexInfoRequest(symbol=symbol)
        return await self.request(
            Method.GET,
            "indexInfo",
            SecurityLevel.NONE,
            models.IndexInfoResponse,  # type: ignore[arg-type]
            request,
        )
