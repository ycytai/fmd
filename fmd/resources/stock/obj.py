from datetime import date
from typing import cast

from fmd.base import ManagerBase, ObjectBase
from fmd.decorators import default_data_range
from fmd.resources.stock.types import (
    BalanceSheet,
    CashFlowStatement,
    FinancialRatio,
    IncomeStatement,
    Revenue,
    StockCompany,
    StockDividend,
    StockInstitutionTradeSummary,
    StockMarginBalance,
    StockPrice,
    StockProfile,
    ValuationMeasurement,
)


class Stock(ObjectBase):
    """
    Represents a stock.

    Example:
        ```python
        from fmd import FmdApi

        fa = FmdApi()
        stock = fa.stock.get(symbol='2330')
        ```

    Attributes:
        symbol (str): The symbol of the stock.

    Methods:
        get_price(start_date, end_date):
            Retrieves the price data for the stock within the specified date range.
        get_vm(start_date, end_date):
            Retrieves the valuation measurement data for the stock within the specified date range.
        get_dividend(start_year, end_year):
            Retrieves the dividend data for the stock within the specified year range.
        get_company():
            Retrieves the company profile for the stock.
        get_revenue(start_year, start_month, end_year, end_month):
            Retrieves the revenue data for the stock within the specified date range.
        get_financial_ratio(start_year, start_quarter, end_year, end_quarter):
            Retrieves the financial ratio data for the stock within the specified date range.
        get_balance_sheet(start_year, start_quarter, end_year, end_quarter):
            Retrieves the balance sheet data for the stock within the specified date range.
        get_income_statement(start_year, start_quarter, end_year, end_quarter):
            Retrieves the income statement data for the stock within the specified date range.
        get_margin_balance(start_date, end_date):
            Retrieves the margin balance data for the stock within the specified date range.
        get_institution_trade_summary(start_date, end_date):
            Retrieves the institution trade summary for the stock within the specified date range.
        get_cash_flow_statement(start_year, start_quarter, end_year, end_quarter):
            Retrieves the cash flow statement data for the stock within the specified date range.
    """

    @default_data_range(freq='daily', days=30)
    def get_price(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[StockPrice]:
        """
        Retrieves the price data for the stock within the specified date range.
        Default data range is last 30 days.

        Parameters:
            start_date (str | date | None): The start date for the price data.
            end_date (str | date | None): The end date for the price data.

        Returns:
            A list of `StockPrice` objects containing price information.
        """
        path = f'/stock/{self.symbol}/price'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='daily', days=30)
    def get_vm(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[ValuationMeasurement]:
        """
        Retrieves the valuation measurement data for the stock within the specified date range.
        Default data range is last 30 days.

        Parameters:
            start_date (str | date | None): The start date for the valuation measurement data.
            end_date (str | date | None): The end date for the valuation measurement data.

        Returns:
            A list of `ValuationMeasurement` objects containing valuation measurement information.
        """
        path = f'/stock/{self.symbol}/vm'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='yearly', years=3)
    def get_dividend(
        self, start_year: int | None = None, end_year: int | None = None
    ) -> list[StockDividend]:
        """
        Retrieves the dividend data for the stock within the specified year range.
        Default data range is last 3 years.

        Parameters:
            start_year (int | None): The start year for the dividend data.
            end_year (int | None): The end year for the dividend data.

        Returns:
            A list of `StockDividend` objects containing dividend information.
        """
        path = f'/stock/{self.symbol}/dividend'
        params = {'start_year': start_year, 'end_year': end_year}
        return self.manger.fa.send_request('get', path, params=params)

    def get_company(self) -> StockCompany:
        """
        Retrieves the company profile for the stock.

        Returns:
            A `StockCompany` object containing the company's profile information.
        """
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
        """
        Retrieves the revenue data for the stock within the specified date range.
        Default data range is last 6 months.

        Parameters:
            start_year (int | None): The start year for the revenue data.
            start_month (int | None): The start month for the revenue data.
            end_year (int | None): The end year for the revenue data.
            end_month (int | None): The end month for the revenue data.

        Returns:
            A list of `Revenue` objects containing revenue information.
        """
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
        """
        Retrieves the financial ratio data for the stock within the specified date range.
        Default data range is last 8 quarters.

        Parameters:
            start_year (int | None): The start year for the financial ratio data.
            start_quarter (int | None): The start quarter for the financial ratio data.
            end_year (int | None): The end year for the financial ratio data.
            end_quarter (int | None): The end quarter for the financial ratio data.

        Returns:
            A list of `FinancialRatio` objects containing financial ratio information.
        """
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
        """
        Retrieves the balance sheet data for the stock within the specified date range.
        Default data range is last 8 quarters.

        Parameters:
            start_year (int | None): The start year for the balance sheet data.
            start_quarter (int | None): The start quarter for the balance sheet data.
            end_year (int | None): The end year for the balance sheet data.
            end_quarter (int | None): The end quarter for the balance sheet data.

        Returns:
            A list of `BalanceSheet` objects containing balance sheet information.
        """
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
        """
        Retrieves the income statement data for the stock within the specified date range.
        Default data range is last 8 quarters.

        Parameters:
            start_year (int | None): The start year for the income statement data.
            start_quarter (int | None): The start quarter for the income statement data.
            end_year (int | None): The end year for the income statement data.
            end_quarter (int | None): The end quarter for the income statement data.

        Returns:
            A list of `IncomeStatement` objects containing income statement information.
        """
        path = f'/stock/{self.symbol}/income-statement'
        params = {
            'start_year': start_year,
            'start_quarter': start_quarter,
            'end_year': end_year,
            'end_quarter': end_quarter,
        }
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='daily', days=30)
    def get_margin_balance(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[StockMarginBalance]:
        """
        Retrieves the margin balance data for the stock within the specified date range.
        Default data range is last 30 days.

        Parameters:
            start_date (str | date | None): The start date for the data.
            end_date (str | date | None): The end date for the data.

        Returns:
            A list of `StockMarginBalance` objects containing margin balance information.
        """
        path = f'/stock/{self.symbol}/margin-balance'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='daily', days=30)
    def get_institution_trade_summary(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[StockInstitutionTradeSummary]:
        """
        Retrieves the institution trade summary for the stock within the specified date range.
        Default data range is last 30 days.

        Parameters:
            start_date (str | date | None): The start date for data.
            end_date (str | date | None): The end date for data.

        Returns:
            A list of `StockInstitutionTradeSummary` objects containing institutions trade summary.
        """
        path = f'/stock/{self.symbol}/institution-trade-summary'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='quarterly', quarters=8)
    def get_cash_flow_statement(
        self,
        start_year: int | None = None,
        start_quarter: int | None = None,
        end_year: int | None = None,
        end_quarter: int | None = None,
    ) -> list[CashFlowStatement]:
        """
        Retrieves the cash flow statement data for the stock within the specified date range.
        Default data range is last 8 quarters.

        Parameters:
            start_year (int | None): The start year for the cash flow statement data.
            start_quarter (int | None): The start quarter for the cash flow statement data.
            end_year (int | None): The end year for the cash flow statement data.
            end_quarter (int | None): The end quarter for the cash flow statement data.

        Returns:
            A list of `CashFlowStatement` objects containing cash flow statement information.
        """
        path = f'/stock/{self.symbol}/cash-flow-statement'
        params = {
            'start_year': start_year,
            'start_quarter': start_quarter,
            'end_year': end_year,
            'end_quarter': end_quarter,
        }
        return self.manger.fa.send_request('get', path, params=params)


class StockManager(ManagerBase):
    """
    Manages multiple Stock objects.

    Methods:
        get(symbol):
            Retrieves a Stock object based on the provided symbol.
        get_available_list():
            Retrieves a list of available stocks with their profiles.
    """

    _obj = Stock

    def get(self, symbol: str) -> Stock:
        """
        Retrieves a Stock object based on the provided symbol.

        Parameters:
            symbol (str): The symbol of the stock to retrieve.

        Returns:
            A `Stock` object corresponding to the provided symbol.
        """
        return cast(self._obj, super().get(symbol=symbol))

    def get_available_list(self) -> list[StockProfile]:
        """
        Retrieves a list of available stocks with their profiles.

        Returns:
            A list of `StockProfile` objects containing the profile information of available stocks.
        """
        path = '/stock'
        return self.fa.send_request('get', path)
