#!/usr/bin/env python
# coding: utf-8

# In[66]:


# !pip install backtesting

#Importing backtesting library
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG

#Importing stock data 
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd


# In[88]:


## Import Data 
# We would like all available data
start_date = '2019-01-01'
end_date = '2021-02-01'

stock_name = 'NKLA'

# In days
short_window_input = 50
long_window_input = 100


# In[89]:


# User pandas_reader.data.DataReader to load the desired data. As simple as that.
imported_stock_data = data.DataReader(stock_name, 'yahoo', start_date, end_date)

### Augmenting Data

## We need data in the following format:
# Index High	Low	Close	Volume

STOCK = imported_stock_data[["Open", "High", "Low", "Close", "Volume"]]

STOCK


# In[ ]:





# In[ ]:





# In[90]:


### Define Stratgy 

class SmaCross(Strategy):
    n1 = short_window_input
    n2 = long_window_input

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()



# In[ ]:





# In[ ]:





# In[ ]:





# In[91]:


bt = Backtest(STOCK, SmaCross,
              cash=1000, commission=.002,
              exclusive_orders=True)

output = bt.run()
bt.plot()





# In[92]:



output


# In[ ]:





# In[ ]:





# In[ ]:




