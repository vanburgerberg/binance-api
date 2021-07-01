from datetime import datetime as _datetime
from typing import Optional as _Optional
from typing import Union as _Union

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field
from pydantic import NonNegativeInt as _NonNegativeInt
from pydantic import PositiveFloat as _PositiveFloat
from pydantic import PositiveInt as _PositiveInt


class Ticker24hr(_BaseModel):
    symbol: str
    price_change: float = _Field(alias="priceChange")
    price_change_percent: float = _Field(alias="priceChangePercent")
    weighted_avg_price: _PositiveFloat = _Field(alias="weightedAvgPrice")
    last_price: _PositiveFloat = _Field(alias="lastPrice")
    last_qty: _PositiveFloat = _Field(alias="lastQty")
    open_price: _PositiveFloat = _Field(alias="openPrice")
    high_price: _PositiveFloat = _Field(alias="highPrice")
    low_price: _PositiveFloat = _Field(alias="lowPrice")
    volume: _PositiveFloat = _Field(alias="volume")
    quote_volume: _PositiveFloat = _Field(alias="quoteVolume")
    open_time: _datetime = _Field(alias="openTime")
    close_time: _datetime = _Field(alias="closeTime")
    first_trade_id: _PositiveInt = _Field(alias="firstId")
    last_trade_id: _PositiveInt = _Field(alias="lastId")
    trade_count: _NonNegativeInt = _Field(alias="count")


Ticker24hrNoSymbolResponse = list[Ticker24hr]


Ticker24hrResponse = _Union[Ticker24hr, Ticker24hrNoSymbolResponse]


class Ticker24hrRequest(_BaseModel):
    symbol: _Optional[str]


class PriceInfo(_BaseModel):
    symbol: str
    price: _PositiveFloat
    time: _datetime


PriceInfoNoSymbolResponse = list[PriceInfo]


PriceInfoResponse = _Union[PriceInfo, PriceInfoNoSymbolResponse]


class PriceInfoRequest(_BaseModel):
    symbol: _Optional[str]


class Book(_BaseModel):
    symbol: str
    bid_price: _PositiveFloat = _Field(alias="bidPrice")
    bid_qty: _PositiveFloat = _Field(alias="bidQty")
    ask_price: _PositiveFloat = _Field(alias="askPrice")
    ask_qty: _PositiveFloat = _Field(alias="askQty")
    time: _datetime


BookNoSymbolResponse = list[Book]


BookResponse = _Union[Book, BookNoSymbolResponse]


class BookRequest(_BaseModel):
    symbol: _Optional[str]
