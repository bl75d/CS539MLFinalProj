# https://pypi.org/project/yfinance/
# https://pypi.org/project/stock-dataframe/
# from Data_stock_dataframe import GetStockData
from stock_pandas import StockDataFrame
import generate_dataframe as gd
import stock_dataframe_to_stdf as sdts
import stock_pandas_to_stdf as spts
import Data.generate_label as lbl
import pandas as pd

def AllStocksData():
    symbol_list = ["TSLA"]
    # symbol_list = ["AAPL","TSLA","AMZN","GOOG","FB"]
    interval_list = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    StockDict={}
    LabelDict={}

    for symbol in symbol_list:
        prd="1y"
        intvl="1h"
        data = gd.generate_df(symbol,prd,intvl)
        columns = ['open', 'close', 'high', 'low', 'volume', 'amount']
        stockdf = sdts.generate_stdf(data)
        stock = sdts.data_processing(columns, stockdf)
        df = sdts.to_df(stock)
        stockdf = spts.data_processing(StockDataFrame(df))

        # stockdf is a pandas dataframe
        stockdf=pd.DataFrame(stockdf)
        # fulfill missing values
        stockdf = stockdf.fillna(method='ffill')
        stockdf = stockdf.fillna(0)
        # print(stock.isnull().sum())
        stockdf[['style:bullish']] = stockdf[['style:bullish']] * 1
        # df.to_excel("./Shijing_try/data_v1.xlsx", engine="xlsxwriter")
        StockDict[symbol]=stockdf

        # Generate labels: macd based,w/o ris criteria
        # Label=lbl.get_label(stockdf)
        Label=lbl.get_naive_label(stockdf)
        # print(stockdf.shape)
        # print(Label)
        LabelDict[symbol]=Label
    return StockDict,LabelDict