from binance_api.exception.code_factory import (
    BaseCodeException as _BaseCodeException,
)
from binance_api.exception.code_factory import CodeFactory as _CodeFactory


class _APIError(_BaseCodeException):
    def __init__(self, message: str):
        self.message = message


APIError = _CodeFactory(_APIError)
