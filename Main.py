#!/usr/bin/env python3

# (0) Load libraries
import datetime as dt
from datetime import datetime


# (1) Load functionality
from Downloader import save_stock_data, get_stock_data
from Trader import trade_rolling_average


# (2) Set our desired variables/parameters
source = 'yahoo'
ticker = 'GOOGL'
#ticker = '^DJI'
start = dt.datetime(1998,3,5)
end = dt.datetime.today()


# (3) Get stock data
#tickers = [ 'GOOGL' ]
#save_stock_data( source, tickers, start, end )
data = get_stock_data( source, ticker, start, end )


# (4) Trade
money = trade_rolling_average( data, 250, 10000, 5, True )


# (5) Repeat for different lengths of rolling averages
rolls = [ x * 10 for x in range(1, 40)]
returns = []
max_value = [ 0, 0 ]
for roll in rolls:
    value = trade_rolling_average( data, roll, 10000, 5, False )
    if value > max_value[ 0 ]:
        max_value = [ value, roll ]

print( '\n' )
print( 'Repeated for different rolling lengths: ', str( rolls ) )
print( 'Maximal return for rolling length: ', str( max_value[ 1 ] ) )
print( 'Maximal return: ', str( max_value[ 0 ] ) )
