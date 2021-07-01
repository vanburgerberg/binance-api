from abc import ABC as _ABC
from abc import abstractmethod as _abstractmethod
from typing import Generic as _Generic
from typing import Optional as _Optional
from typing import Type as _Type
from typing import TypeVar as _TypeVar


class BaseCodeException(Exception):
    code: int


CodeException = _TypeVar("CodeException", bound=BaseCodeException)


class CodeFactory(_ABC, _Generic[CodeException]):
    @_abstractmethod
    def __call__(self, code: _Optional[int] = None) -> _Type[CodeException]:
        pass
