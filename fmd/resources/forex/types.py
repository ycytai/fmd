from fmd.backend import JsonDict


class ForexProfile(JsonDict):
    """
    Attributes:
        code (str): Currency code.
        name (str): Name of the forex.
        chinese_name (str): Chinese name of the forex.

    Example:
        ```json
        {
            "code": "EUR",
            "name": "Euro-Area Euro",
            "chinese_name": "歐元"
        }
        ```
    """

    code: str
    name: str
    chinese_name: str


class Rate(JsonDict):
    """
    Attributes:
        AUD (str): Australian Dollar
        BRL (str): Brazilian Real
        CAD (str): Canadian Dollar
        CHF (str): Swiss Franc
        CNY (str): Chinese Yuan
        DKK (str): Danish Krone
        EUR (str): Euro-Area Euro
        GBP (str): United Kingdom Pound
        HKD (str): Hong Kong Dollar
        INR (str): Indian Rupee
        JPY (str): Japanese Yen
        KRW (str): South Korean Won
        LKR (str): Sri Lankan Rupee
        MXN (str): Mexican Peso
        MYR (str): Malaysian Ringgit
        NOK (str): Norwegian Krone
        NZD (str): New Zealand Dollar
        SEK (str): Swedish Krona
        SGD (str): Singapore Dollar
        THB (str): Thailand Baht
        TWD (str): Taiwanese N.T. Dollar
        USD (str): US Dollar
        VEB (str): Venezuelan Bolivar
        ZAR (str): South African Rand

    Example:
        ```json
        {
            "AUD": "1.61707633",
            "BRL": "6.05060000",
            "CAD": "1.43690000",
            "CHF": "0.91390000",
            "CNY": "7.33110000",
            "DKK": "7.24900000",
            "EUR": "0.97162845",
            "GBP": "0.82047916",
            "HKD": "7.78620000",
            "INR": "86.63000000",
            "JPY": "157.95000000",
            "KRW": "1459.50000000",
            "LKR": "294.42000000",
            "MXN": "20.51440000",
            "MYR": "4.50430000",
            "NOK": "11.39470000",
            "NZD": "1.78699071",
            "SEK": "11.19100000",
            "SGD": "1.36770000",
            "THB": "34.70000000",
            "TWD": "32.97000000",
            "USD": "1.00000000",
            "VEB": "53.78490000",
            "ZAR": "18.92980000"
        }
        ```
    """

    AUD: str
    BRL: str
    CAD: str
    CHF: str
    CNY: str
    DKK: str
    EUR: str
    GBP: str
    HKD: str
    INR: str
    JPY: str
    KRW: str
    LKR: str
    MXN: str
    MYR: str
    NOK: str
    NZD: str
    SEK: str
    SGD: str
    THB: str
    TWD: str
    USD: str
    VEB: str
    ZAR: str


class ForexRate(JsonDict):
    """
    Attributes:
        date (str): Date of the forex rate data.
        base_currency (str): Base currency of exchange rate.
        rates (Rate): Exchange rate.


    Example:
        ```json
        {
            "date": "2025-01-14",
            "base_currency": "USD",
            "rates": {
                "AUD": "1.61707633",
                "BRL": "6.05060000",
                "CAD": "1.43690000",
                "CHF": "0.91390000",
                "CNY": "7.33110000",
                "DKK": "7.24900000",
                "EUR": "0.97162845",
                "GBP": "0.82047916",
                "HKD": "7.78620000",
                "INR": "86.63000000",
                "JPY": "157.95000000",
                "KRW": "1459.50000000",
                "LKR": "294.42000000",
                "MXN": "20.51440000",
                "MYR": "4.50430000",
                "NOK": "11.39470000",
                "NZD": "1.78699071",
                "SEK": "11.19100000",
                "SGD": "1.36770000",
                "THB": "34.70000000",
                "TWD": "32.97000000",
                "USD": "1.00000000",
                "VEB": "53.78490000",
                "ZAR": "18.92980000"
            }
        ```
    """

    date: str
    base_currency: str
    rates: Rate
