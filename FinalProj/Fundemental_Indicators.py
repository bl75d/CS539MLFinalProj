# https://pypi.org/project/yfinance/
# https://pypi.org/project/stock-pandas/
import yfinance as yf
import pandas as pd
from stock_pandas import StockDataFrame
msft = yf.Ticker("MSFT")

# get stock info
msft.info
print(msft.info)

# get historical market data
hist = msft.history(period="ytd")
