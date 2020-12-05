from Processing import DataBrick,SplitData,DataPipeline,Scale
import numpy as np
if __name__ == '__main__':
    symbol_list = ["AAPL"]
    # symbol_list = ["AAPL","TSLA","AMZN","GOOG","FB"]
    # interval_list = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    # period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]

    period = "1y"
    interval = "1d"
    #size of databrick(eg.10days/hours as a databrick for training)
    size=10

    # return a dictionary of stocks, and a dictionary of labels----{stock_symbol:stock_data;label symbol:label_data}
    StockDict, LabelDict=DataPipeline(symbol_list,period,interval)

    for symbol in StockDict:
        stock=StockDict[symbol]
        label=LabelDict[symbol]
        X_train, X_test, y_train, y_test=SplitData(stock,label,size)

        # Code for running the model for each stock
        print(X_train.shape)
        print(y_train.shape)




