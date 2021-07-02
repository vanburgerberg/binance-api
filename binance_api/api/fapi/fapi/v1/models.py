from datetime import datetime
from typing import NamedTuple, Optional, Union

from pydantic import (
    BaseModel,
    Field,
    NonNegativeFloat,
    NonNegativeInt,
    PositiveFloat,
    PositiveInt,
)

from binance_api.api.fapi.fapi.v1 import types
from binance_api.types import Timestamp

__all__ = [
    "PingResponse",
    "TimeResponse",
    "ExchangeFilter",
    "RateLimitInfo",
    "AssetInfo",
    "PriceFilter",
    "LotSizeFilter",
    "OrderCountFilter",
    "MinNotionalFilter",
    "PercentPriceFilter",
    "Filter",
    "SymbolInfo",
    "ExchangeInfoResponse",
    "Proposal",
    "DepthResponse",
    "DepthRequest",
    "Trade",
    "TradesResponse",
    "TradesRequest",
    "HistoricalTradesRequest",
    "AggregateTradeInfo",
    "AggregateTradesResponse",
    "AggregateTradesRequest",
    "Bar",
    "KlinesResponse",
    "KlinesRequest",
    "ContinuousKlinesRequest",
    "PriceBar",
    "PriceKlinesResponse",
    "IndexPriceKlinesRequest",
    "PremiumIndex",
    "PremiumIndexNoSymbol",
    "PremiumIndexNoSymbolResponse",
    "PremiumIndexResponse",
    "PremiumIndexRequest",
    "FundingRate",
    "FundingRateResponse",
    "FundingRateRequest",
    "OpenInterestResponse",
    "OpenInterestRequest",
    "LvtBar",
    "LvtKlinesResponse",
    "LvtKlinesRequest",
    "IndexAssetInfo",
    "IndexInfo",
    "IndexInfoNoSymbolResponse",
    "IndexInfoResponse",
    "IndexInfoRequest",
]


class PingResponse(BaseModel):
    pass


class TimeResponse(BaseModel):
    server_time: datetime = Field(alias="serverTime")


class ExchangeFilter(BaseModel):
    pass


class RateLimitInfo(BaseModel):
    interval: types.RateLimitInterval
    interval_count: PositiveInt = Field(alias="intervalNum")
    limit: PositiveInt
    type: types.RateLimitType = Field(alias="rateLimitType")


class AssetInfo(BaseModel):
    asset: str
    margin_avaliable: bool = Field(alias="marginAvailable")
    auto_asset_exchange: float = Field(None, alias="autoAssetExchange")


class BaseFilter(BaseModel):
    type: types.FilterType = Field(alias="filterType")


class PriceFilter(BaseFilter):
    max_price: PositiveFloat = Field(alias="maxPrice")
    min_price: PositiveFloat = Field(alias="minPrice")
    tick_size: PositiveFloat = Field(alias="tickSize")


class LotSizeFilter(BaseFilter):
    max_qty: PositiveFloat = Field(alias="maxQty")
    min_qty: PositiveFloat = Field(alias="minQty")
    step_size: PositiveFloat = Field(alias="stepSize")


class OrderCountFilter(BaseFilter):
    limit: PositiveInt


class MinNotionalFilter(BaseFilter):
    notional: PositiveFloat


class PercentPriceFilter(BaseFilter):
    multiplier_up: PositiveFloat = Field(alias="multiplierUp")
    multiplier_down: PositiveFloat = Field(alias="multiplierDown")
    multiplier_precision: PositiveInt = Field(alias="multiplierDecimal")


Filter = Union[
    PriceFilter,
    LotSizeFilter,
    OrderCountFilter,
    MinNotionalFilter,
    PercentPriceFilter,
]


