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

    def test_get_dividend(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'dividend_data'}
        start_year = 2022
        end_year = 2023

        response = self.stock.get_dividend(start_year=start_year, end_year=end_year)

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/stock/{self.symbol}/dividend',
            params={'start_year': start_year, 'end_year': end_year},
        )
        assert response == {'data': 'dividend_data'}

    def test_get_company(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'company_data'}

        response = self.stock.get_company()

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/stock/{self.symbol}/company',
        )
        assert response == {'data': 'company_data'}

    def test_get_revenue(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'revenue_data'}
        start_year = 2022
        start_month = 1
        end_year = 2023
        end_month = 12

        response = self.stock.get_revenue(
            start_year=start_year, start_month=start_month, end_year=end_year, end_month=end_month
        )

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/stock/{self.symbol}/revenue',
            params={
                'start_year': start_year,
                'start_month': start_month,
                'end_year': end_year,
                'end_month': end_month,
            },
        )
        assert response == {'data': 'revenue_data'}

    def test_get_financial_ratio(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'financial_ratio_data'}
        start_year = 2022
        start_quarter = 1
        end_year = 2023
        end_quarter = 4

        response = self.stock.get_financial_ratio(
            start_year=start_year,
            start_quarter=start_quarter,
            end_year=end_year,
            end_quarter=end_quarter,
        )

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/stock/{self.symbol}/financial-ratio',
            params={
                'start_year': start_year,
                'start_quarter': start_quarter,
                'end_year': end_year,
                'end_quarter': end_quarter,
            },
        )
        assert response == {'data': 'financial_ratio_data'}

    def test_get_balance_sheet(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'balance_sheet_data'}
        start_year = 2022
        start_quarter = 1
        end_year = 2023
        end_quarter = 4

        response = self.stock.get_balance_sheet(
            start_year=start_year,
            start_quarter=start_quarter,
            end_year=end_year,
            end_quarter=end_quarter,
        )

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/stock/{self.symbol}/balance-sheet',
            params={
                'start_year': start_year,
                'start_quarter': start_quarter,
                'end_year': end_year,
                'end_quarter': end_quarter,
            },
        )
        assert response == {'data': 'balance_sheet_data'}

    def test_get_income_statement(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'income_statement_data'}
        start_year = 2022
        start_quarter = 1
        end_year = 2023
        end_quarter = 4

        response = self.stock.get_income_statement(
            start_year=start_year,
            start_quarter=start_quarter,
            end_year=end_year,
            end_quarter=end_quarter,
        )

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/stock/{self.symbol}/income-statement',
            params={
                'start_year': start_year,
                'start_quarter': start_quarter,
                'end_year': end_year,
                'end_quarter': end_quarter,
            },
        )
        assert response == {'data': 'income_statement_data'}


class TestStockManager:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.api = FmdApi()
        self.manager = StockManager(self.api)
        yield

    def test_get_stock(self, mock_manager_get) -> None:
        symbol = '2330'
        stock = Stock(symbol=symbol, manager=self.manager)
        mock_manager_get.return_value = stock

        result = self.manager.get(symbol=symbol)

        mock_manager_get.assert_called_once_with(symbol=symbol)
        assert result == stock

    def test_get_available_list(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'available_list'}
        response = self.manager.get_available_list()
        mock_fa_send_request.assert_called_once_with('get', '/stock')
        assert response == {'data': 'available_list'}
