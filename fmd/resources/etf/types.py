from fmd.backend import JsonDict


class ETFPrice(JsonDict):
    date: str
    symbol: str
    open: str
    high: str
    low: str
    close: str
    volume: str
    values: str


class ETFDividend(JsonDict):
    symbol: str
    name: str
    ex_dividend_date: str
    dividend_based_date: str
    dividend_receive_date: str
    dividend_amount: str | None
    announce_year: int


class ETFProfile(JsonDict):
    name: str
    symbol: str
    category: str
    listed_date: str
    issuer: str
    underlying_index: str
