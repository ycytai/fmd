from datetime import date
from typing import cast

from fmd.base import ManagerBase, ObjectBase
from fmd.decorators import default_data_range
from fmd.resources.forex.types import ForexProfile, ForexRate


class Forex(ObjectBase):
    """
    Represents a currency.

    Example:
        ```python
        from fmd import FmdApi

        fa = FmdApi()
        forex = fa.forex.get(currency='TWD')
        ```

    Attributes:
        currency (str): The currency of the forex.

    Methods:
        get_rate(start_date, end_date):
            Retrieves the rates for the currency within the specified date range.
        get_profile():
            Retrieves the profile information of the currency.
    """

    @default_data_range(freq='daily', days=30)
    def get_rate(
        self, start_date: str | date | None = None, end_date: str | date | None = None
    ) -> list[ForexRate]:
        """
        Retrieves the rates for the currency within the specified date range.
        Default data range is last 30 days.

        Parameters:
            start_date (str | date | None): The start date for the rates data.
            end_date (str | date | None): The end date for the rates data.

        Returns:
            A list of `ForexRate` objects containing rates information.
        """
        path = f'/forex/{self.currency}/rate'
        params = {'start_date': start_date, 'end_date': end_date}
        return self.manger.fa.send_request('get', path, params=params)

    def get_profile(self) -> ForexProfile:
        """
        Retrieves the profile for the currency.

        Returns:
            A `ForexProfile` object containing the profile information of the forex.
        """
        path = f'/forex/{self.currency}/profile'
        return self.manger.fa.send_request('get', path)


class ForexManager(ManagerBase):
    """
    Manages multiple Forex objects.

    Methods:
        get(currency):
            Retrieves a Forex object based on the provided currency.
        get_available_list():
            Retrieves a list of available forex with their profiles.
    """

    _obj = Forex

    def get(self, currency: str) -> Forex:
        """
        Retrieves a Forex object based on the provided currency.

        Parameters:
            currency (str): The currency of the forex to retrieve.

        Returns:
            A `Forex` object corresponding to the provided currency.
        """
        return cast(self._obj, super().get(currency=currency))

    def get_available_list(self) -> list[ForexProfile]:
        """
        Retrieves a list of available currencies with their profiles.

        Returns:
            A list of `ForexProfile` objects containing the profile information of available currencies.
        """
        path = '/forex'
        return self.fa.send_request('get', path)
