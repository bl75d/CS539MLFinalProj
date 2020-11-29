from AllStocks import AllStocksData

if __name__ == '__main__':
    #return a dictionary of stocks, and a dictionary of labels----{stock_symbol:stock_data;label symbol:label_data}
    stocks,labels=AllStocksData()
    for symbol,data in stocks.items():
        print(data.shape)
        print(labels[symbol].shape)