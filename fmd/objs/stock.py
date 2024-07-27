from datetime import date
from typing import cast

from fmd.base import ManagerBase, ObjectBase


class Stock(ObjectBase):
    def get_price(self, start_date: str | date | None = None, end_date: str | date | None = None):
        path = f'/stock/{self.symbol}/price'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    def get_vm(self, start_date: str | date | None = None, end_date: str | date | None = None):
        path = f'/stock/{self.symbol}/vm'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)


class StockManager(ManagerBase):
    _obj = Stock

    def get(cls, symbol: str) -> Stock:
        return cast(cls._obj, super().get(symbol=symbol))
