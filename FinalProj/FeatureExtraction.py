from DataRequest import *

import yfinance as yf, pandas as pd, shutil, os, time, glob
import numpy as np
import requests
from statistics import mean
import stockstats

tickers = ["AMZN", "CRM", "AAL", "DAL", "TSLA", "MSFT", "FB", "AAPL"]
stock =stockstats.StockDataFrame.retype(rawData)