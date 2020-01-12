#!/usr/bin/env python3.7

# the above ensures that this code is being executed with python3.7 if we simply issue this script

# (1) Create a virtual environment in which we run python3.7
# (1) This is to protect the system phyton.
# (1) To this end, it will create a directory "virt-python3.7" in which we run a fresh copy of python3.7
# (1) In particular, all packages have to be installed in this virtual environment (otherwise: module not found)
python3.7 -m venv virt-python3.7

# (2) Activate the virtual environment
source virt-python3.7/bin/activate

# (3) Load all necessary libraries
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
#style.use('ggplot')

# load our functions
#import Downloader.py
#import trader_001.py

# execute our functions

#get_stock_data()
