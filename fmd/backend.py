from typing import Any

import requests


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
