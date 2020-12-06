from sklearn.preprocessing import MinMaxScaler,StandardScaler
from tslearn.preprocessing import TimeSeriesScalerMinMax
import numpy as np
from sklearn.model_selection import train_test_split
from Data_stock_dataframe import GetStockData
from sklearn.impute import SimpleImputer
import pandas as pd
from sklearn.preprocessing import Normalizer

def Normalize(df):
    norm=Normalizer()
    norm_df=norm.fit_transform(df)
    return norm_df

def Impute(df):
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputed_df=imp.fit_transform(df)
    return imputed_df

def Scale(df):
    sc = MinMaxScaler(feature_range=(-1, 1))
    scaled_df = sc.fit_transform(df)
    return scaled_df

def tsScale(ts):
    tsc=TimeSeriesScalerMinMax(value_range=(-1,1))
    scaled_ts=tsc.fit_transform(ts)
    return scaled_ts

# create databrick and not split it
def DataBrick(rawdata,rawlabel,size):
    length=rawdata.shape[0]
    databrick=[]
    bricklabel=[]
    if length < size:
        raise Exception("Databrick size exceeds data max length!")
    else:
        # drop the last databrick, b/c last label is fake.
        for i in range(length-size):
            databrick.append(rawdata[i:i+size,:])
            bricklabel.append(rawlabel[i+size])
        databrick=np.asarray(databrick)
        bricklabel=np.asarray(bricklabel).reshape(-1,1)
    return databrick,bricklabel

def SplitData(stock,label,size):
    databrick, bricklabel = DataBrick(stock, label, size)
    X_train, X_test, y_train, y_test = train_test_split(
        # databrick, bricklabel, test_size=0.2, random_state=42)
        databrick, bricklabel, test_size=0.1, shuffle=False)

    # print(X_train.shape, y_train.shape)
    return X_train, X_test, y_train, y_test

def DataPipeline(symbol_list,period,interval):
    StockDict={}
    LabelDict={}
    for symbol in symbol_list:
        # return raw data--stock and label
        stockdf,labeldf = GetStockData(symbol, period, interval)
        stock = np.asarray(stockdf)
        # print(stock)
        label=np.asarray(labeldf)

        # Normalization
        # print(np.any(np.isinf(stock)))

        # deal with some inf in the data
        stock[stock==np.inf]=0
        stock=Impute(stock)
        stock=Scale(stock)
        # stock=Normalize(stock)
        # print(stock)
        StockDict[symbol] = stock
        LabelDict[symbol] = label
    return StockDict,LabelDict