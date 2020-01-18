# (1) Load necessary libraries
import matplotlib.pyplot as plt
from matplotlib import style
import math
import numpy as np
from scipy.stats.stats import pearsonr
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# (2) Trade by rolling average
def trade_rolling_average( data, roll_length, amount, fee, display ):

    # 2.1 prepare data for trading
    rolling_mean = data.rolling(window=roll_length,min_periods=0).mean()
    difference = data - rolling_mean
    
    # 2.2 set constant
    cash = amount
    shares = 0
    invested = False
    bancrupt = False
    trades = 0
    value = [ ]
    max_share_price = data.max()
    
    # 2.3 Trade:
    # (1) Wait for good moment for investment
    # (2) Wail for good instance to sell
    # -> Repeat
    if display:
        print( 'Investor starts...' )

    for i in range( 0, len( data ) ):
        
        # Wait at least 10 days
        # But in any case long enough to have finite values for the differences (can identify tendency)
        if i > 10 and not math.isnan( difference[ i - 2 ] ) and not math.isnan( difference[ i ] ) and not bancrupt:
            
            # check if we should act
            if np.sign( difference[i-2] ) != np.sign( difference[i] ):

                if difference[i] > 0 and invested == False and cash > fee:
                    # -> Buy!
                    shares = ( cash - fee ) / data[ i ]
                    cash = 0
                    invested = True
                    trades = trades + 1
                    if display:
                        print( "Buy:" )
                        print( "Value: " + str( data[ i ] ) )
                        print( "Difference: " + str( difference[i ] ) )
                        print( "Tendency: " + str( difference[ i ] - difference[ i - 2 ] ) )
                        print( "(Money,Shares) = [" + str( cash ) + ", " + str( shares ) + " ]" )
                        print( "Total value: " + str( cash + shares * data[ i ] ) + " \n" )
            
                if difference[i] < 0 and invested == True and shares * data[ i ] - fee > 0:
                    # -> Sell!
                    cash = shares * data[ i ] - fee
                    shares = 0
                    invested = False
                    trades = trades + 1
                    if display:
                        print( "Sell:" )
                        print( "Value: " + str( data[ i ] ) )
                        print( "Difference: " + str( difference[i ] ) )
                        print( "Tendency: " + str( difference[ i ] - difference[ i - 2 ] ) )
                        print( "(Money,Shares) = [" + str( cash ) + ", " + str( shares ) + " ]" )
                        print( "Total value: " + str( cash + shares * data[ i ] ) + " \n" )
        
        # check if the trader is very bad and bancrupt
        if cash + shares * data[ i ] < 0:
            cash = 0
            shares = 0
            bancrupt = True
            print( "Trader bancrupt" )

        value.append( ( cash + shares * data[ i ] ) / amount * max_share_price )
    
    if display:
        print( 'Investor ends \n' )
        print( 'Original investment: ' + str( amount ) )
        print( 'Length of rolling average: ' + str( roll_length ) + ' days' )
        print( 'Total trades: ', str( trades ) )
        print( 'Total fees: ', str( trades * fee ) )
        print( '\n' )
        print( 'Shares: ', str( shares ) )
        print( 'Money: ', str( cash ) )
        print( 'Total value: ', str( data[ len( data ) - 1 ] * shares + cash ) )
        print( 'Increase of value: ' + str( 100 * ( data[ len( data ) - 1 ] * shares + cash ) / amount - 100 ) + '%' )
        print( '\n' )
        print( 'Final difference: ' + str( difference[ len( data ) - 1 ] ) )
        if difference[ len( data ) - 1 ] > 0:
            print( 'Tendency: Value increases -> Hold/Buy' )
        if difference[ len( data ) - 1 ] <= 0:
            print( 'Tendency: Value decreases -> Sell' )
        pos = list(data.index.values)
        plt.plot( pos, data, label = 'opening value' )
        plt.plot( pos, rolling_mean, label = 'rolling mean' )
        plt.plot( pos, difference, label = 'difference' )
        plt.plot( pos, value, label = 'total trading value' )
        plt.title("Opening prices, rolling average and difference")
        plt.ylabel('Value', fontsize = 14)
        plt.xlabel('Trading days', fontsize = 14)
        plt.grid(which = "major", color = 'k', linestyle = '-.', linewidth = 0.5 )
        plt.legend()
        plt.show()
    
    # return total value
    return data[ len( data ) - 1 ] * shares + cash


# (3) Optimize rolling length
def optimize_rolling_length( data, amount, fee ):
    
    print( 'Perform investment for different rolling lengths...' )
    
    rolls = [ x * 10 for x in range(1, 40)]
    returns = []
    max_value = [ 0, 0 ]
    for roll in rolls:
        value = trade_rolling_average( data, roll, amount, fee, False )
        if value > max_value[ 0 ]:
            max_value = [ value, roll ]

    print( 'Finished investings...' )
    print( 'Amount: ' + str( amount ) )
    print( 'Fee per order: ' + str( fee ) )
    print( 'Choices of rolling lengths: ', str( rolls ) )
    print( 'Best rolling length: ', str( max_value[ 1 ] ) )
    print( 'Return for best rolling length: ', str( max_value[ 0 ] ) )
    print( '\n' )

    # Display more details on this ideal strategy
    trade_rolling_average( data, max_value[ 1 ], amount, fee, True )

    # and return data summary
    return max_value
