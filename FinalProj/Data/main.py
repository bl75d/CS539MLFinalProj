from AllStocks import AllStocksData

if __name__ == '__main__':
    #return a dictionary of stocks----{stock_symbol:stock_data}
    stocks=AllStocksData()

    for symbol,data in stocks.items():
        print(data)