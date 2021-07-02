from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveFloat

from binance_api.api.fapi.futures.data import types
from binance_api.types import Timestamp

__all__ = [
    "OpenInterestInfo",
    "OpenInterestHistResponse",
    "Request",
    "LongShortRatioInfo",
    "LongShortRatioResponse",
    "TakerLongShortRatioInfo",
    "TakerLongShortRatioResponse",
]


class OpenInterestInfo(BaseModel):
    symbol: str
    sum: PositiveFloat = Field(alias="sumOpenInterest")
    sum_value: PositiveFloat = Field(alias="sumOpenInterestValue")
    time: datetime = Field(alias="timestamp")


OpenInterestHistResponse = list[OpenInterestInfo]


class Request(BaseModel):
    symbol: str
    period: types.Period
    limit: Optional[int] = Field(ge=1, le=500)
    startTime: Optional[Timestamp] = Field(alias="start_time")
    endTime: Optional[Timestamp] = Field(alias="end_time")


class LongShortRatioInfo(BaseModel):
    symbol: str
    long_short_ratio: PositiveFloat = Field(alias="longShortRatio")
    long_ratio: PositiveFloat = Field(alias="longAccount")
    short_ratio: PositiveFloat = Field(alias="shortAccount")
    timestamp: datetime


LongShortRatioResponse = list[LongShortRatioInfo]


class TakerLongShortRatioInfo(BaseModel):
    buy_sell_ratio: PositiveFloat = Field(alias="buySellRatio")
    buy_volume: PositiveFloat = Field(alias="buyVol")
    sell_volume: PositiveFloat = Field(alias="sellVol")
    timestamp: datetime


TakerLongShortRatioResponse = list[TakerLongShortRatioInfo]
