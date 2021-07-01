from collections.abc import Generator as _Generator
from datetime import datetime as _datetime
from enum import Enum as _Enum
from enum import IntEnum as _IntEnum
from typing import Any as _Any
from typing import Callable as _Callable
from typing import Union as _Union
from typing import cast as _cast
from typing import no_type_check as _no_type_check

from pydantic.datetime_parse import parse_datetime as _parse_datetime


class StrEnum(str, _Enum):
    @_no_type_check
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __str__(self) -> str:
        return _cast(str, self.value)


class IntEnum(_IntEnum):
    def __str__(self) -> str:
        return str(self.value)


class SecurityLevel(IntEnum):
    NONE = 0
    KEY = 1
    SIGN = 2


class Timestamp(int):
    @classmethod
    def __get_validators__(
        cls,
    ) -> _Generator[_Callable[[_Any], int], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, v: _Any) -> int:
        datetime = _parse_datetime(v)
        return int(datetime.timestamp() * 1000)


Time = _Union[_datetime, str, int]
