import pytest

from fmd import FmdApi
from fmd.resources import Etf, EtfManager


class TestEtf:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.symbol = '0050'
        self.api = FmdApi()
        self.etf_manager = EtfManager(self.api)
        self.etf = Etf(symbol=self.symbol, manager=self.etf_manager)
        yield

    def test_get_price(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'price_data'}
        start_date = '2023-01-01'
        end_date = '2023-01-31'

        response = self.etf.get_price(start_date=start_date, end_date=end_date)

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/etf/{self.symbol}/price',
            params={'start_date': start_date, 'end_date': end_date},
        )
        assert response == {'data': 'price_data'}

    def test_get_dividend(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'etf_data'}
        start_year = 2020
        end_year = 2024

        response = self.etf.get_dividend(start_year=start_year, end_year=end_year)

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/etf/{self.symbol}/dividend',
            params={'start_year': start_year, 'end_year': end_year},
        )
        assert response == {'data': 'etf_data'}


class TestEtfManager:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.api = FmdApi()
        self.manager = EtfManager(self.api)
        yield

    def test_get_etf(self, mock_manager_get) -> None:
        symbol = '0050'
        etf = Etf(symbol=symbol, manager=self.manager)
        mock_manager_get.return_value = etf

        result = self.manager.get(symbol=symbol)

        mock_manager_get.assert_called_once_with(symbol=symbol)
        assert result == etf

    def test_get_available_list(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'available_list'}
        response = self.manager.get_available_list()
        mock_fa_send_request.assert_called_once_with('get', '/etf')
        assert response == {'data': 'available_list'}
