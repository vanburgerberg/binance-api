from collections.abc import MutableMapping as _MutableMapping
from typing import Generic as _Generic
from typing import Optional as _Optional
from typing import Type as _Type
from typing import cast as _cast

from binance_api.exception.code_factory.abc import (
    BaseCodeException as _BaseCodeException,
)
from binance_api.exception.code_factory.abc import (
    CodeException as _CodeException,
)
from binance_api.exception.code_factory.abc import (
    CodeFactory as _ABCCodeFactory,
)


class CodeFactory(_ABCCodeFactory[_CodeException], _Generic[_CodeException]):
    def __init__(
        self, base_exception: _Optional[_Type[_CodeException]] = None
    ):
        self._base_exception = (
            base_exception
            if base_exception is not None
            else _BaseCodeException
        )
        self._exceptions: _MutableMapping[int, _Type[_CodeException]] = {}

    def __call__(self, code: _Optional[int] = None) -> _Type[_CodeException]:
        if code is not None:
            return self._get_exception(code)
        return self._base_exception

    def _get_exception(self, code: int) -> _Type[_CodeException]:
        exception = self._exceptions.get(code)
        if exception is not None:
            return exception
        return self._new_exception(code)

    def _new_exception(self, code: int) -> _Type[_CodeException]:
        name = f"{self._base_exception.__name__}_{code}"
        exception = _cast(
            _Type[_CodeException],
            type(name, (self._base_exception,), {}),
        )
        exception.code = code
        self._exceptions[code] = exception
        return exception
