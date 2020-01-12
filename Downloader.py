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


# (2) Get stock_data
def save_stock_data( source, tickers, start, end ):
    
    if not os.path.exists('stockdata'):
        os.makedirs('stockdata')
    
    for ticker in tickers:
        print (ticker)
        try:
            df = web.DataReader(ticker, source, start, end )
            df.to_csv('stockdata/'+ticker+'.csv')
            print(ticker,'downloaded and saved')
            print('\n')
        except Exception as e:
            print( e, 'error' )


# (2) Get stock_data
def get_stock_data( source, ticker, start, end ):
    
    print (ticker)
    try:
        df = web.DataReader(ticker, source, start, end )
        print(ticker,'downloaded')
        print('\n')
    except Exception as e:
        print( e, 'error' )
    
    # use date as index in this dataframe
    df.reset_index(inplace=True) 
    df.set_index("Date", inplace=True)
    
    # now return the data
    return df
