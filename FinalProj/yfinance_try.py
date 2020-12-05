import yfinance as yf

msft = yf.Ticker("AAPL")
# yf.Ticker("MSFT")
# get stock info


# for key in msft.info.keys():
#     print(key)
# # get historical market data
# hist = msft.history(period="max")

# show actions (dividends, splits)
print(msft.actions)

# # show dividends
# msft.dividends

# # show splits
# msft.splits

# # show financials
# msft.financials
# msft.quarterly_financials

# # show major holders
# msft.major_holders

# # show institutional holders
# msft.institutional_holders

# # show balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet

# # show cashflow
print(msft.cashflow)
# print(msft.quarterly_cashflow)
