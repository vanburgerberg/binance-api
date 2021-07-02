from typing import Type, TypeVar, cast

__all__ = ["CodeException"]


T = TypeVar("T", bound=Type["CodeException"])


class CodeExceptionMeta(type):
    def __getitem__(cls: T, code: int) -> T:  # type: ignore
        if cls.__code_specified__ is True:
            raise TypeError("code already specified")

        exception = cls.__exceptions__.get(code)
        if exception is not None:
            return cast(T, exception)

        name = f"{cls.__name__}_{code}"
        new_exception = cast(T, type(name, (cls,), {}))
        new_exception.__code_specified__ = True
        cls.__exceptions__[code] = new_exception

        return new_exception


class CodeException(Exception, metaclass=CodeExceptionMeta):
    code: int
    __exceptions__: dict[int, Type["CodeException"]] = {}
    __code_specified__ = False
