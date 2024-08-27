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
