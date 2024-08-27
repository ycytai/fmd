from fmd.backend import JsonDict


class StockProfile(JsonDict):
    """
    Attributes:
        symbol (str): Stock symbol.
        name (str): Name of the stock.
        capital (str): Total capital.
        listed_date (str): Date when the stock was listed.
        industry (str): Industry to which the stock belongs.
        marker_category (str): Marker category for the stock.

    Example:
        ```json
        {
            'symbol': '1101',
            'name': '台泥',
            'capital': '77511817420.00',
            'listed_date': '1962-02-09',
            'industry': '水泥工業',
            'market_category': '上市'
        }
        ```
    """

    symbol: str
    name: str
    capital: str
    listed_date: str
    industry: str
    marker_category: str


class StockPrice(JsonDict):
    """
    Attributes:
        date (str): Date of the stock price data.
        symbol (str): Stock symbol.
        open (str): Opening price.
        high (str): Highest price.
        low (str): Lowest price.
        close (str): Closing price.
        volume (str): Trading volume.
        values (str): Additional trade values.

    Example:
        ```json
        {
            'date': '2024-07-29',
            'symbol': '2330',
            'open': '942.00',
            'high': '948.00',
            'low': '936.00',
            'close': '944.00',
            'volume': '44000914.00',
            'values': '41481319942.00'
        }
        ```
    """

    date: str
    symbol: str
    open: str
    high: str
    low: str
    close: str
    volume: str
    values: str


class ValuationMeasurement(JsonDict):
    """
    Attributes:
        date (str): Date of the valuation measurement.
        symbol (str): Stock symbol.
        pe (str): Price-to-earnings ratio.
        pb (str): Price-to-book ratio.
        yield_rate (str): Dividend yield rate.
        financial_report_year (int): Year of the financial report.
        financial_report_quarter (int): Quarter of the financial report.
        dividend_belongs_year (int): Year to which the dividend belongs.

    Example:
        ```json
        {
            'date': '2024-07-26',
            'symbol': '2330',
            'pe': '27.97',
            'pb': '6.59',
            'yield_rate': '1.41',
            'financial_report_year': 2024,
            'financial_report_quarter': 1,
            'dividend_belongs_year': 2023
        }
        ```
    """

    date: str
    symbol: str
    pe: str
    pb: str
    yield_rate: str
    financial_report_year: int
    financial_report_quarter: int
    dividend_belongs_year: int


class StockDividend(JsonDict):
    """
    Attributes:
        symbol (str): Stock symbol.
        period (str): Dividend period.
        announce_date (str): Date of the dividend announcement.
        cash_dividend_amount (str): Amount of cash dividend.
        cash_ex_dividend_date (str): Ex-dividend date for cash dividends.
        cash_dividend_receive_date (str): Date on which cash dividend is received.
        stock_dividend_amount (str): Amount of stock dividend.
        stock_ex_dividend_date (str | None): Ex-dividend date for stock dividends; can be None if not applicable.

    Example:
        ```json
        {
            'symbol': '2330',
            'period': '2021Q1',
            'announce_date': '2021-06-09',
            'cash_dividend_amount': '2.75',
            'cash_ex_dividend_date': '2021-09-16',
            'cash_dividend_receive_date': '2021-10-14',
            'stock_dividend_amount': '0.00',
            'stock_ex_dividend_date': null
        }
        ```
    """

    symbol: str
    period: str
    announce_date: str
    cash_dividend_amount: str
    cash_ex_dividend_date: str
    cash_dividend_receive_date: str
    stock_dividend_amount: str
    stock_ex_dividend_date: str | None


class StockCompany(JsonDict):
    """
    Attributes:
        symbol (str): Stock symbol.
        chinese_name (str): Chinese name of the company.
        chairman (str): Name of the chairman.
        president (str): Name of the president.
        capital (str): Total capital.
        listed_date (str): Date when the stock was listed.
        company_url (str): URL of the company's website.
        industry (str): Industry to which the company belongs.
        market_category (str): Market category of the stock.

    Example:
        ```json
        {
            'symbol': '2330',
            'chinese_name': '台積電',
            'chairman': '魏哲家',
            'president': '總裁: 魏哲家',
            'capital': '259336292420.00',
            'listed_date': '1994-09-05',
            'company_url': 'https://www.tsmc.com',
            'industry': '半導體業',
            'market_category': '上市'
        }
        ```
    """

    symbol: str
    chinese_name: str
    chairman: str
    president: str
    capital: str
    listed_date: str
    company_url: str
    industry: str
    market_category: str


