''' 
@author Shijing (Iris)
@create date 2020-11-23 21:48:51
'''

import yfinance as yf
import pandas as pd
from stock_pandas import StockDataFrame
import generate_dataframe as gd 
import stock_dataframe_to_stdf as sdts 
import stock_pandas_to_stdf as spts 
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

data = gd.generate_df("AAPL","1y","1d")
columns = ['open','close','high','low','volume','amount']
stockdf = sdts.generate_stdf(data)
stock = sdts.data_processing(columns,stockdf)
df = sdts.to_df(stock)
stockdf = spts.data_processing(StockDataFrame(df))
df = sdts.to_df(stockdf)

# dropping columns with at least one nan value
temp_df = df.dropna(axis=1) 
print(temp_df.head())
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
numeric_df = temp_df.select_dtypes(include=numerics)
# print(numeric_df.shape)
# numeric_df.drop(["Date"],axis=1)
# print(numeric_df.head())
import seaborn as sns 
# 
sns.heatmap(numeric_df.corr())
plt.show()