class SymbolInfo(BaseModel):
    symbol: str
    pair: str
    contract_type: types.ContractType = Field(alias="contractType")
    delivery_date: datetime = Field(alias="deliveryDate")
    onboard_date: datetime = Field(alias="onboardDate")
    status: types.ContractStatus
    maint_margin_percent: PositiveFloat = Field(alias="maintMarginPercent")
    required_margin_percent: PositiveFloat = Field(
        alias="requiredMarginPercent"
    )
    base_asset: str = Field(alias="baseAsset")
    quote_asset: str = Field(alias="quoteAsset")
    margin_asset: str = Field(alias="marginAsset")
    price_precision: NonNegativeInt = Field(alias="pricePrecision")
    quantity_precision: NonNegativeInt = Field(alias="quantityPrecision")
    base_asset_precision: NonNegativeInt = Field(alias="baseAssetPrecision")
    quote_asset_precision: NonNegativeInt = Field(alias="quotePrecision")
    underlying_type: types.UnderlyingType = Field(alias="underlyingType")
    underlying_subtypes: list[types.UnderlyingSubType] = Field(
        alias="underlyingSubType"
    )
    settle_plan: int = Field(alias="settlePlan")
    trigger_protect: PositiveFloat = Field(alias="triggerProtect")
    filters: list[Filter]
    allowed_ordertypes: list[types.OrderType] = Field(alias="orderTypes")
    allowed_time_in_force: list[types.TimeInForce] = Field(alias="timeInForce")


class ExchangeInfoResponse(BaseModel):
    server_time: datetime = Field(alias="serverTime")
    exchange_filters: list[ExchangeFilter] = Field(alias="exchangeFilters")
    rate_limits: list[RateLimitInfo] = Field(alias="rateLimits")
    assets: list[AssetInfo]
    symbols: list[SymbolInfo]
    timezone: types.Timezone


class Proposal(NamedTuple):
    price: PositiveFloat
    quantity: PositiveFloat


class DepthResponse(BaseModel):
    last_update_id: PositiveInt = Field(alias="lastUpdateId")
    message_output_time: datetime = Field(alias="E")
    transaction_time: datetime = Field(alias="T")
    bids: list[Proposal]
    asks: list[Proposal]


class DepthRequest(BaseModel):
    symbol: str
    limit: Optional[types.DepthLimit]


class Trade(BaseModel):
    id: PositiveInt
    price: PositiveFloat
    quantity: PositiveFloat = Field(alias="qty")
    quote_qty: PositiveFloat = Field(alias="quoteQty")
    time: datetime
    is_buyer_maker: bool = Field(alias="isBuyerMaker")


TradesResponse = list[Trade]


class TradesRequest(BaseModel):
    symbol: str
    limit: Optional[int] = Field(ge=1, le=1000)


class HistoricalTradesRequest(TradesRequest):
    fromId: Optional[PositiveInt] = Field(alias="from_id")


class AggregateTradeInfo(BaseModel):
    trade_id: PositiveInt = Field(alias="a")
    price: PositiveFloat = Field(alias="p")
    quantity: PositiveFloat = Field(alias="q")
    first_trade_id: PositiveInt = Field(alias="f")
    last_trade_id: PositiveInt = Field(alias="l")
    time: datetime = Field(alias="T")
    is_buyer_maker: bool = Field(alias="m")


AggregateTradesResponse = list[AggregateTradeInfo]


class AggregateTradesRequest(BaseModel):
    symbol: str
    fromId: Optional[PositiveInt] = Field(alias="from_id")
    startTime: Optional[Timestamp] = Field(alias="start_time")
    endTime: Optional[Timestamp] = Field(alias="end_time")
    limit: Optional[int] = Field(ge=1, le=1000)


class Bar(NamedTuple):
    open_time: datetime
    open: PositiveFloat
    high: PositiveFloat
    low: PositiveFloat
    close: PositiveFloat
    volume: PositiveFloat
    close_time: datetime
    quote_volume: PositiveFloat
    trade_count: PositiveInt
    taker_buy_volume: PositiveFloat
    taker_buy_quote_volume: PositiveFloat
    ignore: NonNegativeFloat


KlinesResponse = list[Bar]


class KlinesRequest(BaseModel):
    symbol: str
    interval: types.KlineInterval
    startTime: Optional[Timestamp] = Field(alias="start_time")
    endTime: Optional[Timestamp] = Field(alias="end_time")
    limit: Optional[int] = Field(ge=1, le=1500)


