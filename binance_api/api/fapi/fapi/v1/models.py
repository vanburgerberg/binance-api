from datetime import datetime as _datetime
from typing import NamedTuple as _NamedTuple
from typing import Optional as _Optional
from typing import Union as _Union

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field
from pydantic import NonNegativeFloat as _NonNegativeFloat
from pydantic import NonNegativeInt as _NonNegativeInt
from pydantic import PositiveFloat as _PositiveFloat
from pydantic import PositiveInt as _PositiveInt

import binance_api.api.fapi.fapi.v1.types as _types
from binance_api.types import Timestamp as _Timestamp


class PingResponse(_BaseModel):
    pass


class TimeResponse(_BaseModel):
    server_time: _datetime = _Field(alias="serverTime")


class ExchangeFilter(_BaseModel):
    pass


class RateLimitInfo(_BaseModel):
    interval: _types.RateLimitInterval
    interval_count: _PositiveInt = _Field(alias="intervalNum")
    limit: _PositiveInt
    type: _types.RateLimitType = _Field(alias="rateLimitType")


class AssetInfo(_BaseModel):
    asset: str
    margin_avaliable: bool = _Field(alias="marginAvailable")
    auto_asset_exchange: float = _Field(None, alias="autoAssetExchange")


class _BaseFilter(_BaseModel):
    type: _types.FilterType = _Field(alias="filterType")


class PriceFilter(_BaseFilter):
    max_price: _PositiveFloat = _Field(alias="maxPrice")
    min_price: _PositiveFloat = _Field(alias="minPrice")
    tick_size: _PositiveFloat = _Field(alias="tickSize")


class LotSizeFilter(_BaseFilter):
    max_qty: _PositiveFloat = _Field(alias="maxQty")
    min_qty: _PositiveFloat = _Field(alias="minQty")
    step_size: _PositiveFloat = _Field(alias="stepSize")


class OrderCountFilter(_BaseFilter):
    limit: _PositiveInt


class MinNotionalFilter(_BaseFilter):
    notional: _PositiveFloat


class PercentPriceFilter(_BaseFilter):
    multiplier_up: _PositiveFloat = _Field(alias="multiplierUp")
    multiplier_down: _PositiveFloat = _Field(alias="multiplierDown")
    multiplier_precision: _PositiveInt = _Field(alias="multiplierDecimal")


Filter = _Union[
    PriceFilter,
    LotSizeFilter,
    OrderCountFilter,
    MinNotionalFilter,
    PercentPriceFilter,
]


class SymbolInfo(_BaseModel):
    symbol: str
    pair: str
    contract_type: _types.ContractType = _Field(alias="contractType")
    delivery_date: _datetime = _Field(alias="deliveryDate")
    onboard_date: _datetime = _Field(alias="onboardDate")
    status: _types.ContractStatus
    maint_margin_percent: _PositiveFloat = _Field(alias="maintMarginPercent")
    required_margin_percent: _PositiveFloat = _Field(
        alias="requiredMarginPercent"
    )
    base_asset: str = _Field(alias="baseAsset")
    quote_asset: str = _Field(alias="quoteAsset")
    margin_asset: str = _Field(alias="marginAsset")
    price_precision: _NonNegativeInt = _Field(alias="pricePrecision")
    quantity_precision: _NonNegativeInt = _Field(alias="quantityPrecision")
    base_asset_precision: _NonNegativeInt = _Field(alias="baseAssetPrecision")
    quote_asset_precision: _NonNegativeInt = _Field(alias="quotePrecision")
    underlying_type: _types.UnderlyingType = _Field(alias="underlyingType")
    underlying_sub_types: list[_types.UnderlyingSubType] = _Field(
        alias="underlyingSubType"
    )
    settle_plan: int = _Field(alias="settlePlan")
    trigger_protect: _PositiveFloat = _Field(alias="triggerProtect")
    filters: list[Filter]
    allowed_order_types: list[_types.OrderType] = _Field(alias="orderTypes")
    allowed_time_in_force: list[_types.TimeInForce] = _Field(
        alias="timeInForce"
    )


class ExchangeInfoResponse(_BaseModel):
    server_time: _datetime = _Field(alias="serverTime")
    exchange_filters: list[ExchangeFilter] = _Field(alias="exchangeFilters")
    rate_limits: list[RateLimitInfo] = _Field(alias="rateLimits")
    assets: list[AssetInfo]
    symbols: list[SymbolInfo]
    timezone: _types.Timezone


class Proposal(_NamedTuple):
    price: _PositiveFloat
    quantity: _PositiveFloat


class DepthResponse(_BaseModel):
    last_update_id: _PositiveInt = _Field(alias="lastUpdateId")
    message_output_time: _datetime = _Field(alias="E")
    transaction_time: _datetime = _Field(alias="T")
    bids: list[Proposal]
    asks: list[Proposal]


class DepthRequest(_BaseModel):
    symbol: str
    limit: _Optional[_types.DepthLimit]


class Trade(_BaseModel):
    id: _PositiveInt
    price: _PositiveFloat
    quantity: _PositiveFloat = _Field(alias="qty")
    quote_qty: _PositiveFloat = _Field(alias="quoteQty")
    time: _datetime
    is_buyer_maker: bool = _Field(alias="isBuyerMaker")


TradesResponse = list[Trade]


class TradesRequest(_BaseModel):
    symbol: str
    limit: _Optional[int] = _Field(ge=1, le=1000)


class HistoricalTradesRequest(TradesRequest):
    fromId: _Optional[_PositiveInt] = _Field(alias="from_id")


