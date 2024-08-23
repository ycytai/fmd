from datetime import date
from typing import cast

from fmd.base import ManagerBase, ObjectBase
from fmd.decorators import default_data_range
from fmd.resources.stock.types import (
    BalanceSheet,
    FinancialRatio,
    IncomeStatement,
    Revenue,
    StockCompany,
    StockDividend,
    StockPrice,
    StockProfile,
    ValuationMeasurement,
)


class Stock(ObjectBase):

    @default_data_range(freq='daily', days=30)
    def get_price(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[StockPrice]:
        path = f'/stock/{self.symbol}/price'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='daily', days=30)
    def get_vm(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[ValuationMeasurement]:
        path = f'/stock/{self.symbol}/vm'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='yearly', years=3)
    def get_dividend(
        self, start_year: int | None = None, end_year: int | None = None
    ) -> list[StockDividend]:
        path = f'/stock/{self.symbol}/dividend'
        params = {'start_year': start_year, 'end_year': end_year}
        return self.manger.fa.send_request('get', path, params=params)

    def get_company(self) -> StockCompany:
        path = f'/stock/{self.symbol}/company'
        return self.manger.fa.send_request('get', path)

    @default_data_range(freq='monthly', months=6)
    def get_revenue(
        self,
        start_year: int | None = None,
        start_month: int | None = None,
        end_year: int | None = None,
        end_month: int | None = None,
    ) -> list[Revenue]:
        path = f'/stock/{self.symbol}/revenue'
        params = {
            'start_year': start_year,
            'start_month': start_month,
            'end_year': end_year,
            'end_month': end_month,
        }
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='quarterly', quarters=8)
    def get_financial_ratio(
        self,
        start_year: int | None = None,
        start_quarter: int | None = None,
        end_year: int | None = None,
        end_quarter: int | None = None,
    ) -> list[FinancialRatio]:
        path = f'/stock/{self.symbol}/financial-ratio'
        params = {
            'start_year': start_year,
            'start_quarter': start_quarter,
            'end_year': end_year,
            'end_quarter': end_quarter,
        }
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='quarterly', quarters=8)
    def get_balance_sheet(
        self,
        start_year: int | None = None,
        start_quarter: int | None = None,
        end_year: int | None = None,
        end_quarter: int | None = None,
    ) -> list[BalanceSheet]:
        path = f'/stock/{self.symbol}/balance-sheet'
        params = {
            'start_year': start_year,
            'start_quarter': start_quarter,
            'end_year': end_year,
            'end_quarter': end_quarter,
        }
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='quarterly', quarters=8)
    def get_income_statement(
        self,
        start_year: int | None = None,
        start_quarter: int | None = None,
        end_year: int | None = None,
        end_quarter: int | None = None,
    ) -> list[IncomeStatement]:
        path = f'/stock/{self.symbol}/income-statement'
        params = {
            'start_year': start_year,
            'start_quarter': start_quarter,
            'end_year': end_year,
            'end_quarter': end_quarter,
        }
        return self.manger.fa.send_request('get', path, params=params)


class StockManager(ManagerBase):
    _obj = Stock

    def get(self, symbol: str) -> Stock:
        return cast(self._obj, super().get(symbol=symbol))

    def get_available_list(self) -> list[StockProfile]:
        path = '/stock'
        return self.fa.send_request('get', path)
