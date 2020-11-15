# https://finnhub.io/docs/api

import requests
import pandas as pd
import io

# https://finnhub.io/docs/api
key='btvb3h748v6o8d95q2o0'
symbol_list=["AAPL","AMZN","TSLA"]
symbol='TSLA'
# UNIX timestamp. Interval initial value.
starttime='1225533600'
endtime='1602086400'
# Supported resolution includes 1, 5, 15, 30, 60, D, W, M
solution=['1', '5', '15', '30', '60', 'D', 'W', 'M' ]
format=['json','csv']

# for symbol in symbol_list:
#     requests_string='https://finnhub.io/api/v1/stock/candle?symbol='+symbol+'&resolution='+solution[4]+'&from='+starttime+'&to='+endtime+'&token='+key
#     print(requests_string)
#     # response = requests.get(requests_string)
#     # print(response.json())

# response = requests.get(requests_string)
# # print(response.json())
#
# close_price=response.json()['c']
# highest_price=response.json()['h']
# lowest_price=response.json()['l']
# open_price=response.json()['o']
# volume=response.json()['v']
# time_stanp=response.json()['t']

requests_string='https://finnhub.io/api/v1/stock/candle?symbol='+symbol+'&resolution='+solution[4]+'&from='+starttime+'&to='+endtime+'&token='+key+'&format='+format[1]

response = requests.get(requests_string).content
rawData=pd.read_csv(io.StringIO(response.decode('utf-8')))
#rawData has colums as [t,o,h,l,c,v]
print(rawData)
