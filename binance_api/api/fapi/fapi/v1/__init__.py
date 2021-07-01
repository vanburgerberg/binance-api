from typing import Optional as _Optional
from typing import overload as _overload

import binance_api.api.fapi.fapi.v1.models as _models
import binance_api.api.fapi.fapi.v1.types as _types
from binance_api.api.fapi.fapi.v1.ticker import Category as _TickerCategory
from binance_api.category import Category as _BaseCategory
from binance_api.http import Method as _Method
from binance_api.types import SecurityLevel as _SecurityLevel
from binance_api.types import Time as _Time


class Category(_BaseCategory):
    _path = "v1"

    @property
    def ticker(self) -> _TickerCategory:
        return _TickerCategory(self)

    async def ping(self) -> _models.PingResponse:
        return await self.request(
            _Method.GET, "ping", _SecurityLevel.NONE, _models.PingResponse
        )

    async def time(self) -> _models.TimeResponse:
        return await self.request(
            _Method.GET, "time", _SecurityLevel.NONE, _models.TimeResponse
        )

    async def exchange_info(self) -> _models.ExchangeInfoResponse:
        return await self.request(
            _Method.GET,
            "exchangeInfo",
            _SecurityLevel.NONE,
            _models.ExchangeInfoResponse,
        )

    async def depth(
        self, symbol: str, limit: _Optional[_types.DepthLimit] = None
    ) -> _models.DepthResponse:
        request = _models.DepthRequest(symbol=symbol, limit=limit)
        return await self.request(
            _Method.GET,
            "depth",
            _SecurityLevel.NONE,
            _models.DepthResponse,
            request,
        )

    async def trades(
        self, symbol: str, limit: _Optional[int] = None
    ) -> _models.TradesResponse:
        request = _models.TradesRequest(symbol=symbol, limit=limit)
        return await self.request(
            _Method.GET,
            "trades",
            _SecurityLevel.NONE,
            _models.TradesResponse,
            request,
        )

    async def historical_trades(
        self,
        symbol: str,
        limit: _Optional[int] = None,
        from_id: _Optional[int] = None,
    ) -> _models.TradesResponse:
        request = _models.HistoricalTradesRequest(
            symbol=symbol, limit=limit, from_id=from_id
        )
        return await self.request(
            _Method.GET,
            "historicalTrades",
            _SecurityLevel.KEY,
            _models.TradesResponse,
            request,
        )

    async def aggregate_trades(
        self,
        symbol: str,
        from_id: _Optional[int] = None,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
        limit: _Optional[int] = None,
    ) -> _models.AggregateTradesResponse:
        request = _models.AggregateTradesRequest(
            symbol=symbol,
            from_id=from_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            _Method.GET,
            "aggTrades",
            _SecurityLevel.NONE,
            _models.AggregateTradesResponse,
            request,
        )

    async def klines(
        self,
        symbol: str,
        interval: str,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
        limit: _Optional[int] = None,
    ) -> _models.KlinesResponse:
        request = _models.KlinesRequest(
            symbol=symbol,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            _Method.GET,
            "klines",
            _SecurityLevel.NONE,
            _models.KlinesResponse,
            request,
        )

    async def continuous_klines(
        self,
        pair: str,
        contract_type: str,
        interval: str,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
        limit: _Optional[int] = None,
    ) -> _models.KlinesResponse:
        request = _models.ContinuousKlinesRequest(
            pair=pair,
            contract_type=contract_type,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            _Method.GET,
            "continuousKlines",
            _SecurityLevel.NONE,
            _models.KlinesResponse,
            request,
        )

    async def index_price_klines(
        self,
        pair: str,
        interval: str,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
        limit: _Optional[int] = None,
    ) -> _models.PriceKlinesResponse:
        request = _models.IndexPriceKlinesRequest(
            pair=pair,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            _Method.GET,
            "indexPriceKlines",
            _SecurityLevel.NONE,
            _models.PriceKlinesResponse,
            request,
        )

    async def mark_price_klines(
        self,
        symbol: str,
        interval: str,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
        limit: _Optional[int] = None,
    ) -> _models.PriceKlinesResponse:
        request = _models.KlinesRequest(
            symbol=symbol,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            _Method.GET,
            "markPriceKlines",
            _SecurityLevel.NONE,
            _models.PriceKlinesResponse,
            request,
        )

    @_overload
    async def premium_index(self) -> _models.PremiumIndexNoSymbolResponse:
        ...

    @_overload
    async def premium_index(self, symbol: str) -> _models.PremiumIndex:
        ...

    async def premium_index(
        self, symbol: _Optional[str] = None
    ) -> _models.PremiumIndexResponse:
        request = _models.PremiumIndexRequest(symbol=symbol)
        return await self.request(
            _Method.GET,
            "premiumIndex",
            _SecurityLevel.NONE,
            _models.PremiumIndexResponse,  # type: ignore
            request,
        )

    async def funding_rate(
        self, symbol: _Optional[str] = None
    ) -> _models.FundingRateResponse:
        request = _models.FundingRateRequest(symbol=symbol)
        return await self.request(
            _Method.GET,
            "fundingRate",
            _SecurityLevel.NONE,
            _models.FundingRateResponse,
            request,
        )

    async def open_interest(self, symbol: str) -> _models.OpenInterestResponse:
        request = _models.OpenInterestRequest(symbol=symbol)
        return await self.request(
            _Method.GET,
            "openInterest",
            _SecurityLevel.NONE,
            _models.OpenInterestResponse,
            request,
        )

    async def lvt_klines(
        self,
        symbol: str,
        interval: str,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
        limit: _Optional[int] = None,
    ) -> _models.LvtKlinesResponse:
        request = _models.LvtKlinesRequest(
            symbol=symbol,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        return await self.request(
            _Method.GET,
            "lvtKlines",
            _SecurityLevel.NONE,
            _models.LvtKlinesResponse,
            request,
        )

    @_overload
    async def index_info(self) -> _models.IndexInfoNoSymbolResponse:
        ...

    @_overload
    async def index_info(self, symbol: str) -> _models.IndexInfo:
        ...

    async def index_info(
        self, symbol: _Optional[str] = None
    ) -> _models.IndexInfoResponse:
        request = _models.IndexInfoRequest(symbol=symbol)
        return await self.request(
            _Method.GET,
            "indexInfo",
            _SecurityLevel.NONE,
            _models.IndexInfoResponse,  # type: ignore
            request,
        )
