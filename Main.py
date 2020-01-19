#!/usr/bin/env python3

# (0) Load libraries
import datetime as dt
from datetime import datetime


# (1) Load functionality
from Downloader import save_stock_data, get_stock_data
from Trader import trade_rolling_average, optimize_rolling_length


# (2) Set constants
source = 'yahoo'
tickers = [ 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SAP', '^DJI', 'CON.DE', 'TTR1.DE', 'DRI.DE', 'ZO1.DE', '005930.KS', 'LEO' ]
start = dt.datetime(1980,3,5)
end = dt.datetime.today()


# (3) Obtain stock data
data = get_stock_data( source, tickers, start, end )
test_data = data[ 11 ]

# (5) Pick how much to invest in single order and how much one order costs in fees
amount = 10000
fee = 5
stopLoss = 0.1
trade_rolling_average( test_data, 20, amount, fee, stopLoss, True )
#max_value = optimize_rolling_length( data, amount, fee )
