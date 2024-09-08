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

## Feedback and Bugs Report

Feel free to raise a issue once you found any specious errors or encounter an unknown situation. We cherish your feedback, your insights are invaluable as we continuously strive to improve our service. Fill this [form](https://forms.gle/mv3zY5nkDeupE6zL9) to give your feedback. Cheers.
