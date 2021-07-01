from binance_api.exception.code_exception import (
    CodeException as _CodeException,
)


class APIError(_CodeException):
    def __init__(self, message: str):
        self.message = message
