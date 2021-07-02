from enum import auto

from binance_api.types import IntEnum, StrEnum

__all__ = [
    "RateLimitInterval",
    "RateLimitType",
    "ContractType",
    "ContractStatus",
    "UnderlyingType",
    "UnderlyingSubType",
    "FilterType",
    "OrderType",
    "TimeInForce",
    "Timezone",
    "DepthLimit",
    "KlineInterval",
]


class RateLimitInterval(StrEnum):
    MINUTE = auto()
    SECOND = auto()


class RateLimitType(StrEnum):
    REQUEST_WEIGHT = auto()
    ORDERS = auto()


class ContractType(StrEnum):
    PERPETUAL = auto()
    CURRENT_MONTH = auto()
    NEXT_MONTH = auto()
    CURRENT_QUARTER = auto()
    NEXT_QUARTER = auto()
    NONE = ""


class ContractStatus(StrEnum):
    PENDING_TRADING = auto()
    TRADING = auto()
    PRE_DELIVERING = auto()
    DELIVERING = auto()
    DELIVERED = auto()
    PRE_SETTLE = auto()
    SETTLING = auto()
    CLOSE = auto()


class UnderlyingType(StrEnum):
    COIN = auto()
    INDEX = auto()


class UnderlyingSubType(StrEnum):
    STORAGE = auto()
    DEFI = auto()
    HOT = auto()
    BSC = auto()
    NFT = auto()


class FilterType(StrEnum):
    PRICE = "PRICE_FILTER"
    LOT_SIZE = auto()
    MARKET_LOT_SIZE = auto()
    MAX_ORDER_COUNT = "MAX_NUM_ORDERS"
    MAX_ALGO_ORDER_COUNT = "MAX_NUM_ALGO_ORDERS"
    MIN_NOTIONAL = auto()
    PERCENT_PRICE = auto()


class OrderType(StrEnum):
    LIMIT = auto()
    MARKET = auto()
    STOP = auto()
    STOP_MARKET = auto()
    TAKE_PROFIT = auto()
    TAKE_PROFIT_MARKET = auto()
    TRAILING_STOP_MARKET = auto()


class TimeInForce(StrEnum):
    GTC = auto()
    IOC = auto()
    FOK = auto()
    GTX = auto()


class Timezone(StrEnum):
    UTC = auto()


class DepthLimit(IntEnum):
    FIVE = 5
    TEN = 10
    TWENTY = 20
    FIFTY = 50
    HUNDRED = 100
    FIVE_HUNDRED = 500
    THOUSAND = 1000


class KlineInterval(StrEnum):
    ONE_MINUTE = "1m"
    THREE_MINUTES = "3m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    TWO_HOURS = "2h"
    FOUR_HOURS = "4h"
    SIX_HOURS = "6h"
    EIGHT_HOURS = "8h"
    TWELVE_HOURS = "12h"
    ONE_DAY = "1d"
    THREE_DAYS = "3d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1M"
