from typing import Optional as _Optional

import binance_api.api.fapi.futures.data.models as _models
from binance_api.category import Category as _BaseCategory
from binance_api.http import Method as _Method
from binance_api.types import SecurityLevel as _SecurityLevel
from binance_api.types import Time as _Time


class Category(_BaseCategory):
    _path = "data"

    async def open_interest_hist(
        self,
        symbol: str,
        period: str,
        limit: _Optional[int] = None,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
    ) -> _models.OpenInterestHistResponse:
        request = _models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            _Method.GET,
            "openInterestHist",
            _SecurityLevel.NONE,
            _models.OpenInterestHistResponse,
            request,
        )

    async def top_long_short_account_ratio(
        self,
        symbol: str,
        period: str,
        limit: _Optional[int] = None,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
    ) -> _models.LongShortRatioResponse:
        request = _models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            _Method.GET,
            "topLongShortAccountRatio",
            _SecurityLevel.KEY,
            _models.LongShortRatioResponse,
            request,
        )

    async def top_long_short_position_ratio(
        self,
        symbol: str,
        period: str,
        limit: _Optional[int] = None,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
    ) -> _models.LongShortRatioResponse:
        request = _models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            _Method.GET,
            "topLongShortPositionRatio",
            _SecurityLevel.KEY,
            _models.LongShortRatioResponse,
            request,
        )

    async def global_long_short_account_ratio(
        self,
        symbol: str,
        period: str,
        limit: _Optional[int] = None,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
    ) -> _models.LongShortRatioResponse:
        request = _models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            _Method.GET,
            "globalLongShortAccountRatio",
            _SecurityLevel.NONE,
            _models.LongShortRatioResponse,
            request,
        )

    async def taker_long_short_ratio(
        self,
        symbol: str,
        period: str,
        limit: _Optional[int] = None,
        start_time: _Optional[_Time] = None,
        end_time: _Optional[_Time] = None,
    ) -> _models.TakerLongShortRatioResponse:
        request = _models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            _Method.GET,
            "takerlongshortRatio",
            _SecurityLevel.NONE,
            _models.TakerLongShortRatioResponse,
            request,
        )
