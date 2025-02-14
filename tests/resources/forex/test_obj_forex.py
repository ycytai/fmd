import pytest

from fmd import FmdApi
from fmd.resources import Forex, ForexManager


class TestForex:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.currency = 'TWD'
        self.api = FmdApi()
        self.forex_manager = ForexManager(self.api)
        self.forex = Forex(currency=self.currency, manager=self.forex_manager)
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
    def test_get_rate(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'price_data'}
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        response = self.forex.get_rate(start_date=start_date, end_date=end_date)
        mock_fa_send_request.assert_called()
        assert response == {'data': 'price_data'}

    def test_get_profile(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'profile_data'}

        response = self.forex.get_profile()

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/forex/{self.currency}/profile',
        )
        assert response == {'data': 'profile_data'}


class TestForexManager:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.api = FmdApi()
        self.manager = ForexManager(self.api)
        yield

    def test_get_forex(self, mock_manager_get) -> None:
        currency = 'TWD'
        forex = Forex(currency=currency, manager=self.manager)
        mock_manager_get.return_value = forex

        result = self.manager.get(currency=currency)

        mock_manager_get.assert_called_once_with(currency=currency)
        assert result == forex

    def test_get_available_list(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'available_list'}
        response = self.manager.get_available_list()
        mock_fa_send_request.assert_called_once_with('get', '/forex')
        assert response == {'data': 'available_list'}