class AggregateTradeInfo(_BaseModel):
    trade_id: _PositiveInt = _Field(alias="a")
    price: _PositiveFloat = _Field(alias="p")
    quantity: _PositiveFloat = _Field(alias="q")
    first_trade_id: _PositiveInt = _Field(alias="f")
    last_trade_id: _PositiveInt = _Field(alias="l")
    time: _datetime = _Field(alias="T")
    is_buyer_maker: bool = _Field(alias="m")


AggregateTradesResponse = list[AggregateTradeInfo]


class AggregateTradesRequest(_BaseModel):
    symbol: str
    fromId: _Optional[_PositiveInt] = _Field(alias="from_id")
    startTime: _Optional[_Timestamp] = _Field(alias="start_time")
    endTime: _Optional[_Timestamp] = _Field(alias="end_time")
    limit: _Optional[int] = _Field(ge=1, le=1000)


class Bar(_NamedTuple):
    open_time: _datetime
    open: _PositiveFloat
    high: _PositiveFloat
    low: _PositiveFloat
    close: _PositiveFloat
    volume: _PositiveFloat
    close_time: _datetime
    quote_volume: _PositiveFloat
    trade_count: _PositiveInt
    taker_buy_volume: _PositiveFloat
    taker_buy_quote_volume: _PositiveFloat
    ignore: _NonNegativeFloat


KlinesResponse = list[Bar]


class KlinesRequest(_BaseModel):
    symbol: str
    interval: _types.KlineInterval
    startTime: _Optional[_Timestamp] = _Field(alias="start_time")
    endTime: _Optional[_Timestamp] = _Field(alias="end_time")
    limit: _Optional[int] = _Field(ge=1, le=1500)


class ContinuousKlinesRequest(_BaseModel):
    pair: str
    contractType: _types.ContractType = _Field(alias="contract_type")
    interval: _types.KlineInterval
    startTime: _Optional[_Timestamp] = _Field(alias="start_time")
    endTime: _Optional[_Timestamp] = _Field(alias="end_time")
    limit: _Optional[int] = _Field(ge=1, le=1500)


class PriceBar(_NamedTuple):
    open_time: _datetime
    open: _PositiveFloat
    high: _PositiveFloat
    low: _PositiveFloat
    close: _PositiveFloat
    ignore: _NonNegativeFloat
    close_time: _datetime
    ignore_2: _NonNegativeFloat
    data_count: _PositiveInt
    ignore_3: _NonNegativeFloat
    ignore_4: _NonNegativeFloat
    ignore_5: _NonNegativeFloat


PriceKlinesResponse = list[PriceBar]


class IndexPriceKlinesRequest(_BaseModel):
    pair: str
    interval: _types.KlineInterval
    startTime: _Optional[_Timestamp] = _Field(alias="start_time")
    endTime: _Optional[_Timestamp] = _Field(alias="end_time")
    limit: _Optional[int] = _Field(ge=1, le=1500)


class PremiumIndex(_BaseModel):
    symbol: str
    mark_price: _PositiveFloat = _Field(alias="markPrice")
    index_price: _PositiveFloat = _Field(alias="indexPrice")
    last_funding_rate: float = _Field(alias="lastFundingRate")
    next_funding_time: _datetime = _Field(alias="nextFundingTime")
    interest_rate: float = _Field(alias="interestRate")
    time: _datetime


class PremiumIndexNoSymbol(PremiumIndex):
    estimated_settle_price: _PositiveFloat = _Field(
        alias="estimatedSettlePrice"
    )


PremiumIndexNoSymbolResponse = list[PremiumIndexNoSymbol]


PremiumIndexResponse = _Union[PremiumIndex, PremiumIndexNoSymbolResponse]


class PremiumIndexRequest(_BaseModel):
    symbol: _Optional[str]


class FundingRate(_BaseModel):
    symbol: str
    funding_rate: float = _Field(alias="fundingRate")
    funding_time: _datetime = _Field(alias="fundingTime")


FundingRateResponse = list[FundingRate]


class FundingRateRequest(_BaseModel):
    symbol: _Optional[str]


class OpenInterestResponse(_BaseModel):
    open_interest: float = _Field(alias="openInterest")
    symbol: str
    time: _datetime


class OpenInterestRequest(_BaseModel):
    symbol: str


class LvtBar(_NamedTuple):
    open_time: _datetime
    open: _PositiveFloat
    high: _PositiveFloat
    low: _PositiveFloat
    close: _PositiveFloat
    leverage: _PositiveFloat
    close_time: _datetime
    ignore: _NonNegativeFloat
    update_count: _PositiveInt
    ignore_2: _NonNegativeFloat
    ignore_3: _NonNegativeFloat
    ignore_4: _NonNegativeFloat


LvtKlinesResponse = list[LvtBar]


class LvtKlinesRequest(_BaseModel):
    symbol: str
    interval: _types.KlineInterval
    startTime: _Optional[_Timestamp] = _Field(alias="start_time")
    endTime: _Optional[_Timestamp] = _Field(alias="end_time")
    limit: _Optional[int] = _Field(ge=1, le=1000)


class IndexAssetInfo(_BaseModel):
    base_asset: str = _Field(alias="baseAsset")
    quote_asset: str = _Field(alias="quoteAsset")
    quantity_weight: _PositiveFloat = _Field(alias="weightInQuantity")
    percentage_weight: _PositiveFloat = _Field(alias="weightInPercentage")


class IndexInfo(_BaseModel):
    symbol: str
    time: _datetime
    component: str
    base_assets: list[IndexAssetInfo] = _Field(alias="baseAssetList")


IndexInfoNoSymbolResponse = list[IndexInfo]


IndexInfoResponse = _Union[IndexInfo, IndexInfoNoSymbolResponse]


class IndexInfoRequest(_BaseModel):
    symbol: _Optional[str]
