from fmd.backend import JsonDict


class IndexProfile(JsonDict):
    """
    Attributes:
        symbol (str): Index symbol.
        name (str): Name of the index.
        issued_date (str): Issued date of the index.
        base_date (str): Base date of the index.
        base_date_price (str): Base date price of the index.

    Example:
        ```json
        {
            "symbol": "LI0001",
            "name": "發行量加權股價指數",
            "issued_date": "1970-11-02",
            "base_date": null,
            "base_date_price": "100.00"
        }
        ```
    """

    symbol: str
    name: str
    capital: str
    listed_date: str
    industry: str
    marker_category: str


class IndexPrice(JsonDict):
    """
    Attributes:
        date (str): Date of the index price data.
        symbol (str): Index symbol.
        open (str): Opening price.
        high (str): Highest price.
        low (str): Lowest price.
        close (str): Closing price.
        volume (str): Trading volume.
        values (str): Additional trade values.

    Example:
        ```json
        {
            "date": "2024-08-23",
            "symbol": "LI0001",
            "open": "22148.83",
            "high": "22159.27",
            "low": "21935.98",
            "close": "22158.05",
            "volume": "8158257464.00",
            "values": "314491168746.00"
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