class ContinuousKlinesRequest(BaseModel):
    pair: str
    contractType: types.ContractType = Field(alias="contract_type")
    interval: types.KlineInterval
    startTime: Optional[Timestamp] = Field(alias="start_time")
    endTime: Optional[Timestamp] = Field(alias="end_time")
    limit: Optional[int] = Field(ge=1, le=1500)


class PriceBar(NamedTuple):
    open_time: datetime
    open: PositiveFloat
    high: PositiveFloat
    low: PositiveFloat
    close: PositiveFloat
    ignore: NonNegativeFloat
    close_time: datetime
    ignore_2: NonNegativeFloat
    data_count: PositiveInt
    ignore_3: NonNegativeFloat
    ignore_4: NonNegativeFloat
    ignore_5: NonNegativeFloat


PriceKlinesResponse = list[PriceBar]


class IndexPriceKlinesRequest(BaseModel):
    pair: str
    interval: types.KlineInterval
    startTime: Optional[Timestamp] = Field(alias="start_time")
    endTime: Optional[Timestamp] = Field(alias="end_time")
    limit: Optional[int] = Field(ge=1, le=1500)


class PremiumIndex(BaseModel):
    symbol: str
    mark_price: PositiveFloat = Field(alias="markPrice")
    index_price: PositiveFloat = Field(alias="indexPrice")
    last_funding_rate: float = Field(alias="lastFundingRate")
    next_funding_time: datetime = Field(alias="nextFundingTime")
    interest_rate: float = Field(alias="interestRate")
    time: datetime


class PremiumIndexNoSymbol(PremiumIndex):
    estimated_settle_price: PositiveFloat = Field(alias="estimatedSettlePrice")


PremiumIndexNoSymbolResponse = list[PremiumIndexNoSymbol]


PremiumIndexResponse = Union[PremiumIndex, PremiumIndexNoSymbolResponse]


class PremiumIndexRequest(BaseModel):
    symbol: Optional[str]


class FundingRate(BaseModel):
    symbol: str
    funding_rate: float = Field(alias="fundingRate")
    funding_time: datetime = Field(alias="fundingTime")


FundingRateResponse = list[FundingRate]


class FundingRateRequest(BaseModel):
    symbol: Optional[str]


class OpenInterestResponse(BaseModel):
    open_interest: float = Field(alias="openInterest")
    symbol: str
    time: datetime


class OpenInterestRequest(BaseModel):
    symbol: str


class LvtBar(NamedTuple):
    open_time: datetime
    open: PositiveFloat
    high: PositiveFloat
    low: PositiveFloat
    close: PositiveFloat
    leverage: PositiveFloat
    close_time: datetime
    ignore: NonNegativeFloat
    update_count: PositiveInt
    ignore_2: NonNegativeFloat
    ignore_3: NonNegativeFloat
    ignore_4: NonNegativeFloat


LvtKlinesResponse = list[LvtBar]


class LvtKlinesRequest(BaseModel):
    symbol: str
    interval: types.KlineInterval
    startTime: Optional[Timestamp] = Field(alias="start_time")
    endTime: Optional[Timestamp] = Field(alias="end_time")
    limit: Optional[int] = Field(ge=1, le=1000)


class IndexAssetInfo(BaseModel):
    base_asset: str = Field(alias="baseAsset")
    quote_asset: str = Field(alias="quoteAsset")
    quantity_weight: PositiveFloat = Field(alias="weightInQuantity")
    percentage_weight: PositiveFloat = Field(alias="weightInPercentage")


class IndexInfo(BaseModel):
    symbol: str
    time: datetime
    component: str
    base_assets: list[IndexAssetInfo] = Field(alias="baseAssetList")


IndexInfoNoSymbolResponse = list[IndexInfo]


IndexInfoResponse = Union[IndexInfo, IndexInfoNoSymbolResponse]


class IndexInfoRequest(BaseModel):
    symbol: Optional[str]
