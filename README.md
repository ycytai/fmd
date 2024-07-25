# fmd

Provides users with an easy-to-use interface to access data from the *Financial Market Data (FMD)* API, specializing in Taiwan's financial market.

## Installation

Install via `pip`
```
pip install fmd
```

## Quick Start

Retrieve data through `FmdApi` with various predefined methods.
```python
from fmd import FmdApi

fmd_api = FmdApi()
data = fmd_api.get_stock_price(
    symbol='2330',
    start_date='2024-07-01',
    end_date='2024-07-15'
)
```
