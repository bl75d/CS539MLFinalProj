import numpy as np
import yfinance as yf
import pandas as pd
from stock_dataframe import StockDataFrame
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


def get_label(stock):
    # # fulfill missing values
    # stock = stock.fillna(method='ffill')
    # stock = stock.fillna(0)
    # print(stock.isnull().sum())

    # label(macd based)
    x = np.asarray(stock['macd'])
    y = np.asarray(stock['amount'] / stock['volume'])

    peaks, _ = find_peaks(stock['macd'], height=0)
    valleys, _ = find_peaks(-stock['macd'], height=0)

    # Savitzky–Golay filter
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_filter.html
    xhat = savgol_filter(x, 31, 3)
    savgol_peaks, _ = find_peaks(xhat, height=0)
    savgol_valleys, _ = find_peaks(-xhat, height=0)

    # RSI criteria
    # v=[]
    # p=[]
    #
    # for i in peaks:
    #         if (stock["rsi_6"].iloc[i]>65):
    #              p.append(i)
    #
    # for i in valleys:
    #         if(stock["rsi_6"].iloc[i]<35):
    #              v.append(i)

    # peaks=p
    # valleys=v
    # print(peaks)
    # print(x[peaks])
    # print(x[valleys])

    # plot the MACD graph land mark the local peak/valley points
    # plt.plot(x)
    # plt.plot(peaks,x[peaks],"x")
    # plt.plot(valleys,x[valleys],"x")
    # plt.plot(np.zeros_like(x),"--",color="gray")
    # plt.show()
    #
    # plt.plot(y)
    # plt.plot(peaks,y[peaks],"x")
    # plt.plot(valleys,y[valleys],"x")
    # plt.plot(np.zeros_like(y),"--",color="gray")
    # plt.show()

    # Savitzky–Golay filtered peaks and valleys
    # plt.plot(x)
    # plt.title("MACD")
    # plt.plot(savgol_peaks,x[savgol_peaks],"x")
    # plt.plot(savgol_valleys,x[savgol_valleys],"x")
    # plt.plot(np.zeros_like(x),"--",color="gray")
    # plt.show()

    plt.plot(y)
    plt.title("Stockprice")
    plt.plot(savgol_peaks, y[savgol_peaks], "x")
    plt.plot(savgol_valleys, y[savgol_valleys], "x")
    plt.plot(np.zeros_like(y), "--", color="gray")
    plt.show()

    stock['label'] = 0
    for i in peaks:
        stock["label"].iloc[i] = 1
    for i in valleys:
        stock["label"].iloc[i] = -1

    # print(stock["label"])
    # print(stock)

    # print(stock.shape)
    label = stock['label']
    return label

def get_naive_label(stock):
    stock = stock.fillna(method='ffill')
    stock = stock.fillna(0)
    adj_price= np.asarray(stock['amount'] / stock['volume'])
    stock['label'] = 0
    for i in range(adj_price.shape[0]-1):
            if(adj_price[i+1]>adj_price[i]):
                stock['label'].iloc[i]=1
            elif(adj_price[i+1]<adj_price[i]):
                stock['label'].iloc[i]=-1

    # For current last data, there is no label, always predict it as 1(assume next time is a bull)
    stock['label'].iloc[-1] = 1
    label=stock['label']
    # print(label)
    return label