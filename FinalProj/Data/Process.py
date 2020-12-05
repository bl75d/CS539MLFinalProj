
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import stock_pandas as pds
from stock_dataframe import StockDataFrame

import yfinance as yf

from tslearn.preprocessing import TimeSeriesScalerMinMax
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer

from scipy.signal import savgol_filter
from scipy.ndimage.interpolation import shift
from scipy.signal import find_peaks

def process(stockDict,labelDict,size=10):

    X_train = []
    X_test = []
    Y_train = []
    Y_test = []

    for symbol in stockDict.keys():

        stockData = stockDict[symbol]
        labelData = labelDict[symbol]

        # deal with some inf in the data
        stockData[stockData==np.inf]=0
        stockData=Impute(stockData)
        stockData=Scale(stockData)

        stock_X_train, stock_X_test, stock_Y_train, stock_Y_test = SplitData(stockData,labelData,size)

        X_train.append(stock_X_train)
        X_test.append(stock_X_test)
        Y_train.append(stock_Y_train)
        Y_test.append(stock_Y_test)

    X_train = np.array(X_train[0])
    X_test = np.array(X_test[0])
    Y_train = np.array(Y_train[0])
    Y_test = np.array(Y_test[0])
    return X_train,X_test,Y_train,Y_test

def Normalize(df):
    norm=Normalizer()
    norm_df=norm.fit_transform(df)
    return norm_df

def Impute(df):
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputed_df=imp.fit_transform(df)
    return imputed_df

def Scale(df):
    sc = MinMaxScaler(feature_range=(0, 1))
    scaled_df = sc.fit_transform(df)
    return scaled_df

def tsScale(ts):
    tsc=TimeSeriesScalerMinMax(value_range=(0,1))
    scaled_ts=tsc.fit_transform(ts)
    return scaled_ts

def DataBrick(rawdata,rawlabel,size):
    length=rawdata.shape[0]
    databrick=[]
    bricklabel=[]
    if length < size:
        raise Exception("Databrick size exceeds data max length!")
    else:
        # drop the last databrick, b/c last label is fake.
        for i in range(length-size):
            databrick.append(rawdata[i:i+10,:])
            bricklabel.append(rawlabel[i+10])
        databrick=np.asarray(databrick)
        bricklabel=np.asarray(bricklabel).reshape(-1,1)
    return databrick,bricklabel

def SplitData(stock,label,size):
    databrick, bricklabel = DataBrick(stock, label, size)
    X_train, X_test, y_train, y_test = train_test_split(databrick, bricklabel, test_size=0.2, shuffle=False)

    return X_train, X_test, y_train, y_test