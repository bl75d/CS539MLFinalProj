# https://pypi.org/project/yfinance/
# https://pypi.org/project/stock-dataframe/
from Data_stock_dataframe import GetStockData
def AllStocksData():
    symbol_list = ["AAPL"]
    interval_list = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    StockDict={}
    for symbol in symbol_list:
        prd="3y"
        intvl="1d"
        stock=GetStockData(symbol,prd,intvl)
        StockDict[symbol]=stock

    # print(StockDict)
    return StockDict