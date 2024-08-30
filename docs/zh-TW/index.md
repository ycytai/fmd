# fmd

**fmd** 是一個 Python Wrapper，提供用戶簡單的使用介面從 FMD API 獲取數據，專注於臺灣的金融市場相關資料。

**程式碼**: [https://github.com/ycytai/fmd](https://github.com/ycytai/fmd)

**文件**: [https://fmd.ycytai.com/](https://fmd.ycytai.com/)

## 特色

- :smile: **使用者友好**: 直覺的設計，從入門到進階的開發者都適合。
- :chart_with_upwards_trend: **多樣化數據**: 包括股票價格、股利等熱門金融數據。
- :package: **全都是JSON**: 簡單的資料格式，方便進行各種整合與分析。

## 安裝

直接用 `pip`
```
pip install fmd
```

## 快速入門

使用多種預先定義好的方式來取得資料。

```python
from fmd import FmdApi

fa = FmdApi()
stock = fa.stock.get(symbol='2330')
data = stock.get_price()
```
