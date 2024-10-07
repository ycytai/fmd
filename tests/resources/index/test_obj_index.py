import pytest

from fmd import FmdApi
from fmd.resources import Index, IndexManager


class TestIndex:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.symbol = 'LI0001'
        self.api = FmdApi()
        self.index_manager = IndexManager(self.api)
        self.index = Index(symbol=self.symbol, manager=self.index_manager)
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

        response = self.index.get_price(start_date=start_date, end_date=end_date)
        mock_fa_send_request.assert_called()
        assert response == {'data': 'price_data'}

    def test_get_profile(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'profile_data'}

        response = self.index.get_profile()

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/index/{self.symbol}/profile',
        )
        assert response == {'data': 'profile_data'}


class TestIndexManager:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.api = FmdApi()
        self.manager = IndexManager(self.api)
        yield

    def test_get_index(self, mock_manager_get) -> None:
        symbol = '0050'
        index = Index(symbol=symbol, manager=self.manager)
        mock_manager_get.return_value = index

        result = self.manager.get(symbol=symbol)

        mock_manager_get.assert_called_once_with(symbol=symbol)
        assert result == index

    def test_get_available_list(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'available_list'}
        response = self.manager.get_available_list()
        mock_fa_send_request.assert_called_once_with('get', '/index')
        assert response == {'data': 'available_list'}
