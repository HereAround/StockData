# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:50:25 2020

@author: Patrick
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import math
import numpy as np
from scipy.stats.stats import pearsonr 

style.use('ggplot')

"""
----------------
Import of Data 
----------------
"""

start = dt.datetime(1986, 1, 1) # choose starting date of data import
end = dt.datetime(2020, 1, 7) # choose end date of data import
df = web.DataReader("^DJI", 'yahoo', start, end) # choose the title/index etc.
df.reset_index(inplace=True) 
df.set_index("Date", inplace=True)

S = df['Close'].dropna()
length = len(S)

"""
-----------------------------
Computation of Log Returns
-----------------------------
"""

logreturn = [0]
for i in range(0,length-1):
    logreturn.append(math.log(S[i+1]/S[i]))

df['Return'] = logreturn

"""
-------------------------------------------------------
Rolling mean of stock prices and its deviation (delta)
-------------------------------------------------------
"""

rolling_mean = S.rolling(window=250,min_periods=0).mean()
df['Rolling Mean'] = rolling_mean

delta = [0]
for i in range(0, length-1):
    if S[i] is not 'nan':
        delta.append((S[i]/df['Rolling Mean'][i]-1)/length)

df['Delta'] = delta

"""
------------------------------
Definition of Delta investor
------------------------------
"""
monthly_investment = 500
total_investment = 0
begin = 10
end = 5000
shares = 0
shares_list = []
for i in range(begin,end):
    if df['Rolling Mean'][i] < df['Close'][i]:
        shares = shares + monthly_investment/S[i]
        shares_list.append(shares)
        i = i + 30
        total_investment = total_investment + monthly_investment
    else:
        shares_list.append(shares)
        

"""
----------------------
Definition of output
----------------------
"""

print('Deviation from rolling mean:', sum(delta))
print(len(shares_list))
print('Total return rate:', 100*(S[end]*shares_list[end-begin-1]/total_investment - 1), '%')