import yfinance as yf # type: ignore
from  app.utils.constants import nifty50_stocks

for stock in nifty50_stocks:
    tcs = yf.Ticker(stock)
    data = tcs.history(period="6mo") # type: ignore
    print(data)