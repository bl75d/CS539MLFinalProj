# Jingfeng Xia
# jxia@wpi.edu

# !pip install sklearn
# !pip install yfinance
# !pip install tensorflow
# !pip install keras

import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras import optimizers
from keras.optimizers import SGD

def GetStockData(ticker,prd,intvl):
        rawdata = yf.download(  # or pdr.get_data_yahoo(...
                # tickers list or string as well
                tickers = ticker,

                # use "period" instead of start/end
                # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                # (optional, default is '1mo')
                # period = "ytd",
                period = prd,

                # fetch data by interval (including intraday if period < 60 days)
                # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                # (optional, default is '1d')
                interval = intvl,

                # group by ticker (to access via data['SPY'])
                # (optional, default is 'column')
                group_by = 'ticker',

                # adjust all OHLC automatically
                # (optional, default is False)
                # auto_adjust = True,

                # download pre/post regular market hours data
                # (optional, default is False)
                prepost = True,

                # use threads for mass downloading? (True/False/Integer)
                # (optional, default is True)
                threads = True,

                # proxy URL scheme use use when downloading?
                # (optional, default is None)
                proxy = None
            )
        return rawdata

rawdata=GetStockData("AAPL","max","1d")
# rawdata.head(6)

# filename may change for difference cases
rawdata.to_csv("AAPL_max_1d.csv",index=False,sep=',')

# read csv file to save time
rawdata = np.genfromtxt("AAPL_max_1d.csv", delimiter=',', skip_header=True)

data = np.ones(shape=(rawdata.shape[0],2))
# data[:,0] = rawdata.iloc[:,3] # for pd.dataframe, if not using csv
data[:,0] = rawdata[:,3]

def labeling(data,width):
    for i in range(data.shape[0]-1):
        if width*data[i,0]<data[i+1,0]: # buy
            data[i,-1]=2
        elif data[i,0]>width*data[i+1,0]: # sell
            data[i,-1]=0
        else:
            pass
    return data

ldata = np.ones(data.shape)
ldata = labeling(data[0:-1,:],1.006)
# print(ldata[:50,:],ldata.shape)
# type(ldata)
# print(np.count_nonzero(ldata[:,1] == 0))
# print(np.count_nonzero(ldata[:,1] == 1))
# print(np.count_nonzero(ldata[:,1] == 2))

# 1.007: 634 1059 824
# 1.006: 699 928 890
# 1.005: 774 784 959

def blocknlabel(data):
    block = np.zeros((data.shape[0]-12*21,12,21))
    label = np.ones((data.shape[0]-12*21,1))
    for i in range(data.shape[0]-12*21): # reshape into a block.shape=(12,21) 
        block[i] = data[i:i+12*21,0].reshape(12,21)
        label[i] = data[i+12*21,1]
    return block,label

datablock = np.zeros((data.shape[0]-12*21,12,21))
datalabel = np.ones((data.shape[0]-12*21,1))
datablock,datalabel = blocknlabel(ldata)

X_train, X_test, y_train, y_test = \
train_test_split(datablock, datalabel, test_size=0.3, random_state=1206)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
y_train = np.squeeze(tf.one_hot(y_train,3))
y_test = np.squeeze(tf.one_hot(y_test,3))
# y_train = y_train.reshape(y_train,shape[0],3)
# y_test = y_test.reshape(y_test,shape[0],3)
X_train = X_train.reshape(X_train.shape[0],12,21,1)
X_test = X_test.reshape(X_test.shape[0],12,21,1)
print(X_train.shape)
print(y_train.shape)


#build the model
model = Sequential()
model.add(Conv2D(64,3,strides=1,input_shape=(12,21,1),\
                 padding='same',activation='relu'))

# keras.layers.convolutional.Conv2D(filters, kernel_size, strides=(1, 1), \
# padding='valid', data_format=None, dilation_rate=(1, 1), activation=None, \
# use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', \
# kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, \
# kernel_constraint=None, bias_constraint=None)

model.add(MaxPooling2D(pool_size = (3,3)))
# model.add(Conv2D(64,(3,3),activation = 'relu',padding='same'))
# model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Flatten())
model.add(Dense(128,activation = 'relu'))
model.add(Dense(3,activation = 'softmax'))
print(model.summary())
sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=sgd,metrics=['accuracy'])
model.fit(X_train,y_train,batch_size = 100,epochs = 5)
score_tr = model.evaluate(X_train,y_train)
print("train_loss: "+str(score_tr[0]))
print("train_accuracy: "+str(score_tr[1]))
score_te = model.evaluate(X_test,y_test)
print("test_loss: "+str(score_te[0]))
print("test_accuracy: "+str(score_te[1]))