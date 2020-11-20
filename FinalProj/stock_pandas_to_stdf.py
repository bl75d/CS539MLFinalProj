''' 
@author Shijing (Iris)
@create date 2020-11-19 13:22:19
'''

import yfinance as yf
import pandas as pd
from stock_pandas import StockDataFrame
import generate_dataframe as gd 
import stock_dataframe_to_stdf as sdts 



def data_processing(stockdf):
    # simple moving average
    stockdf['ma:2']
    stockdf['ma:5']
    stockdf['ma:2,open']
    stockdf['ma:5,open']
    # Exponential Moving Average
    stockdf['ema:5']

    # Moving Average Convergence Divergence
    stockdf['macd:2,3']
    stockdf['macd.s']
    stockdf['macd.h']
    # BOLLinger bands
    stockdf['boll:2,open']
    # Raw Stochastic Value
    stockdf['rsv:2']
    # stochastic oscillator
    stockdf['kdj.d']
    # Relative Strength Index
    stockdf['rsi:2']
    # Bull and Bear Index
    stockdf['bbi']
    # Lowest of Low Values
    stockdf['llv:2,low']
    stockdf['llv:2,close']
    stockdf['llv:5,low']
    stockdf['llv:5,close']
    stockdf['llv:10,low']
    stockdf['llv:10,close']
    # Highest of High Values
    stockdf['hhv:2,low']
    stockdf['hhv:2,close']
    stockdf['hhv:5,low']
    stockdf['hhv:5,close']
    stockdf['hhv:10,low']
    stockdf['hhv:10,close']
    # bullish/bearish
    stockdf['style:bullish']
    # increase
    # has been increasing repeatedly for 3 times (maybe 3 days)
    stockdf['increase:(ma:20,close),3']
    # If the close price has been decreasing repeatedly for 5 times (maybe 5 days)
    stockdf['increase:close,5,-1']

    return stockdf

if __name__ == "__main__":
    data = gd.generate_df("AAPL","1y","1d")
    columns = ['open','close','high','low','volume','amount']
    stockdf = sdts.generate_stdf(data)
    stock = sdts.data_processing(columns,stockdf)
    df = sdts.to_df(stock)
    stockdf = data_processing(StockDataFrame(df))
    print(stockdf.head(5))
    print(stockdf.shape)

