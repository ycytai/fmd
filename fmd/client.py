import time
from typing import Any

from fmd.backend import RequestsBackend, ResponseStatus, ResponseType
from fmd.exceptions import RequestError


class FmdApi:
    def __init__(self, version: str = '1') -> None:
        self._base_url = 'https://api.fmarketdata.com'
        self._url = f'{self._base_url}/api/v{version}'
        self._client = RequestsBackend()

        # NOTE: To avoid circular import
        from fmd import resources

        # Resources
        self.stock = resources.StockManager(self)
        self.etf = resources.ETFManager(self)
        self.index = resources.IndexManager(self)

    def send_request(
        self,
        method: str,
        path: str,
        json: dict[str, Any] | bytes | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
        max_retries: int = 10,
    ):
        url = self._get_url(path)
        current_retries = 0
        while True:
            try:
                res = self._client.send_request(
                    method=method, url=url, json=json, params=params, timeout=timeout
                )
            except Exception:
                if current_retries < max_retries:
                    current_retries += 1
                    secs = current_retries * 0.5
                    time.sleep(secs)
                    continue
                raise
            res_json: ResponseType = res.json()
            if res_json.get('status') == ResponseStatus.SUCCESS:
                return res_json.get('data')
            raise RequestError(status_code=res.status_code, msg=res_json.get('msg'))

    def _get_url(self, path: str) -> str:
        if path.startswith('http://') or path.startswith('https://'):
            return path
        _url = self._url.rstrip('/')
        return f'{_url}{path}'
