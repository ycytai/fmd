from unittest.mock import MagicMock

import pytest

from fmd import FmdApi
from fmd.objs import Stock, StockManager


class TestStock:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.symbol = '2330'
        self.api = FmdApi()
        self.stock_manager = StockManager(self.api)
        self.stock = Stock(symbol=self.symbol, manager=self.stock_manager)
        yield

    def test_get_price(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'price_data'}
        start_date = '2023-01-01'
        end_date = '2023-01-31'

        response = self.stock.get_price(start_date=start_date, end_date=end_date)

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/stock/{self.symbol}/price',
            params={'start_date': start_date, 'end_date': end_date},
        )
        assert response == {'data': 'price_data'}

    def test_get_vm(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'vm_data'}
        start_date = '2023-01-01'
        end_date = '2023-01-31'

        response = self.stock.get_vm(start_date=start_date, end_date=end_date)

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/stock/{self.symbol}/vm',
            params={'start_date': start_date, 'end_date': end_date},
        )
        assert response == {'data': 'vm_data'}


class TestStockManager:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.api = MagicMock(spec=FmdApi)
        self.manager = StockManager(self.api)
        yield

    def test_get_stock(self, mock_manager_get) -> None:
        symbol = '2330'
        stock = Stock(symbol=symbol, manager=self.manager)
        mock_manager_get.return_value = stock

        result = self.manager.get(symbol=symbol)

        mock_manager_get.assert_called_once_with(symbol=symbol)
        assert result == stock
