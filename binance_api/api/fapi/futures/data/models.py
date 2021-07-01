from datetime import datetime as _datetime
from typing import Optional as _Optional

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field
from pydantic import PositiveFloat as _PositiveFloat

import binance_api.api.fapi.futures.data.types as _types
from binance_api.types import Timestamp as _Timestamp


class OpenInterestInfo(_BaseModel):
    symbol: str
    sum: _PositiveFloat = _Field(alias="sumOpenInterest")
    sum_value: _PositiveFloat = _Field(alias="sumOpenInterestValue")
    time: _datetime = _Field(alias="timestamp")


OpenInterestHistResponse = list[OpenInterestInfo]


class Request(_BaseModel):
    symbol: str
    period: _types.Period
    limit: _Optional[int] = _Field(ge=1, le=500)
    startTime: _Optional[_Timestamp] = _Field(alias="start_time")
    endTime: _Optional[_Timestamp] = _Field(alias="end_time")


class LongShortRatioInfo(_BaseModel):
    symbol: str
    long_short_ratio: _PositiveFloat = _Field(alias="longShortRatio")
    long_ratio: _PositiveFloat = _Field(alias="longAccount")
    short_ratio: _PositiveFloat = _Field(alias="shortAccount")
    timestamp: _datetime


LongShortRatioResponse = list[LongShortRatioInfo]


class TakerLongShortRatioInfo(_BaseModel):
    buy_sell_ratio: _PositiveFloat = _Field(alias="buySellRatio")
    buy_volume: _PositiveFloat = _Field(alias="buyVol")
    sell_volume: _PositiveFloat = _Field(alias="sellVol")
    timestamp: _datetime


TakerLongShortRatioResponse = list[TakerLongShortRatioInfo]
