## 基本使用

初始化 API 後，可以存取各種資源。下方是一個簡單的範例，用於取得股票價格。
```python
from fmd import FmdApi

fa = FmdApi()
stock = fa.stock.get(symbol='2330')
data = stock.get_price()
```

更多的資料取得方法可參考[Stock](/reference/stock/#fmd.resources.stock.obj.Stock).

**注意**: 所有資料均以 JSON 格式回傳，意即將自動轉換為 `dict`。

## 找出提供的股票代號

要查找可用的股票資訊，可以使用[`get_available_list()`](/reference/stock/#fmd.resources.stock.obj.StockManager.get_available_list)

```python
from fmd import FmdApi

fa = FmdApi()
stock_profiles = fa.stock.get_available_list()
```

同樣的方式也適用於[`ETF`](/reference/etf)。

```python
from fmd import FmdApi

fa = FmdApi()
etf_profiles = fa.etf.get_available_list()
```

## 搭配`pandas`使用

資料結果可以輕鬆與 `pandas` 整合，並轉換為 `DataFrame` 後再進一步操作。
```python
from fmd import FmdApi
import pandas as pd

fa = FmdApi()
stock = fa.stock.get('2330')
price = stock.get_price()

df = pd.DataFrame(price)
df.head()
```

大多數資料欄位是 `str` 類型 ，可能需要將它們轉換為 `float` 以便進行分析或視覺化。

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
