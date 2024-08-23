import pytest

from fmd import FmdApi
from fmd.resources import ETF, ETFManager


class TestETF:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.symbol = '0050'
        self.api = FmdApi()
        self.etf_manager = ETFManager(self.api)
        self.etf = ETF(symbol=self.symbol, manager=self.etf_manager)
        yield

    @pytest.mark.parametrize(
        ['params'],
        argvalues=[
            pytest.param(
                dict(start_date='2023-01-01', end_date='2023-01-31'),
                id='Data range given',
            ),
            pytest.param(
                dict(start_date=None, end_date=None),
                id='Use default data range',
            ),
        ],
    )
    def test_get_price(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'price_data'}
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        response = self.etf.get_price(start_date=start_date, end_date=end_date)
        mock_fa_send_request.assert_called()
        assert response == {'data': 'price_data'}

    @pytest.mark.parametrize(
        ['params'],
        argvalues=[
            pytest.param(
                dict(start_year=2020, end_year=2024),
                id='Data range given',
            ),
            pytest.param(
                dict(start_year=None, end_year=None),
                id='Use default data range',
            ),
        ],
    )
    def test_get_dividend(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'etf_data'}
        start_year = params.get('start_year')
        end_year = params.get('end_year')

        response = self.etf.get_dividend(start_year=start_year, end_year=end_year)

        mock_fa_send_request.assert_called()
        assert response == {'data': 'etf_data'}


class TestETFManager:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.api = FmdApi()
        self.manager = ETFManager(self.api)
        yield

    def test_get_etf(self, mock_manager_get) -> None:
        symbol = '0050'
        etf = ETF(symbol=symbol, manager=self.manager)
        mock_manager_get.return_value = etf

        result = self.manager.get(symbol=symbol)

        mock_manager_get.assert_called_once_with(symbol=symbol)
        assert result == etf

    def test_get_available_list(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'available_list'}
        response = self.manager.get_available_list()
        mock_fa_send_request.assert_called_once_with('get', '/etf')
        assert response == {'data': 'available_list'}
