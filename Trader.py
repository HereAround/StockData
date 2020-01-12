# (1) Load necessary libraries
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from datetime import datetime
import os
import matplotlib.pyplot as plt
from matplotlib import style
import math
import numpy as np
from scipy.stats.stats import pearsonr 
style.use('ggplot')


# (2) Trade by rolling average
def trade_rolling_average( data, roll_length, amount, fee, display ):

    # Compute rolling average
    S = data['Open'].dropna()
    length = len(S)
    rolling_mean = S.rolling(window=roll_length,min_periods=0).mean()
    data['Rolling-Mean'] = rolling_mean

    # Compute the differences
    data['Difference'] = data['Open'] - data['Rolling-Mean']

    # Trade:
    # (1) Wait for good moment for investment
    # (2) Wail for good instance to sell
    # -> Repeat
    money = amount
    shares = 0
    invested = False
    trades = 0
    if display:
        print( 'Investor starts...' )

    for i in range(2, length ):
        
        # check if we should act
        if np.sign( data['Difference'][i-2] ) != np.sign( data['Difference'][i] ):

            if data['Difference'][i] > 0 and invested == False:
                # -> Buy!
                shares = ( money - fee ) / data['Open'][ i ]
                money = 0
                invested = True
                trades = trades + 1
            
            if data['Difference'][i] < 0 and invested == True:
                # -> Sell!
                money = shares * data['Open'][ i ] - fee
                shares = 0
                invested = False
                trades = trades + 1
    
    if display:
        print( 'Investor ends' )
        print( '\n' )
        print( 'Original investment: ' + str( amount ) )
        print( 'Length of rolling average: ' + str( roll_length ) + ' days' )
        print( 'Total trades: ', str( trades ) )
        print( 'Total fees: ', str( trades * fee ) )
        print( '\n' )
        print( 'Shares: ', str( shares ) )
        print( 'Money: ', str( money ) )
        print( 'Total value: ', str( data['Open'][ length - 1 ] * shares + money ) )
        print( 'Increase of value: ' + str( 100 * ( data['Open'][ length - 1 ] * shares + money ) / amount ) + '%' )
    
    # return total value
    return data['Open'][ length - 1 ] * shares + money
