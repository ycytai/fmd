# fmd

**fmd** is a python wrapper that provides users with an easy-to-use interface to access data from Financial Market Data (FMD) API, specializing in Taiwan's financial market.

**Source Code**: [https://github.com/ycytai/fmd](https://github.com/ycytai/fmd)

**Documentation**: [https://fmd.ycytai.com/](https://fmd.ycytai.com/)

## Features

- :smile: **User-friendly**: Intuitive interface for easy adoption by all skill levels.
- :chart_with_upwards_trend: **Diverse data**: Popular financial data including prices, dividends, and more.
- :package: **All JSON**: Streamlined data format for effortless integration and analysis.

## Installation

Just use `pip`
```
pip install fmd
```

## Quick Start

Retrieve data with various predefined resources.

```python
from fmd import FmdApi

fa = FmdApi()
stock = fa.stock.get(symbol='2330')
data = stock.get_price()
```
