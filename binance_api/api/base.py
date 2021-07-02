import hashlib
import hmac
import time
import urllib
from typing import Any, Optional, Type, Union

from pydantic import BaseModel, parse_obj_as

from binance_api.api.abc import API as ABCAPI
from binance_api.api.abc import ResponseModel
from binance_api.exception import APIError
from binance_api.http import ABCClient as ABCHTTPClient
from binance_api.http import AIOHTTPClient as AIOHTTPHTTPClient
from binance_api.models import APIErrorResponse
from binance_api.types import SecurityLevel

__all__ = ["API"]


class API(ABCAPI):
    _url: str

    def __init__(
        self,
        api_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        *,
        recv_window: Optional[int] = None,
        client: Optional[ABCHTTPClient] = None,
    ):
        self.client = client if client is not None else AIOHTTPHTTPClient()
        self._api_key = api_key
        self._secret_key = secret_key
        self._recv_window = recv_window

    @staticmethod
    def _parse_response(
        json: Any, model: Type[ResponseModel]
    ) -> ResponseModel:
        response: Union[APIErrorResponse, ResponseModel] = parse_obj_as(
            Union[APIErrorResponse, model], json  # type: ignore[arg-type]
        )

        if isinstance(response, APIErrorResponse):
            raise APIError[-response.code](response.message)

        return response

    def _get_key_header(self) -> dict[str, str]:
        if self._api_key is None:
            raise TypeError("API Key is required")

        return {"X-MBX-APIKEY": self._api_key}

    def _get_signature(self, query: str) -> str:
        if self._secret_key is None:
            raise TypeError("Secret Key is required")

        key = self._secret_key.encode()
        msg = query.encode()

        hash_obj = hmac.new(key, msg, hashlib.sha256)
        return hash_obj.hexdigest()

    async def request(
        self,
        method: str,
        path: str,
        security_level: SecurityLevel,
        response_model: Type[ResponseModel],
        request: Optional[BaseModel] = None,
    ) -> ResponseModel:
        headers = None
        params = request.dict(exclude_none=True) if request is not None else {}

        if security_level >= SecurityLevel.KEY:
            headers = self._get_key_header()

        if security_level >= SecurityLevel.SIGN:
            if self._recv_window is not None:
                params["recvWindow"] = self._recv_window

            params["timestamp"] = int(time.time() * 1000)

            query = urllib.parse.urlencode(params)
            params["signature"] = self._get_signature(query)

        query = urllib.parse.urlencode(params)

        json = await self.client.request(
            method, f"{self._url}/{path}?{query}", headers=headers
        )

        response = self._parse_response(json, response_model)

        return response
