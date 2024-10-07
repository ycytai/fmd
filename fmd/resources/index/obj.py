from datetime import date
from typing import cast

from fmd.base import ManagerBase, ObjectBase
from fmd.decorators import default_data_range
from fmd.resources.index.types import IndexPrice, IndexProfile


class Index(ObjectBase):
    """
    Represents a index.

    Example:
        ```python
        from fmd import FmdApi

        fa = FmdApi()
        index = fa.index.get(symbol='LI0001')
        ```

    Attributes:
        symbol (str): The symbol of the index.

    Methods:
        get_price(start_date, end_date):
            Retrieves the price data for the index within the specified date range.
        get_profile():
            Retrieves the profile information of the index.
    """

    @default_data_range(freq='daily', days=30)
    def get_price(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[IndexPrice]:
        """
        Retrieves the price data for the index within the specified date range.
        Default data range is last 30 days.

        Parameters:
            start_date (str | date | None): The start date for the price data.
            end_date (str | date | None): The end date for the price data.

        Returns:
            A list of `IndexPrice` objects containing price information.
        """
        path = f'/index/{self.symbol}/price'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    def get_profile(self) -> IndexProfile:
        """
        Retrieves the profile for the index.

        Returns:
            A `IndexProfile` object containing the profile information of the index.
        """
        path = f'/index/{self.symbol}/profile'
        return self.manger.fa.send_request('get', path)


class IndexManager(ManagerBase):
    """
    Manages multiple Index objects.

    Methods:
        get(symbol):
            Retrieves a Index object based on the provided symbol.
        get_available_list():
            Retrieves a list of available indexs with their profiles.
    """

    _obj = Index

    def get(self, symbol: str) -> Index:
        """
        Retrieves a Index object based on the provided symbol.

        Parameters:
            symbol (str): The symbol of the index to retrieve.

        Returns:
            A `Index` object corresponding to the provided symbol.
        """
        return cast(self._obj, super().get(symbol=symbol))

    def get_available_list(self) -> list[IndexProfile]:
        """
        Retrieves a list of available indexs with their profiles.

        Returns:
            A list of `IndexProfile` objects containing the profile information of available indexs.
        """
        path = '/index'
        return self.fa.send_request('get', path)
