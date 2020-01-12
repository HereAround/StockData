#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is the main file. The other files declare functions.

# Load all necessary libraries
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

# load our functions
import Downloader.py
import trader_001.py

# execute our functions

get_stock_data()