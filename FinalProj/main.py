from Data.AllStocks import AllStocksData
import model as mdl
from Models.LSTM import LSTM_Model
from sklearn.model_selection import TimeSeriesSplit
import numpy as np
from Data.Processing import preprocessing
if __name__ == '__main__':
    #return a dictionary of stocks, and a dictionary of labels----{stock_symbol:stock_data;label symbol:label_data}
    stocks,labels=AllStocksData()
    for symbol in stocks:
        # print(stocks[symbol])
        X=stocks[symbol]
        print(X)
        y=labels[symbol].tolist()
        # Minmax Scaler
        X=preprocessing(X)


        # # split data into training and testing set
        # tscv = TimeSeriesSplit()
        # for train_index, test_index in tscv.split(X):
        #     print("TRAIN:", train_index, "TEST:", test_index)
        #     X_train, X_test = X[train_index], X[test_index]
        #     y_train, y_test = y[train_index], y[test_index]

        train_ind = int(len(X) * 0.8)
        X_train = X[:train_ind]
        X_test=X[train_ind:]
        y_train=y[:train_ind]
        y_test=y[train_ind:]

        print(X_train)
        print(y_train)

        # model= mdl.create_model(model_class=LSTM_Model,
        # #                              # **kwargs
        # )
        # # # modelpath="./model_checkpoint/"
        # # mdl.load_trained(model, modelpath)
        # mdl.compile_model(model)
        # mdl.train(model, np.asarray(X_train), np.asarray(y_train), directory="model_checkpoint/")
        # res=mdl.evaluate(model, np.asarray(X_test), np.asarray(y_test))
        # print(mdl.summary)