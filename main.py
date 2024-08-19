import akshare as ak
import pandas as pd
from datetime import datetime
import taipy.gui.builder as tgb
from taipy.gui import Gui 

# Fetching AAPL stock data using akshare
# akshare provides various interfaces, we'll use the stock interface here
stock_data = ak.stock_us_daily(symbol="AAPL")

# Filtering data for the month of August 2018
start_date = "2018-08-01"
end_date = "2018-08-31"
mask = (stock_data['date'] >= start_date) & (stock_data['date'] <= end_date)
stock_filtered = stock_data.loc[mask]

# Rename columns to match the expected format
stock_filtered = stock_data.rename(columns={
    "date": "Date",
    "open": "Open",
    "close": "Close",
    "low": "Low",
    "high": "High"
})

print(stock_filtered)
# Now let's plot the data
with tgb.Page() as page:
    tgb.chart("{stock_filtered}", type="candlestick", x="Date", open="Open", close="Close", low="Low", high="High")

if __name__ == "__main__":
    Gui(page=page).run(title="Dynamic chart")