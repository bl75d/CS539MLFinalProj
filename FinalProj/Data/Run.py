from Processing import DataBrick,SplitData,DataPipeline,DataBrick,GetclosePrice
from CNN import  run_CNN
from simple_LSTM import run_LSTM
if __name__ == '__main__':
    symbol_list = ["AAPL"]
    period = "2y"
    interval = "1d"
    #size of databrick(eg.10days/hours as a databrick for training)
    size=36
    # return a dictionary of stocks, and a dictionary of labels----{stock_symbol:stock_data;label symbol:label_data}
    StockDict, LabelDict=DataPipeline(symbol_list,period,interval)

    # get price list for testing set to calculate NAV
    StockPriceDic=GetclosePrice(symbol_list,period,interval,size)

    for symbol in symbol_list:
        X_train, X_test, y_train, y_test=SplitData(StockDict[symbol],LabelDict[symbol],size)


        # CNN-------size must be 4,9,16,36,49.........for CNN
        # go to CNN.py to change settings for CNN
        # run_CNN(X_train, X_test, y_train, y_test,size,symbol,StockPriceDic[symbol])

        # LSTM
        # run_LSTM(X_train, X_test, y_train, y_test,symbol,StockPriceDic[symbol])