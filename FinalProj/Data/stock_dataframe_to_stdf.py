# https://pypi.org/project/yfinance/
# https://pypi.org/project/stock-dataframe/
import yfinance as yf
import pandas as pd
from stock_dataframe import StockDataFrame
import generate_dataframe as gd 

def df_to_stdf(df):
    stockdf=StockDataFrame.retype(df)
    return stockdf


def data_processing(columns,stockdf):
    stock=stockdf[columns]

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

    # close price less than 10.0 in 5 days count
    stock['close_10.0_le_5_c']=stockdf['close_10.0_le_5_c']

    # CR MA2 cross up CR MA1 in 20 days count
    stock['cr-ma2_xu_cr-ma1_20_c']=stockdf['cr-ma2_xu_cr-ma1_20_c']

    # count forward(future) where close price is larger than 10
    stock['close_10.0_ge_5_fc']=stockdf['close_10.0_ge_5_fc']

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

    return stock

def to_df(stock_df):
    df = pd.DataFrame(stock_df)
    return df

def generate_stdf(data):
    stockdf=StockDataFrame.retype(pd.DataFrame(data))
    return stockdf

# if __name__ == "__main__":
#     data = gd.generate_df("AAPL","1y","1d")
#     stockdf= generate_stdf(data)
#     columns = ['open','close','high','low','volume','amount']
#     stock = data_processing(columns,stockdf)
#     print(stock.head())
#     # print(stock.shape)
#     # print(type(stock))
#     df = to_df(stock)
#     print(type(df))