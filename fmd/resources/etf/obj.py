from datetime import date
from typing import cast

from fmd.base import ManagerBase, ObjectBase
from fmd.decorators import default_data_range
from fmd.resources.etf.types import ETFDividend, ETFPrice, ETFProfile


class ETF(ObjectBase):

    @default_data_range(freq='daily', days=30)
    def get_price(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[ETFPrice]:
        path = f'/etf/{self.symbol}/price'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='yearly', years=3)
    def get_dividend(
        self, start_year: int | None = None, end_year: int | None = None
    ) -> list[ETFDividend]:
        path = f'/etf/{self.symbol}/dividend'
        params = {'start_year': start_year, 'end_year': end_year}
        return self.manger.fa.send_request('get', path, params=params)


class ETFManager(ManagerBase):
    _obj = ETF

    def get(cls, symbol: str) -> ETF:
        return cast(cls._obj, super().get(symbol=symbol))

    def get_available_list(self) -> list[ETFProfile]:
        path = '/etf'
        return self.fa.send_request('get', path)
