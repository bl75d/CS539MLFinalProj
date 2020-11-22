# https://pypi.org/project/yfinance/
# https://pypi.org/project/stock-pandas/
import yfinance as yf
import pandas as pd
from stock_pandas import StockDataFrame
msft = yf.Ticker("MSFT")

# get stock info
msft.info
# print(msft.info)

# get historical market data
hist = msft.history(period="ytd")
print(hist)
# #
# {'zip': '98052-6399',
#  'sector': 'Technology',
#  'fullTimeEmployees': 163000,
#  'longBusinessSummary': 'Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); Skype, Outlook.com, and OneDrive; LinkedIn that includes Talent, Learning, Sales, and Marketing solutions, as well as premium subscriptions; and Dynamics 365, a set of cloud-based and on-premises business solutions for small and medium businesses, large organizations, and divisions of enterprises. Its Intelligent Cloud segment licenses SQL and Windows Servers, Visual Studio, System Center, and related CALs; GitHub that provides a collaboration platform and code hosting service for developers; and Azure, a cloud platform. It also offers support services and Microsoft consulting services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification to developers and IT professionals on various Microsoft products. Its More Personal Computing segment provides Windows original equipment manufacturer (OEM) licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; Windows Internet of Things; and MSN advertising. It also offers Surface, PC accessories, PCs, tablets, gaming and entertainment consoles, and other intelligent devices; Gaming, including Xbox hardware, and Xbox content and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. It sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online stores, and retail stores. The company was founded in 1975 and is headquartered in Redmond, Washington.',
#  'city': 'Redmond',
#  'phone': '425-882-8080',
#  'state': 'WA',
#  'country': 'United States',
#  'companyOfficers': [],
#  'website': 'http://www.microsoft.com',
#  'maxAge': 1,
#  'address1': 'One Microsoft Way',
#  'industry': 'Software—Infrastructure',
#  'previousClose': 211.08,
#  'regularMarketOpen': 211.38,
#  'twoHundredDayAverage': 204.50165,
#  'trailingAnnualDividendYield': 0.009901458,
#  'payoutRatio': 0.32900003, 'volume24Hr': None,
#  'regularMarketDayHigh': 212.99,
#  'navPrice': None,
#  'averageDailyVolume10Day': 29447012,
#  'totalAssets': None,
#  'regularMarketPreviousClose': 211.08,
#  'fiftyDayAverage': 213.52083,
#  'trailingAnnualDividendRate': 2.09,
#  'open': 211.38, 'toCurrency': None,
#  'averageVolume10days': 29447012,
#  'expireDate': None,
#  'yield': None,
#  'algorithm': None,
#  'dividendRate': 2.24,
#  'exDividendDate': 1605657600,
#  'beta': 0.868094,
#  'circulatingSupply': None,
#  'startDate': None,
#  'regularMarketDayLow': 209.93,
#  'priceHint': 2,
#  'currency': 'USD',
#  'trailingPE': 34.26682,
#  'regularMarketVolume': 24792746,
#  'lastMarket': None,
#  'maxSupply': None,
#  'openInterest': None,
#  'marketCap': 1606001491968,
#  'volumeAllCurrencies': None,
#  'strikePrice': None,
#  'averageVolume': 32138892,
#  'priceToSalesTrailing12Months': 10.916714,
#  'dayLow': 209.93, 'ask': 212.11, 'ytdReturn': None, 'askSize': 800, 'volume': 24792746, 'fiftyTwoWeekHigh': 232.86, 'forwardPE': 28.474531, 'fromCurrency': None, 'fiveYearAvgDividendYield': 1.78, 'fiftyTwoWeekLow': 132.52, 'bid': 211.96, 'tradeable': False, 'dividendYield': 0.0106, 'bidSize': 1000, 'dayHigh': 212.99, 'exchange': 'NMS', 'shortName': 'Microsoft Corporation', 'longName': 'Microsoft Corporation', 'exchangeTimezoneName': 'America/New_York', 'exchangeTimezoneShortName': 'EST', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '-18000000', 'quoteType': 'EQUITY', 'symbol': 'MSFT', 'messageBoardId': 'finmb_21835', 'market': 'us_market', 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 10.476, 'beta3Year': None, 'profitMargins': 0.32285, 'enterpriseToEbitda': 22.623, '52WeekChange': 0.4120953, 'morningStarRiskRating': None, 'forwardEps': 7.46, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 7560500224, 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'bookValue': 16.313, 'sharesShort': 36796420, 'sharesPercentSharesOut': 0.0049, 'fundFamily': None, 'lastFiscalYearEnd': 1593475200, 'heldPercentInstitutions': 0.71892, 'netIncomeToCommon': 47495999488, 'trailingEps': 6.199, 'lastDividendValue': 0.56, 'SandP52WeekChange': 0.14958727, 'priceToBook': 13.021517, 'heldPercentInsiders': 0.00059, 'nextFiscalYearEnd': 1656547200, 'mostRecentQuarter': 1601424000, 'shortRatio': 1.27, 'sharesShortPreviousMonthDate': 1601424000, 'floatShares': 7448222604, 'enterpriseValue': 1541136449536, 'threeYearAverageReturn': None, 'lastSplitDate': 1045526400, 'lastSplitFactor': '2:1', 'legalType': None, 'lastDividendDate': 1605657600, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': 0.301, 'dateShortInterest': 1604016000, 'pegRatio': 2.15, 'lastCapGain': None, 'shortPercentOfFloat': 0.0049, 'sharesShortPriorMonth': 39634230, 'category': None, 'fiveYearAverageReturn': None, 'regularMarketPrice': 211.38, 'logo_url': 'https://logo.clearbit.com/microsoft.com'}