class Revenue(JsonDict):
    """
    Attributes:
        year (int): Year of the revenue data.
        month (int): Month of the revenue data.
        symbol (str): Stock symbol.
        revenue (str): Revenue amount.
        revenue_last_month (str): Revenue of the previous month.
        revenue_last_year_month (str): Revenue of the same month last year.
        revenue_mom (str): Month-over-month revenue change.
        revenue_yoy (str): Year-over-year revenue change.
        cum_revenue (str): Cumulative revenue.
        cum_revenue_last_year_month (str): Cumulative revenue of the same month last year.
        cum_revenue_yoy (str): Year-over-year cumulative revenue change.

    Example:
        ```json
        {
            'year': 2024,
            'month': 2,
            'symbol': '2330',
            'revenue': '181648270.00',
            'revenue_last_month': '215785127.00',
            'revenue_last_year_month': '163174097.00',
            'revenue_mom': '-15.82',
            'revenue_yoy': '11.32',
            'cum_revenue': '397433397.00',
            'cum_revenue_last_year_month': '363224641.00',
            'cum_revenue_yoy': '9.42'
        }
        ```
    """

    year: int
    month: int
    symbol: str
    revenue: str
    revenue_last_month: str
    revenue_last_year_month: str
    revenue_mom: str
    revenue_yoy: str
    cum_revenue: str
    cum_revenue_last_year_month: str
    cum_revenue_yoy: str


class FinancialRatio(JsonDict):
    """
    Attributes:
        symbol (str): Stock symbol.
        year (int): Year of the financial ratio data.
        quarter (int): Quarter of the financial ratio data.
        gross_profit_margin (str): Gross profit margin.
        operating_profit_margin (str): Operating profit margin.
        pre_tax_net_profit_margin (str): Pre-tax net profit margin.
        net_profit_margin (str): Net profit margin.

    Example:
        ```json
        {
            'symbol': '2330',
            'year': 2022,
            'quarter': 3,
            'gross_profit_margin': '60.43',
            'operating_profit_margin': '50.61',
            'pre_tax_net_profit_margin': '51.65',
            'net_profit_margin': '45.82'
        }
        ```
    """

    symbol: str
    year: int
    quarter: int
    gross_profit_margin: str
    operating_profit_margin: str
    pre_tax_net_profit_margin: str
    net_profit_margin: str


class BalanceSheet(JsonDict):
    """
    Attributes:
        symbol (str): Stock symbol.
        year (int): Year of the balance sheet data.
        quarter (int): Quarter of the balance sheet data.
        asset (str): Total assets.
        capital (str): Total capital.
        equity (str): Total equity.
        liabilities (str): Total liabilities.

    Example:
        ```json
        {
            'symbol': '2330',
            'year': 2022,
            'quarter': 3,
            'asset': '4643301766.00',
            'capital': '259303805.00',
            'equity': '2752316159.00',
            'liabilities': '1890985607.00'
        }
        ```
    """

    symbol: str
    year: int
    quarter: int
    asset: str
    capital: str
    equity: str
    liabilities: str


class IncomeStatement(JsonDict):
    """
    Attributes:
        symbol (str): Stock symbol.
        year (int): Year of the income statement data.
        quarter (int): Quarter of the income statement data.
        revenue (str): Total revenue.
        gross_profit (str): Gross profit.
        operating_income (str): Operating income.
        pre_tax_income (str): Pre-tax income.
        net_income (str): Net income.

    Example:
        ```json
        {
            'symbol': '2330',
            'year': 2022,
            'quarter': 3,
            'revenue': '613142743.00',
            'gross_profit': '370498717.00',
            'operating_income': '310324214.00',
            'pre_tax_income': '316690867.00',
            'net_income': '280968407.00'
        }
        ```
    """

    symbol: str
    year: int
    quarter: int
    revenue: str
    gross_profit: str
    operating_income: str
    pre_tax_income: str
    net_income: str
