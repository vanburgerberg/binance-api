from collections.abc import Generator
from datetime import datetime
from enum import Enum
from enum import IntEnum as BaseIntEnum
from typing import Any, Callable, Union, cast, no_type_check

from pydantic.datetime_parse import parse_datetime

__all__ = ["StrEnum", "IntEnum", "SecurityLevel", "Timestamp", "Time"]


class StrEnum(str, Enum):
    @no_type_check
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __str__(self) -> str:
        return cast(str, self.value)


class IntEnum(BaseIntEnum):
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
    ) -> Generator[Callable[[Any], int], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> int:
        time = parse_datetime(v)
        return int(time.timestamp() * 1000)


Time = Union[datetime, str, int]
