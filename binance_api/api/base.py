import hashlib as _hashlib
import hmac as _hmac
import time as _time
import urllib as _urllib
from typing import Optional as _Optional
from typing import Type as _Type

from pydantic import BaseModel as _BaseModel
from pydantic import parse_obj_as as _parse

from binance_api.api.abc import API as _ABCAPI
from binance_api.api.abc import ResponseModel as _ResponseModel
from binance_api.exception import APIError
from binance_api.http import ABCClient as _ABCHTTPClient
from binance_api.http import AIOHTTPClient as _AIOHTTPHTTPClient
from binance_api.types import SecurityLevel as _SecurityLevel


class API(_ABCAPI):
    _url: str

    def __init__(
        self,
        api_key: _Optional[str] = None,
        secret_key: _Optional[str] = None,
        *,
        recv_window: _Optional[int] = None,
        client: _Optional[_ABCHTTPClient] = None,
    ):
        self.client = client if client is not None else _AIOHTTPHTTPClient()
        self._api_key = api_key
        self._secret_key = secret_key
        self._recv_window = recv_window

    def _get_key_header(self) -> dict[str, str]:
        if self._api_key is None:
            raise TypeError("API Key is required")

        return {"X-MBX-APIKEY": self._api_key}

    def _get_signature(self, query: str) -> str:
        if self._secret_key is None:
            raise TypeError("Secret Key is required")

        key = self._secret_key.encode()
        msg = query.encode()

        hash_obj = _hmac.new(key, msg, _hashlib.sha256)
        return hash_obj.hexdigest()

    async def request(
        self,
        method: str,
        path: str,
        security_level: _SecurityLevel,
        response_model: _Type[_ResponseModel],
        request: _Optional[_BaseModel] = None,
    ) -> _ResponseModel:
        headers = None
        params = request.dict(exclude_none=True) if request is not None else {}

        if security_level >= _SecurityLevel.KEY:
            headers = self._get_key_header()

        if security_level >= _SecurityLevel.SIGN:
            if self._recv_window is not None:
                params["recvWindow"] = self._recv_window

            params["timestamp"] = int(_time.time() * 1000)

            query = _urllib.parse.urlencode(params)
            params["signature"] = self._get_signature(query)

        query = _urllib.parse.urlencode(params)

        response = await self.client.request(
            method, f"{self._url}/{path}?{query}", headers=headers
        )

        if (
            isinstance(response, dict)
            and (code := response.get("code")) is not None
            and (message := response.get("msg")) is not None
        ):
            raise APIError[code](message)

        return _parse(response_model, response)
