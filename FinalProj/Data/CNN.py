from numpy import mean
from numpy import std
from matplotlib import pyplot
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from Processing import DataBrick,SplitData,DataPipeline,DataBrick,GetclosePrice
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import matplotlib.pyplot as plt
import math
from NAV import Nav,Generate_nav

def create_CNN(data):
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(data.shape[1], data.shape[2], data.shape[3])))
	model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(3, activation='softmax'))
	# compile model
	opt = SGD(lr=0.01, momentum=0.9)
	model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
	return model


def expand_dim(data,size):
    newdata=[]
    pic_dim=int(math.sqrt(size))
    for i in range(data.shape[0]):
        pic=[]
        for j in range(pic_dim):
            row=[]
            for k in range(pic_dim):
                row.append(data[i,pic_dim*j+k,:])
            pic.append(row)
        newdata.append(pic)
    newdata=np.asarray(newdata)
    return newdata

def run_CNN(X_train, X_test, y_train, y_test,size,symbol,price):

    # reshape the input data to n_instances * n * n * features
    X_train = expand_dim(X_train, size)
    X_test = expand_dim(X_test, size)
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    CNN=create_CNN(X_train)

    hist = CNN.fit(X_train, y_train, epochs=100, batch_size=10)
    _, acc = CNN.evaluate(X_test, y_test, verbose=0)
    print('> %.3f' % (acc * 100.0))
    prediction = CNN.predict(X_test)
    y_prediction = np.argmax(prediction, axis=1)
    print(y_prediction)
    # plot NAV
    NAV_history = Generate_nav(10000, symbol, price, y_prediction)

# if __name__ == '__main__':
#     symbol_list = ["AAPL"]
#     # symbol_list = ["AAPL","TSLA","AMZN","GOOG","FB","NIO","BYND","FSLY","MRNA","BABA","BLNK"]
#     # interval_list = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
#     # period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
#     period = "10y"
#     interval = "1d"
#
#     #size of databrick(eg.10days/hours as a databrick for training)
#     size=49
#
#     # return a dictionary of stocks, and a dictionary of labels----{stock_symbol:stock_data;label symbol:label_data}
#     StockDict, LabelDict=DataPipeline(symbol_list,period,interval)
#
#     # get price list for testing set to calculate NAV
#     StockPriceDic=GetclosePrice(symbol_list,period,interval,size)
#
#     for symbol in symbol_list:
#         stock=StockDict[symbol]
#         label=LabelDict[symbol]
#         X_train, X_test, y_train, y_test=SplitData(stock,label,size)
#
#         # X,y=DataBrick(stock,label,size)
#         # Code for running the model for each stock
#
#         X_train=expand_dim(X_train,size)
#         X_test=expand_dim(X_test,size)
#         y_train = to_categorical(y_train)
#         y_test = to_categorical(y_test)
#         print(X_train.shape)
#         print(y_train.shape)
#         # create and fit the CNN
#         CNN=create_CNN(X_train)
#         hist=CNN.fit(X_train,y_train,epochs=100, batch_size=10)
#         _, acc = CNN.evaluate(X_test, y_test, verbose=0)
#         print('> %.3f' % (acc * 100.0))
#         prediction=CNN.predict(X_test)
#         # print(prediction)
#         print(prediction.shape)
#         y_prediction=np.argmax(prediction, axis = 1)
#         print(y_prediction)
#
#
#
#
#
#         # get price list for testing set to calculate NAV
#         # prediction=model.predict(X_test)
#         # y_prediction=prediction[:,-1,:]
#         # print(y_prediction)
#         # print(y_test)
#         # NAV_history=Generate_nav(10000,symbol,StockPriceDic,y_test)
#         NAV_history=Generate_nav(10000,symbol,StockPriceDic,y_prediction)