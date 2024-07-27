# fmd

Provides users with an easy-to-use interface to access data from the *Financial Market Data (FMD)* API, specializing in Taiwan's financial market.

## Installation

Install via `pip`
```
pip install fmd
```

## Quick Start

Retrieve data through `FmdApi` with various predefined resources.
```python
from fmd import FmdApi

fa = FmdApi()
stock = fa.stock.get(symbol='2330')
data = stock.get_price()
```
