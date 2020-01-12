#!/usr/bin/env python3

# (0) Load libraries
import datetime as dt
from datetime import datetime


# (1) Load functionality
from Downloader import save_stock_data, get_stock_data
from Trader import trade_rolling_average, optimize_rolling_length


# (2) Pick title
source = 'yahoo'
ticker = 'GOOGL'
ticker = 'AMZN'
#ticker = '^DJI'
#ticker = '005930.KS' # Samsung?
# Next: Automatically find the ticker for a given WKN or ISDN

# (3) Pick start and end date
start = dt.datetime(1980,3,5)
end = dt.datetime.today()


# (4) Pick how much to invest in single order and how much one order costs in fees
amount = 10000
fee = 5


# (5) Extract stock data
data = get_stock_data( source, ticker, start, end )


# (6) Find ideal rolling length
max_value = optimize_rolling_length( data, amount, fee )
