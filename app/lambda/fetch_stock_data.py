import yfinance as yf # type: ignore

tcs = yf.Ticker("TCS.NS")
data = tcs.history(period="6mo") # type: ignore
print(data)