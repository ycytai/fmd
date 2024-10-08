import pytest

from fmd import FmdApi
from fmd.resources import Stock, StockManager


class TestStock:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.symbol = '2330'
        self.api = FmdApi()
        self.stock_manager = StockManager(self.api)
        self.stock = Stock(symbol=self.symbol, manager=self.stock_manager)
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

        response = self.stock.get_price(start_date=start_date, end_date=end_date)

        mock_fa_send_request.assert_called()
        assert response == {'data': 'price_data'}

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
    def test_get_vm(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'vm_data'}
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        response = self.stock.get_vm(start_date=start_date, end_date=end_date)

        mock_fa_send_request.assert_called()
        assert response == {'data': 'vm_data'}

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
        mock_fa_send_request.return_value = {'data': 'dividend_data'}
        start_year = params.get('start_year')
        end_year = params.get('end_year')

        response = self.stock.get_dividend(start_year=start_year, end_year=end_year)

        mock_fa_send_request.assert_called()
        assert response == {'data': 'dividend_data'}

    def test_get_company(self, mock_fa_send_request) -> None:
        mock_fa_send_request.return_value = {'data': 'company_data'}

        response = self.stock.get_company()

        mock_fa_send_request.assert_called_once_with(
            'get',
            f'/stock/{self.symbol}/company',
        )
        assert response == {'data': 'company_data'}

    @pytest.mark.parametrize(
        ['params'],
        argvalues=[
            pytest.param(
                dict(start_year=2022, start_month=1, end_year=2023, end_month=12),
                id='Data range given',
            ),
            pytest.param(
                dict(start_year=None, start_month=None, end_year=None, end_month=None),
                id='Use default data range',
            ),
        ],
    )
    def test_get_revenue(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'revenue_data'}
        start_year = params.get('start_year')
        start_month = params.get('start_month')
        end_year = params.get('end_year')
        end_month = params.get('end_month')

        response = self.stock.get_revenue(
            start_year=start_year, start_month=start_month, end_year=end_year, end_month=end_month
        )

        mock_fa_send_request.assert_called()
        assert response == {'data': 'revenue_data'}

    @pytest.mark.parametrize(
        ['params'],
        argvalues=[
            pytest.param(
                dict(start_year=2022, start_quarter=1, end_year=2023, end_quarter=4),
                id='Data range given',
            ),
            pytest.param(
                dict(start_year=None, start_quarter=None, end_year=None, end_quarter=None),
                id='Use default data range',
            ),
        ],
    )
    def test_get_financial_ratio(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'financial_ratio_data'}
        start_year = params.get('start_year')
        start_quarter = params.get('start_quarter')
        end_year = params.get('end_year')
        end_quarter = params.get('end_quarter')

        response = self.stock.get_financial_ratio(
            start_year=start_year,
            start_quarter=start_quarter,
            end_year=end_year,
            end_quarter=end_quarter,
        )

        mock_fa_send_request.assert_called()
        assert response == {'data': 'financial_ratio_data'}

    @pytest.mark.parametrize(
        ['params'],
        argvalues=[
            pytest.param(
                dict(start_year=2022, start_quarter=1, end_year=2023, end_quarter=4),
                id='Data range given',
            ),
            pytest.param(
                dict(start_year=None, start_quarter=None, end_year=None, end_quarter=None),
                id='Use default data range',
            ),
        ],
    )
    def test_get_balance_sheet(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'balance_sheet_data'}
        start_year = params.get('start_year')
        start_quarter = params.get('start_quarter')
        end_year = params.get('end_year')
        end_quarter = params.get('end_quarter')

        response = self.stock.get_balance_sheet(
            start_year=start_year,
            start_quarter=start_quarter,
            end_year=end_year,
            end_quarter=end_quarter,
        )

        mock_fa_send_request.assert_called()
        assert response == {'data': 'balance_sheet_data'}

    @pytest.mark.parametrize(
        ['params'],
        argvalues=[
            pytest.param(
                dict(start_year=2022, start_quarter=1, end_year=2023, end_quarter=4),
                id='Data range given',
            ),
            pytest.param(
                dict(start_year=None, start_quarter=None, end_year=None, end_quarter=None),
                id='Use default data range',
            ),
        ],
    )
    def test_get_income_statement(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'income_statement_data'}
        start_year = params.get('start_year')
        start_quarter = params.get('start_quarter')
        end_year = params.get('end_year')
        end_quarter = params.get('end_quarter')

        response = self.stock.get_income_statement(
            start_year=start_year,
            start_quarter=start_quarter,
            end_year=end_year,
            end_quarter=end_quarter,
        )

        mock_fa_send_request.assert_called()
        assert response == {'data': 'income_statement_data'}

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
    def test_get_margin_balance(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'margin_balance_data'}
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        response = self.stock.get_margin_balance(start_date=start_date, end_date=end_date)

        mock_fa_send_request.assert_called()
        assert response == {'data': 'margin_balance_data'}

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
    def test_get_institution_trade_summary(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'institution_trade_summary'}
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        response = self.stock.get_institution_trade_summary(
            start_date=start_date, end_date=end_date
        )
        mock_fa_send_request.assert_called()
        assert response == {'data': 'institution_trade_summary'}

    @pytest.mark.parametrize(
        ['params'],
        argvalues=[
            pytest.param(
                dict(start_year=2022, start_quarter=1, end_year=2023, end_quarter=4),
                id='Data range given',
            ),
            pytest.param(
                dict(start_year=None, start_quarter=None, end_year=None, end_quarter=None),
                id='Use default data range',
            ),
        ],
    )
    def test_get_cash_flow_statement(self, mock_fa_send_request, params) -> None:
        mock_fa_send_request.return_value = {'data': 'cash_flow_statement'}
        start_year = params.get('start_year')
        start_quarter = params.get('start_quarter')
        end_year = params.get('end_year')
        end_quarter = params.get('end_quarter')

        response = self.stock.get_cash_flow_statement(
            start_year=start_year,
            start_quarter=start_quarter,
            end_year=end_year,
            end_quarter=end_quarter,
        )

        mock_fa_send_request.assert_called()
        assert response == {'data': 'cash_flow_statement'}


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
