from enum import auto as _auto

from binance_api.types import IntEnum as _IntEnum
from binance_api.types import StrEnum as _StrEnum


class RateLimitInterval(_StrEnum):
    MINUTE = _auto()
    SECOND = _auto()


class RateLimitType(_StrEnum):
    REQUEST_WEIGHT = _auto()
    ORDERS = _auto()


class ContractType(_StrEnum):
    PERPETUAL = _auto()
    CURRENT_MONTH = _auto()
    NEXT_MONTH = _auto()
    CURRENT_QUARTER = _auto()
    NEXT_QUARTER = _auto()
    EMPTY = ""


class ContractStatus(_StrEnum):
    PENDING_TRADING = _auto()
    TRADING = _auto()
    PRE_DELIVERING = _auto()
    DELIVERING = _auto()
    DELIVERED = _auto()
    PRE_SETTLE = _auto()
    SETTLING = _auto()
    CLOSE = _auto()


class UnderlyingType(_StrEnum):
    COIN = _auto()
    INDEX = _auto()


class UnderlyingSubType(_StrEnum):
    STORAGE = _auto()
    DEFI = _auto()
    HOT = _auto()
    BSC = _auto()
    NFT = _auto()


class FilterType(_StrEnum):
    PRICE = "PRICE_FILTER"
    LOT_SIZE = _auto()
    MARKET_LOT_SIZE = _auto()
    MAX_ORDER_COUNT = "MAX_NUM_ORDERS"
    MAX_ALGO_ORDER_COUNT = "MAX_NUM_ALGO_ORDERS"
    MIN_NOTIONAL = _auto()
    PERCENT_PRICE = _auto()


class OrderType(_StrEnum):
    LIMIT = _auto()
    MARKET = _auto()
    STOP = _auto()
    STOP_MARKET = _auto()
    TAKE_PROFIT = _auto()
    TAKE_PROFIT_MARKET = _auto()
    TRAILING_STOP_MARKET = _auto()


class TimeInForce(_StrEnum):
    GTC = _auto()
    IOC = _auto()
    FOK = _auto()
    GTX = _auto()


class Timezone(_StrEnum):
    UTC = _auto()


class DepthLimit(_IntEnum):
    FIVE = 5
    TEN = 10
    TWENTY = 20
    FIFTY = 50
    HUNDRED = 100
    FIVE_HUNDRED = 500
    THOUSAND = 1000


class KlineInterval(_StrEnum):
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
