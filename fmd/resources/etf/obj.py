from datetime import date
from typing import cast

from fmd.base import ManagerBase, ObjectBase
from fmd.decorators import default_data_range
from fmd.resources.etf.types import (
    ETFDividend,
    ETFInstitutionTradeSummary,
    ETFMarginBalance,
    ETFPrice,
    ETFProfile,
)


class ETF(ObjectBase):
    """
    Represents an Exchange Traded Fund (ETF).

    Example:
        ```python
        from fmd import FmdApi

        fa = FmdApi()
        etf = fa.etf.get(symbol='0050')
        ```

    Attributes:
        symbol (str): The symbol of the ETF.

    Methods:
        get_price(start_date, end_date):
            Retrieves the price data for the ETF within the specified date range.
        get_dividend(start_year, end_year):
            Retrieves the dividend data for the ETF within the specified year range.
    """

    @default_data_range(freq='daily', days=30)
    def get_price(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[ETFPrice]:
        """
        Retrieves the price data for the ETF within the specified date range.
        Default data range is last 30 days.

        Parameters:
            start_date (str | date | None): The start date for the price data.
            end_date (str | date | None): The end date for the price data.

        Returns:
            A list of `ETFPrice` objects containing price information.
        """
        path = f'/etf/{self.symbol}/price'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='yearly', years=3)
    def get_dividend(
        self, start_year: int | None = None, end_year: int | None = None
    ) -> list[ETFDividend]:
        """
        Retrieves the dividend data for the ETF within the specified year range.
        Default data range is last 3 years.

        Parameters:
            start_year (int | None): The start year for the dividend data.
            end_year (int | None): The end year for the dividend data.

        Returns:
            A list of `ETFDividend` objects containing dividend information.
        """
        path = f'/etf/{self.symbol}/dividend'
        params = {'start_year': start_year, 'end_year': end_year}
        return self.manger.fa.send_request('get', path, params=params)

    def get_profile(self) -> ETFProfile:
        """
        Retrieves the profile for the ETF.

        Returns:
            A `ETFProfile` object containing the profile information of the ETF.
        """
        path = f'/etf/{self.symbol}/profile'
        return self.manger.fa.send_request('get', path)

    @default_data_range(freq='daily', days=30)
    def get_margin_balance(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[ETFMarginBalance]:
        """
        Retrieves the margin balance data for the ETF within the specified date range.
        Default data range is last 30 days.

        Parameters:
            start_date (str | date | None): The start date for data.
            end_date (str | date | None): The end date for data.

        Returns:
            A list of `ETFMarginBalance` objects containing margin balance information.
        """
        path = f'/etf/{self.symbol}/margin-balance'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    @default_data_range(freq='daily', days=30)
    def get_institution_trade_summary(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[ETFInstitutionTradeSummary]:
        """
        Retrieves the institution trade summary for the ETF within the specified date range.
        Default data range is last 30 days.

        Parameters:
            start_date (str | date | None): The start date for data.
            end_date (str | date | None): The end date for data.

        Returns:
            A list of `ETFInstitutionTradeSummary` objects containing institutions trade summary.
        """
        path = f'/etf/{self.symbol}/institution-trade-summary'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)


class ETFManager(ManagerBase):
    """
    Manages multiple ETF objects.

    Methods:
        get(symbol):
            Retrieves an ETF object based on the provided symbol.
        get_available_list():
            Retrieves a list of available ETFs with their profiles.
    """

    _obj = ETF

    def get(cls, symbol: str) -> ETF:
        """
        Retrieves an ETF object based on the provided symbol.

        Parameters:
            symbol (str): The symbol of the ETF to retrieve.

        Returns:
            An ETF object corresponding to the provided symbol.
        """
        return cast(cls._obj, super().get(symbol=symbol))

    def get_available_list(self) -> list[ETFProfile]:
        """
        Retrieves a list of available ETFs with their profiles.

        Returns:
            A list of `ETFProfile` objects containing the profile information of available ETFs.
        """
        path = '/etf'
        return self.fa.send_request('get', path)
