from typing import Optional

from binance_api.api.fapi.futures.data import models
from binance_api.category import Category as BaseCategory
from binance_api.http import Method
from binance_api.types import SecurityLevel, Time

__all__ = ["Category"]


class Category(BaseCategory):
    _path = "data"

    async def open_interest_hist(
        self,
        symbol: str,
        period: str,
        limit: Optional[int] = None,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
    ) -> models.OpenInterestHistResponse:
        request = models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            Method.GET,
            "openInterestHist",
            SecurityLevel.NONE,
            models.OpenInterestHistResponse,
            request,
        )

    async def top_long_short_account_ratio(
        self,
        symbol: str,
        period: str,
        limit: Optional[int] = None,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
    ) -> models.LongShortRatioResponse:
        request = models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            Method.GET,
            "topLongShortAccountRatio",
            SecurityLevel.KEY,
            models.LongShortRatioResponse,
            request,
        )

    async def top_long_short_position_ratio(
        self,
        symbol: str,
        period: str,
        limit: Optional[int] = None,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
    ) -> models.LongShortRatioResponse:
        request = models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            Method.GET,
            "topLongShortPositionRatio",
            SecurityLevel.KEY,
            models.LongShortRatioResponse,
            request,
        )

    async def global_long_short_account_ratio(
        self,
        symbol: str,
        period: str,
        limit: Optional[int] = None,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
    ) -> models.LongShortRatioResponse:
        request = models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            Method.GET,
            "globalLongShortAccountRatio",
            SecurityLevel.NONE,
            models.LongShortRatioResponse,
            request,
        )

    async def taker_long_short_ratio(
        self,
        symbol: str,
        period: str,
        limit: Optional[int] = None,
        start_time: Optional[Time] = None,
        end_time: Optional[Time] = None,
    ) -> models.TakerLongShortRatioResponse:
        request = models.Request(
            symbol=symbol,
            period=period,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
        )
        return await self.request(
            Method.GET,
            "takerlongshortRatio",
            SecurityLevel.NONE,
            models.TakerLongShortRatioResponse,
            request,
        )
