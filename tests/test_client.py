import pytest

from fmd.client import FmdApi


class TestFmdApi:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.api = FmdApi()
        yield

    def test_init(self):
        assert self.api.base_url == 'https://fmarketdata.com/api/'

    def test_get_stock_price(self, mock_get_data, mock_get_daily_data_params):
        symbol, start_date, end_date = mock_get_daily_data_params
        self.api.get_stock_price(symbol, start_date, end_date)
        mock_get_data.assert_called_with(
            f'{self.api.base_url}v1/stock/{symbol}/price', start_date=start_date, end_date=end_date
        )

    def test_get_stock_vm(self, mock_get_data, mock_get_daily_data_params):
        symbol, start_date, end_date = mock_get_daily_data_params
        self.api.get_stock_vm(symbol, start_date, end_date)
        mock_get_data.assert_called_with(
            f'{self.api.base_url}v1/stock/{symbol}/vm', start_date=start_date, end_date=end_date
        )
