# https://pypi.org/project/yfinance/
# https://pypi.org/project/stock-dataframe/
from Data_stock_dataframe import GetStockData
from stock_pandas import StockDataFrame
import generate_dataframe as gd
import stock_dataframe_to_stdf as sdts
from stock_pandas_to_stdf import data_processing
import generate_label as lbl

def AllStocksData():
    symbol_list = ["AAPL"]
    # symbol_list = ["AAPL","TSLA","AMZN"]
    interval_list = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    StockDict={}
    LabelDict={}
    for symbol in symbol_list:
        prd="3y"
        intvl="1d"
        data = gd.generate_df(symbol,prd,intvl)
        columns = ['open', 'close', 'high', 'low', 'volume', 'amount']
        stockdf = sdts.generate_stdf(data)
        stock = sdts.data_processing(columns, stockdf)
        df = sdts.to_df(stock)
        stockdf = data_processing(StockDataFrame(df))
        # df = sdts.to_df(stockdf)
        # df.to_excel("./Shijing_try/data_v1.xlsx", engine="xlsxwriter")
        StockDict[symbol]=stockdf

        # label: macd based,w/o ris criteria
        # Label=lbl.get_label(stockdf)
        Label=lbl.get_naive_label(stockdf)
        # print(stockdf.shape)
        # print(Label)
        LabelDict[symbol]=Label
    return StockDict,LabelDict