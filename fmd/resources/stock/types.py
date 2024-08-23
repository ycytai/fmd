from fmd.backend import JsonDict


class StockProfile(JsonDict):
    symbol: str
    name: str
    capital: str
    listed_date: str
    industry: str
    marker_category: str


class StockPrice(JsonDict):
    date: str
    symbol: str
    open: str
    high: str
    low: str
    close: str
    volume: str
    values: str


class ValuationMeasurement(JsonDict):
    date: str
    symbol: str
    pe: str
    pb: str
    yield_rate: str
    financial_report_year: int
    financial_report_quarter: int
    dividend_belongs_year: int


class StockDividend(JsonDict):
    symbol: str
    period: str
    announce_date: str
    cash_dividend_amount: str
    cash_ex_dividend_date: str
    cash_dividend_receive_date: str
    stock_dividend_amount: str
    stock_ex_dividend_date: str | None


class StockCompany(JsonDict):
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
    symbol: str
    year: int
    quarter: int
    gross_profit_margin: str
    operating_profit_margin: str
    pre_tax_net_profit_margin: str
    net_profit_margin: str


class BalanceSheet(JsonDict):
    symbol: str
    year: int
    quarter: int
    asset: str
    capital: str
    equity: str
    liabilities: str


class IncomeStatement(JsonDict):
    symbol: str
    year: int
    quarter: int
    revenue: str
    gross_profit: str
    operating_income: str
    pre_tax_income: str
    net_income: str
