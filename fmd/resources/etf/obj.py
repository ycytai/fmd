from datetime import date
from typing import cast

from fmd.base import ManagerBase, ObjectBase
from fmd.resources.etf.types import EtfDividend


class Etf(ObjectBase):
    def get_price(self, start_date: str | date | None = None, end_date: str | date | None = None):
        path = f'/etf/{self.symbol}/price'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    def get_dividend(
        self, start_year: int | None = None, end_year: int | None = None
    ) -> list[EtfDividend]:
        path = f'/etf/{self.symbol}/dividend'
        params = {'start_year': start_year, 'end_year': end_year}
        return self.manger.fa.send_request('get', path, params=params)


class EtfManager(ManagerBase):
    _obj = Etf

    def get(cls, symbol: str) -> Etf:
        return cast(cls._obj, super().get(symbol=symbol))

    def get_available_list(self):
        path = '/etf'
        return self.fa.send_request('get', path)
