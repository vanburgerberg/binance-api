from typing import Type as _Type
from typing import TypeVar as _TypeVar
from typing import cast as _cast

T = _TypeVar("T", bound=_Type["CodeException"])


class CodeExceptionMeta(type):
    def __getitem__(cls: T, code: int) -> T:  # type: ignore
        if cls.__code_specified__ is True:
            raise TypeError("code already specified")

        exception = cls.__exceptions__.get(code)
        if exception is not None:
            return _cast(T, exception)

        name = f"{cls.__name__}_{code}"
        new_exception = _cast(T, type(name, (cls,), {}))
        new_exception.__code_specified__ = True
        cls.__exceptions__[code] = new_exception

        return new_exception


class CodeException(Exception, metaclass=CodeExceptionMeta):
    code: int
    __exceptions__: dict[int, _Type["CodeException"]] = {}
    __code_specified__ = False
