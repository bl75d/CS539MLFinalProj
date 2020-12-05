import numpy as np
import pandas as pd

import yfinance as yf
import stock_pandas as pds

from stock_dataframe import StockDataFrame

from sklearn.preprocessing import MinMaxScaler
from scipy.signal import savgol_filter
from scipy.ndimage.interpolation import shift
from scipy.signal import find_peaks


def get_data(symbol_list=["AAPL"],period="1y",interval="1d"):
    StockDict={}
    LabelDict={}

    for symbol in symbol_list:
        # return raw data--stock and label
        stockdf,labeldf = GetStockData(symbol, period, interval)
        stock = np.asarray(stockdf)
        label = np.asarray(labeldf)

        StockDict[symbol] = stock
        LabelDict[symbol] = label
        
    return StockDict,LabelDict

# request one stock and generating its labels
def GetStockData(ticker,prd,intvl,use_more_data=False):
    rawdata = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers = ticker,

            # use "period" instead of start/end
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            # (optional, default is '1mo')
            # period = "ytd",
            period = prd,

            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            # (optional, default is '1d')
            interval = intvl,

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
    # print(type(data))
    # data=pd.DataFrame(data)

    stockdf=StockDataFrame.retype(pd.DataFrame(data))
    # for additional features in stock-pandas

    stock=stockdf[['open','close','high','low','volume','amount']]
    # stock['rsi_6']=stockdf['rsi_6']

    # Add stock technical indicators to the dataframe
    # ******************************************
    # volume delta against previous day
    stock['volume_delta']=stockdf['volume_delta']

    # open delta against next 2 day
    stock['open_2_d']=stockdf['open_2_d']

    # open price change (in percent) between today and the day before yesterday
    # 'r' stands for rate.
    stock['open_-2_r']=stockdf['open_-2_r']

    # CR indicator, including 5, 10, 20 days moving average
    stock['cr']=stockdf['cr']
    stock['cr-ma1']=stockdf['cr-ma1']
    stock['cr-ma2']=stockdf['cr-ma2']
    stock['cr-ma3']=stockdf['cr-ma3']

    # volume max of three days ago, yesterday and two days later
    stock['volume_-3,2,-1_max']=stockdf['volume_-3,2,-1_max']

    # volume min between 3 days ago and tomorrow
    stock['volume_-3~1_min']=stockdf['volume_-3~1_min']

    # KDJ, default to 9 days
    stock['kdjk']=stockdf['kdjk']
    stock['kdjd']=stockdf['kdjd']
    stock['kdjj']=stockdf['kdjj']

    # three days KDJK cross up 3 days KDJD
    # stock['kdj_3_xu_kdjd_3']=stockdf['kdj_3_xu_kdjd_3']

    # 2 days simple moving average on open price
    stock['open_2_sma']=stockdf['open_2_sma']

    # MACD
    stock['macd']=stockdf['macd']

    # MACD signal line
    stock['macds']
    # MACD histogram
    stock['macdh']=stockdf['macdh']

    # bolling, including upper band and lower band
    stock['boll']=stockdf['boll']
    stock['boll_ub']=stockdf['boll_ub']
    stock['boll_lb']=stockdf['boll_lb']

    # # close price less than 10.0 in 5 days count
    # stock['close_10.0_le_5_c']=stockdf['close_10.0_le_5_c']
    #
    # # CR MA2 cross up CR MA1 in 20 days count
    # stock['cr-ma2_xu_cr-ma1_20_c']=stockdf['cr-ma2_xu_cr-ma1_20_c']
    #
    # # count forward(future) where close price is larger than 10
    # stock['close_10.0_ge_5_fc']=stockdf['close_10.0_ge_5_fc']

    # 6 days RSI
    stock['rsi_6']=stockdf['rsi_6']

    # 12 days RSI
    stock['rsi_12']=stockdf['rsi_12']

    # 10 days WR
    stock['wr_10']=stockdf['wr_10']

    # 6 days WR
    stock['wr_6']=stockdf['wr_6']

    # CCI, default to 14 days
    stock['cci']=stockdf['cci']

    # 20 days CCI
    stock['cci_20']=stockdf['cci_20']

    # TR (true range)
    stock['tr']=stockdf['tr']

    # ATR (Average True Range)
    stock['atr']=stockdf['atr']

    # DMA, difference of 10 and 50 moving average
    stock['dma']=stockdf['dma']

    # DMI
    # +DI, default to 14 days
    stock['pdi']=stockdf['pdi']

    # -DI, default to 14 days
    stock['mdi']=stockdf['mdi']

    # DX, default to 14 days of +DI and -DI
    stock['dx']=stockdf['dx']
    # ADX, 6 days SMA of DX, same as stock['dx_6_ema']
    stock['adx']=stockdf['adx']
    # ADXR, 6 days SMA of ADX, same as stock['adx_6_ema']
    stock['adxr']=stockdf['adxr']

    # TRIX, default to 12 days
    stock['trix']=stockdf['trix']

    # TRIX based on the close price for a window of 3
    stock['close_3_trix']=stockdf['close_3_trix']

    # MATRIX is the simple moving average of TRIX
    stock['trix_9_sma']=stockdf['trix_9_sma']
    # TEMA, another implementation for triple ema
    stock['tema']=stockdf['tema']

    # TEMA based on the close price for a window of 2

    stock['close_2_tema']=stockdf['close_2_tema']

    # VR, default to 26 days
    stock['vr']=stockdf['vr']

    # MAVR is the simple moving average of VR
    stock['vr_6_sma']=stockdf['vr_6_sma']


    # *****************************
    # add stock-pandas.StockDataframe features
    pdseries = pds.StockDataFrame(data)

    if use_more_data:
        stock['ma:2']=pdseries['ma:2']
        stock['ma:5']=pdseries['ma:5']
        stock['ma:2,open']=pdseries['ma:2,open']
        stock['ma:5,open']=pdseries['ma:5,open']
        # Exponential Moving Average
        stock['ema:5']=pdseries['ema:5']

        # Moving Average Convergence Divergence
        stock['macd:2,3']=pdseries['macd:2,3']
        stock['macd.s']=pdseries['macd.s']
        stock['macd.h']=pdseries['macd.h']
        # BOLLinger bands
        stock['boll:2,open']=pdseries['boll:2,open']
        # Raw Stochastic Value
        stock['rsv:2']=pdseries['rsv:2']
        # stochastic oscillator
        # Relative Strength Index
        # Bull and Bear Index
        stock['bbi']=pdseries['bbi']
        # Lowest of Low Values
        stock['llv:2,low']=pdseries['llv:2,low']
        stock['llv:2,close']=pdseries['llv:2,close']
        stock['llv:5,low']=pdseries['llv:5,low']
        stock['llv:5,close']=pdseries['llv:5,close']
        stock['llv:10,low']=pdseries['llv:10,low']
        stock['llv:10,close']=pdseries['llv:10,close']
        # Highest of High Values
        stock['hhv:2,low']=pdseries['hhv:2,low']
        stock['hhv:2,close']=pdseries['hhv:2,close']
        stock['hhv:5,low']=pdseries['hhv:5,low']
        stock['hhv:5,close']=pdseries['hhv:5,close']
        stock['hhv:10,low']=pdseries['hhv:10,low']
        stock['hhv:10,close']=pdseries['hhv:10,close']

    stock['style:bullish']=pdseries['style:bullish']*1

    if use_more_data:
        stock['increase:(ma:20,close),3']=pdseries['increase:(ma:20,close),3']*1

    # naive label
    # stock['label']=stockdf['rsi_6']//10
    # stock['label'] =stock['label'].fillna(method='ffill')
    # stock['label']=stock['label'].fillna(0)


    # fulfill missing values
    # stock['macd']=stock['macd'].fillna(method='ffill')
    # stock['macd']=stock['macd'].fillna(0)

    stock = stock.fillna(method='bfill')
    stock = stock.fillna(0)

    # Generate labels
    # label=get_naive_label(stock)
    # label=generate_label(stock)
    label = generate_pct_label(stock)
    stock=stock.drop(columns='label',axis=1)
    return stock,label

def generate_pct_label(stock):
    adj_price= np.asarray(stock['amount'] / stock['volume'])
    price_change_pct=(shift(adj_price, -1)-adj_price)/adj_price

    n_median=np.median(price_change_pct[price_change_pct<0])
    p_median=np.median(price_change_pct[price_change_pct>0])
    # print(n_median)
    # print(p_median)
    stock['label'] = 1
    for i in range(price_change_pct.shape[0] - 1):
            if (price_change_pct[i] >= p_median):
                    stock['label'].iloc[i] = 2
            elif (price_change_pct[i] <= n_median):
                    stock['label'].iloc[i] = 0
    label = stock['label']

    # _ = plt.hist(label)
    # plt.title("Distribution of labels")
    # plt.show()

    # occurrences0 = np.count_nonzero(label == 0)
    # occurrences1 = np.count_nonzero(label == 1)
    # occurrences2 = np.count_nonzero(label == 2)
    # print(occurrences0)
    # print(occurrences1)
    # print(occurrences2)

    return label