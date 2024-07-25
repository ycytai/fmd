from datetime import date
from urllib.parse import urljoin

from fmd.base import ApiBase


class FmdApi(ApiBase):
    def __init__(self) -> None:
        self.base_url = 'https://fmarketdata.com/api/'

    def get_stock_price(
        self, symbol: str, start_date: str | date | None = None, end_date: str | date | None = None
    ):
        endpoint = 'v1/stock/{symbol}/price'
        endpoint_with_params = endpoint.format(symbol=symbol)
        url = urljoin(self.base_url, endpoint_with_params)
        return self._get_data(url, start_date=start_date, end_date=end_date)

    def get_stock_vm(
        self, symbol: str, start_date: str | date | None = None, end_date: str | date | None = None
    ):
        endpoint = 'v1/stock/{symbol}/vm'
        endpoint_with_params = endpoint.format(symbol=symbol)
        url = urljoin(self.base_url, endpoint_with_params)
        return self._get_data(url, start_date=start_date, end_date=end_date)
