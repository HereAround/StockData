#!/usr/bin/env python3

# (0) Load libraries
import datetime as dt
from datetime import datetime


# (1) Load functionality
from Downloader import save_stock_data, get_stock_data
#import trader_001


# (2) Set our desired variables/parameters
source = 'yahoo'
tickers = ['TSLA', 'MCD', 'AAPL', 'GOOGL', 'XOM' ]
start = dt.datetime(2000,3,5)
end = dt.datetime.today()


# (3) Execute functions
save_stock_data( source, tickers, start, end )
df = get_stock_data( source, tickers, start, end )
