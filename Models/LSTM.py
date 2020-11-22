import numpy
import matplotlib.pyplot as plt
import pandas
import math
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout, Activation
from tensorflow.keras.layers import LSTM, GRU
from sklearn.metrics import mean_squared_error
from tensorflow.keras.optimizers import Adam, SGD, RMSprop
from sklearn.metrics import mean_squared_error
from tensorflow.keras.optimizers import Adam, SGD, RMSprop
from sklearn.preprocessing import MinMaxScaler

def lstm(train_features,test_features,features,train_label,test_label):
    train_features= train_features.reshape(train_features.shape[0], 1, train_features.shape[1])
    train_features.shape

    test_features= test_features.reshape(test_features.shape[0], 1, test_features.shape[1])
    test_features.shape

    # Model building
    model = Sequential()
    model.add(GRU(256, input_shape=(1, features), return_sequences=True ))
    model.add(Dropout(0.25))
    model.add(LSTM(256))
    model.add(Dropout(0.25))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1))
    model.summary()
    # use optimizer to reduce loss and find best parameters
    model.compile(loss='mean_squared_error', optimizer=Adam(0.0005), metrics=['mean_squared_error'])

    # results= model.fit(train_features, train_label, epochs=70, batch_size=128, validation_data=(test_features, test_label))
    return model