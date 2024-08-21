from fmd.backend import JsonDict


class EtfDividend(JsonDict):
    symbol: str
    name: str
    ex_dividend_date: str
    dividend_based_date: str
    dividend_receive_date: str
    dividend_amount: str | None
    announce_year: int
