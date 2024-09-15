from fmd.backend import JsonDict


class ETFPrice(JsonDict):
    """
    Attributes:
        date (str): Date of the etf price data.
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
            'symbol': '0050',
            'open': '181.80',
            'high': '182.00',
            'low': '179.95',
            'close': '180.60',
            'volume': '10574343.00',
            'values': '1915739406.00'
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


class ETFDividend(JsonDict):
    """
    Attributes:
        symbol (str): ETF symbol.
        name (str): Name of the ETF.
        ex_dividend_date (str): Date on which the ETF begins trading without the dividend.
        dividend_based_date (str): Date based on which the dividend is calculated.
        dividend_receive_date (str): Date on which the dividend is received by the holder.
        dividend_amount (str | None): Amount of the dividend; can be None if not applicable.
        announce_year (int): Year in which the dividend was announced.

    Example:
        ```json
        {
            'symbol': '0050',
            'name': '元大台灣50',
            'ex_dividend_date': '2021-01-22',
            'dividend_based_date': '2021-01-30',
            'dividend_receive_date': '2021-03-09',
            'dividend_amount': '3.05',
            'announce_year': 2021
        }
        ```
    """

    symbol: str
    name: str
    ex_dividend_date: str
    dividend_based_date: str
    dividend_receive_date: str
    dividend_amount: str | None
    announce_year: int


class ETFProfile(JsonDict):
    """
    Attributes:
        name (str): Name of the ETF.
        symbol (str): Symbol used to identify the ETF.
        category (str): Category which the ETF belongs.
        listed_date (str): Date when the ETF was listed.
        issuer (str): Company that issues the ETF.
        underlying_index (str): Index that the ETF aims to track or replicate.

    Example:
        ```json
        {
            'name': '元大台灣50',
            'symbol': '0050',
            'category': '國內成分股ETF',
            'listed_date': '2003-06-30',
            'issuer': '元大證券投資信託股份有限公司',
            'underlying_index': '富時臺灣證券交易所臺灣50指數'
        }
        ```
    """

    name: str
    symbol: str
    category: str
    listed_date: str
    issuer: str
    underlying_index: str


class ETFMarginBalance(JsonDict):
    """
    Attributes:
        date (str): Date of the margin balance data.
        symbol (str): ETF symbol.
        margin_buy (int): Total amount of margin buying.
        margin_sell (int): Total amount of margin selling.
        margin_cash_repayment (int): Cash repayment amount for margin accounts.
        today_margin_balance (int): Current margin balance for the day.
        margin_limit_for_next_day (int): Margin limit available for the next trading day.
        short_sale_buy (int): Total amount of short sale buying.
        short_sale_sell (int): Total amount of short sale selling.
        short_sale_stock_repayment (int): Number of stocks repaid in short sales.
        today_short_sale_balance (int): Current balance of short sales for the day.
        short_sale_limit_for_next_day (int): Limit on short sales for the next trading day.
        short_sale_and_margin_offset (int): Offset combining short sales and margin balances.

    Example:
        ```json
        {
            "date": "2024-08-30",
            "symbol": "0050",
            "margin_buy": 36,
            "margin_sell": 101,
            "margin_cash_repayment": 0,
            "today_margin_balance": 1346,
            "margin_limit_for_next_day": 544375,
            "short_sale_buy": 4,
            "short_sale_sell": 13,
            "short_sale_stock_repayment": 0,
            "today_short_sale_balance": 254,
            "short_sale_limit_for_next_day": 544375,
            "short_sale_and_margin_offset": 0
        }
        ```
    """

    date: str
    symbol: str
    margin_buy: int
    margin_sell: int
    margin_cash_repayment: int
    today_margin_balance: int
    margin_limit_for_next_day: int
    short_sale_buy: int
    short_sale_sell: int
    short_sale_stock_repayment: int
    today_short_sale_balance: int
    short_sale_limit_for_next_day: int
    short_sale_and_margin_offset: int


class ETFInstitutionTradeSummary(JsonDict):
    """
    Attributes:
        date (str): Date of the margin balance data.
        symbol (str): ETF symbol.
        foreign_dealer_net (int): Net buy/sell amount by foreign dealers.
        proprietary_net (int): Net buy/sell amount by proprietary firms.
        security_investment_trust_net (int): Net buy/sell amount by security investment trusts.
        sum_of_net (int): Total net buy/sell amount.

    Example:
        ```json
        {
            "date": "2024-08-30",
            "symbol": "0050",
            "foreign_dealer_net": -2393566,
            "proprietary_net": 66457,
            "security_investment_trust_net": 113000,
            "sum_of_net": -2214109
        }
        ```
    """

    date: str
    symbol: str
    foreign_dealer_net: int
    proprietary_net: int
    security_investment_trust_net: int
    sum_of_net: int
