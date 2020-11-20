''' 
@author Shijing (Iris)
@create date 2020-11-19 18:24:27
'''

import yfinance as yf
import pandas as pd

def generate_df(company,period,interval):
    rawdata = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers = company,

            # use "period" instead of start/end
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            # (optional, default is '1mo')
            # period = "ytd",
            period=period,

            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            # (optional, default is '1d')
            interval = interval,

            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
            group_by = 'ticker',

            # adjust all OHLC automatically
            # (optional, default is False)
            # auto_adjust = True,

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
    rawdata['Amount']=rawdata['Adj Close']*rawdata['Volume']
    rawdata.columns=['open','high','low','close','adj','volume','amount']
    data=rawdata[['open','close','high','low','volume','amount']]
    return data


def main():
    df = generate_df("AAPL","1y","1d")
    print(df.head())


if __name__ == "__main__":
    # main()
    pass