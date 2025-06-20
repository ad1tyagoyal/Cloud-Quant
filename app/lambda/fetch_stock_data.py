import yfinance as yf 
from typing import List, Dict, Any
from app.utils.constants import nifty50_stocks
from app.utils.s3_utils import upload_data_to_s3

def fetch_stock_data() -> List[Dict[str, Any]]:
    nifty_50_data: List[Dict[str, Any]] = []
    for stock in nifty50_stocks:
        tcs = yf.Ticker(stock)
        data = tcs.history(period="6mo") 
        nifty_50_data.append({
            "symbol": stock,
            "data": data
        })
    
    return nifty_50_data



if __name__ == "__main__":
    data = fetch_stock_data()
    bucket_name = "nifty-50-raw-data-bucket"
    upload_data_to_s3(bucket_name, str(data).encode('utf-8'), "nifty_50_data.csv")
    print("Stock data fetched and uploaded to S3 successfully.")