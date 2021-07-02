from binance_api.exception.code_exception import CodeException

__all__ = ["APIError"]


class APIError(CodeException):
    def __init__(self, message: str):
        self.message = message
