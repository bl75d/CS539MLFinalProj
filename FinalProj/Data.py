# https://pypi.org/project/yfinance/
import yfinance as yf
import pandas as pd
from stock_pandas import StockDataFrame
import mplfinance as mpf
import numpy as np
data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "SPY",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        # period = "ytd",
        period="2y",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1d",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

stock=StockDataFrame(data)
# print(stock)
stock.alias('open','Open')
stock.alias('high','High')
stock.alias('low','Low')
stock.alias('close','Close')
print(stock)
cross_up_upper = stock['high'].copy()

# `cross_up_upper` is the series of high prices each of which cross up the upper bollinger band.
cross_up_upper[
    ~ stock['column:high > boll.upper']
] = np.nan
# Set some items of the series to `np.nan` so that mplfinance will not draw markers for those items.

cross_down_lower = stock['low'].copy()

cross_down_lower[
    ~ stock['column:low < boll.lower']
] = np.nan

apds = [
        mpf.make_addplot(
                stock[
                        [
                                # The middle band
                                'boll',

                                # The upper band
                                # The default period of bollinger bands is 20 days.
                                # However, we could specify arguments for a command after `:`.
                                'boll.upper:30',

                                # The lower band
                                # Which is a short cut for 'boll.lower'
                                'boll.lower:30'
                        ]
                ]
        ),
        mpf.make_addplot(cross_up_upper, scatter=True, markersize=200, marker='v'),
        mpf.make_addplot(cross_down_lower, scatter=True, markersize=200, marker='^'),
]

# Go plotting! Oh yeah!
mpf.plot(stock, type='candle', addplot=apds, figscale=2)


# msft = yf.Ticker("MSFT")
#
# # get stock info
# msft.info
# print(msft.history(period="1mo"))