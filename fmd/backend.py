from enum import Enum
from typing import Any, TypedDict, TypeVar

import requests
from typing_extensions import Literal


class RequestsBackend:
    def __init__(self) -> None:
        self._client: requests.Session = requests.Session()

    def send_request(
        self,
        method: str,
        url: str,
        json: dict[str, Any] | bytes | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> requests.Response:
        res = self._client.request(
            method=method,
            url=url,
            params=params,
            timeout=timeout,
            json=json,
        )
        return res


class JsonDict(TypedDict):
    pass


T = TypeVar('T', bound=JsonDict)


class ResponseStatus(str, Enum):
    SUCCESS = 'success'
    FAIL = 'fail'


class Response(TypedDict):
    status: Literal[ResponseStatus.SUCCESS, ResponseStatus.FAIL]
    msg: str


class SuccessResponse(Response):
    status: Literal[ResponseStatus.SUCCESS]
    data: list[T] | T | None


class FailResponse(Response):
    status: Literal[ResponseStatus.FAIL]


ResponseType = SuccessResponse | FailResponse
