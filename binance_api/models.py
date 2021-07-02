from pydantic import BaseModel, Field, NegativeInt

__all__ = ["APIErrorResponse"]


class APIErrorResponse(BaseModel):
    code: NegativeInt
    message: str = Field(alias="msg")
