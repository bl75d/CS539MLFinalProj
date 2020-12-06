from Processing import DataBrick,SplitData,DataPipeline,DataBrick,GetclosePrice
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import matplotlib.pyplot as plt
from NAV import Nav,Generate_nav

if __name__ == '__main__':
    symbol_list = ["TSLA"]
    # symbol_list = ["AAPL","TSLA","AMZN","GOOG","FB","NIO","BYND","FSLY","MRNA","BABA","BLNK"]
    # interval_list = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    # period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    period = "5y"
    interval = "1d"

    #size of databrick(eg.10days/hours as a databrick for training)
    size=10

    # return a dictionary of stocks, and a dictionary of labels----{stock_symbol:stock_data;label symbol:label_data}
    StockDict, LabelDict=DataPipeline(symbol_list,period,interval)

    # get price list for testing set to calculate NAV
    StockPriceDic=GetclosePrice(symbol_list,period,interval,size)

    for symbol in StockDict:
        stock=StockDict[symbol]
        label=LabelDict[symbol]
        X_train, X_test, y_train, y_test=SplitData(stock,label,size)

        # X,y=DataBrick(stock,label,size)
        # Code for running the model for each stock
        # print(X_train.shape)
        # print(y_train.shape)



        # create and fit the LSTM network
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
        model.add(Dropout(0.1))
        model.add(LSTM(units=50, return_sequences=True))
        model.add(Dropout(0.1))
        model.add(LSTM(units=25, return_sequences=True))
        model.add(Dropout(0.1))
        # model.add(LSTM(units=50))
        # model.add(Dropout(0.1))
        model.add(Dense(units=1,activation='softmax'))
        model.compile(optimizer='adam', loss='mean_squared_error',metrics=['accuracy'])

        history = model.fit(X_train, y_train, epochs=300, batch_size=32)
        print(model.summary())

        results=model.evaluate(X_test,y_test,batch_size=32)
        print("test loss, test acc:", results)
        # summarize history for accuracy
        plt.plot(history.history['accuracy'],label='Train')
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
        prediction=model.predict(X_test)
        print(prediction)
        print(y_test)

        # history = model.fit(X, y, validation_split=0.1,shuffle=False,epochs=300, batch_size=32)
        # print(model.summary())
        # # summarize history for accuracy
        # plt.plot(history.history['accuracy'])
        # plt.plot(history.history['val_accuracy'])
        # plt.ylabel('accuracy')
        # plt.xlabel('epoch')
        # plt.legend(['train', 'test'], loc='upper left')
        # plt.show()
        # prediction=model.predict(X_test)
        # print(prediction)
        # print(y_test)

        # get price list for testing set to calculate NAV
        NAV_history=Generate_nav(10000,StockPriceDic,symbol,prediction)