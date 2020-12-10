''' 
@author Shijing (Iris)
@create date 2020-11-19 13:22:19
'''

import yfinance as yf
import pandas as pd
from stock_pandas import StockDataFrame
import generate_dataframe as gd 
import stock_dataframe_to_stdf as sdts 
from sklearn import preprocessing


def data_processing(stockdf):
    # bullish/bearish
    stockdf['style:bullish']
    return stockdf


def feature_engineering(df):
    df = df.fillna(0)
    df = df.replace(float('inf'),0)
    isBullish = df["style:bullish"].apply(lambda x: 1 if x == True else 0)
    df.drop(columns=['close_10.0_le_5_c','cr-ma2_xu_cr-ma1_20_c','cr-ma2_xu_cr-ma1_20_c','style:bullish'],inplace=True)
    df['isBullish'] = isBullish
    return df 
    

if __name__ == "__main__":
    data = gd.generate_df("AAPL","1y","1d")
    columns = ['open','close','high','low','volume','amount']
    stockdf = sdts.generate_stdf(data)
    stock = sdts.data_processing(columns,stockdf)
    df = sdts.to_df(stock)
    stockdf = data_processing(StockDataFrame(df))
    df = sdts.to_df(stockdf)
    # print(df.where(df.isnull()==True,0))
    # print(stockdf.head(5))
    # print(stockdf.shape)
    print(feature_engineering(df).shape)
    # df.to_excel("./Shijing_try/data_v2.xlsx",engine="xlsxwriter")


