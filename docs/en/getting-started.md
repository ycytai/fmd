## Basic Usage

After initializing API, you can access various resources. Below is a simple example of retrieving stock prices.
```python
from fmd import FmdApi

fa = FmdApi()
stock = fa.stock.get(symbol='2330')
data = stock.get_price()
```

More get data methods can be found in [Stock](/reference/stock/#fmd.resources.stock.obj.Stock).

**Note**: All data is returned in JSON format, which is automatically converted to a `dict`.

## Find Available Symbols

To find out what stock information is available, use  [`get_available_list()`](/reference/stock/#fmd.resources.stock.obj.StockManager.get_available_list)

```python
from fmd import FmdApi

fa = FmdApi()
stock_profiles = fa.stock.get_available_list()
```

Apply the same approach to retrieve [`ETF`](/reference/etf) information.

```python
from fmd import FmdApi

fa = FmdApi()
etf_profiles = fa.etf.get_available_list()
```

## Working with `pandas`

Data results can be easily integrated with `pandas` and converted into a `DataFrame` for further manipulation
```python
from fmd import FmdApi
import pandas as pd

fa = FmdApi()
stock = fa.stock.get('2330')
price = stock.get_price()

df = pd.DataFrame(price)
df.head()
```

Since most data fields are of `str` type, you may want to convert them to `float` for analysis or visualization.

```python

...

df = df.astype({
    'date': 'datetime64[ns]',
    'open': 'float',
    'high': 'float',
    'low': 'float',
    'close': 'float',
    'volume': 'float',
    'values': 'float',
})
df = df.set_index('date')
df['close'].plot()
```
