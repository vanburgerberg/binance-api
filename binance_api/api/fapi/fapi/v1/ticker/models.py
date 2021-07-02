from datetime import datetime
from typing import Optional, Union

from pydantic import (
    BaseModel,
    Field,
    NonNegativeInt,
    PositiveFloat,
    PositiveInt,
)

__all__ = [
    "Ticker24hr",
    "Ticker24hrNoSymbolResponse",
    "Ticker24hrResponse",
    "Ticker24hrRequest",
    "PriceInfo",
    "PriceInfoNoSymbolResponse",
    "PriceInfoResponse",
    "PriceInfoRequest",
    "Book",
    "BookNoSymbolResponse",
    "BookResponse",
    "BookRequest",
]


class Ticker24hr(BaseModel):
    symbol: str
    price_change: float = Field(alias="priceChange")
    price_change_percent: float = Field(alias="priceChangePercent")
    weighted_avg_price: PositiveFloat = Field(alias="weightedAvgPrice")
    last_price: PositiveFloat = Field(alias="lastPrice")
    last_qty: PositiveFloat = Field(alias="lastQty")
    open_price: PositiveFloat = Field(alias="openPrice")
    high_price: PositiveFloat = Field(alias="highPrice")
    low_price: PositiveFloat = Field(alias="lowPrice")
    volume: PositiveFloat = Field(alias="volume")
    quote_volume: PositiveFloat = Field(alias="quoteVolume")
    open_time: datetime = Field(alias="openTime")
    close_time: datetime = Field(alias="closeTime")
    first_trade_id: PositiveInt = Field(alias="firstId")
    last_trade_id: PositiveInt = Field(alias="lastId")
    trade_count: NonNegativeInt = Field(alias="count")


Ticker24hrNoSymbolResponse = list[Ticker24hr]


Ticker24hrResponse = Union[Ticker24hr, Ticker24hrNoSymbolResponse]


class Ticker24hrRequest(BaseModel):
    symbol: Optional[str]


class PriceInfo(BaseModel):
    symbol: str
    price: PositiveFloat
    time: datetime


PriceInfoNoSymbolResponse = list[PriceInfo]


PriceInfoResponse = Union[PriceInfo, PriceInfoNoSymbolResponse]


class PriceInfoRequest(BaseModel):
    symbol: Optional[str]


class Book(BaseModel):
    symbol: str
    bid_price: PositiveFloat = Field(alias="bidPrice")
    bid_qty: PositiveFloat = Field(alias="bidQty")
    ask_price: PositiveFloat = Field(alias="askPrice")
    ask_qty: PositiveFloat = Field(alias="askQty")
    time: datetime


BookNoSymbolResponse = list[Book]


BookResponse = Union[Book, BookNoSymbolResponse]


class BookRequest(BaseModel):
    symbol: Optional[str]
