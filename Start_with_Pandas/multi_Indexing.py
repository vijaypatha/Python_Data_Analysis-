#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[ ]:


'''
Goal: To understand intution around multi indexing and how it can be used
'''

'''
Data structures:
1) Pandas Series -> an array or list which is on dimmensional. WIth only one index
offical def: Series is a one-dimensional labeled array capable of holding any data type (integers, strings, 
floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index

2) Data Frame -> rows and columns, a two dimmensinal array . with index on rows and columns. DATAFRAME is dict-like container for Series objects

Series vs. DataFRAME 
Series is the datastructure for a single column of a DataFrame, not only conceptually, 
but literally i.e. the data in a DataFrame is actually stored in memory as a collection of Series.
'''

'''
A multi index multiple
(two or more) index levels on an axis. Hierarchical indexing plays an important role in reshaping data and group-based
operations like forming a pivot table
'''


# In[11]:


stocks = pd.read_csv("http://bit.ly/smallstocks")
stocks


# In[35]:


type(stocks)


# In[6]:


stocks.index


# In[41]:


stock_group = stocks.groupby(['Symbol','Date']).Close.mean()
stock_group


# In[31]:


type(stock_group)


# In[26]:


stock_group.index


# In[34]:


check_type = stock_group.unstack()
check_type


# In[33]:


type(check_type)


# In[38]:


stock_pivot = stocks.pivot_table(values = 'Close', index = 'Symbol', columns = 'Date' )
stock_pivot


# In[39]:


type(stock_pivot)


# In[ ]:


'''
Selecting from the multi level Series. Remember stock_group is a series 
'''


# In[42]:


# Selecting by a inner index 
stock_group.loc['AAPL']


# In[44]:


#Selecting by a inner and outer index 
stock_group.loc['AAPL', '2016-10-03']


# In[45]:


#Selecting by outer level
stock_group.loc[:,'2016-10-03']


# In[ ]:


# ******NOTE: DATAFRAME and SERIES SELECTION WORKS THE SAME************


# In[46]:


# Multiindexing Dataframe


# In[48]:


stocks_df = stocks.set_index(['Symbol', 'Date'])
stocks_df


# In[53]:


stocks_df.sort_index(inplace=True)
stocks_df


# In[54]:


type(stocks_df)


# In[56]:


#SELECTING FROM THE STOCK_DF 

stocks_df.loc['AAPL']


# In[57]:


stocks_df.loc['AAPL', '2016-10-04']


# In[59]:


# EVEN THOUGH stocks_df.loc['AAPL', '2016-10-04'] work, best practice when selecting anything other then outer layer
# Its a good practice to pass the inneer levels as a tupel and then a comma to indicate what columns
stocks_df.loc[('AAPL', '2016-10-04'),:]


# In[74]:


#What if I want all stock for one column
stocks_df.loc[(['AAPL','MSFT','CSCO'], '2016-10-04'),:]


# In[73]:


#What if I want all stock for a data
check2 = stocks_df.loc[(['AAPL','MSFT','CSCO'], ['2016-10-04', '2016-10-05']),'Close']
check2


# In[70]:


#type(check)


# In[71]:


check2.unstack()


# In[75]:


#What if I want all stock for a data
check3 = stocks_df.loc[(['AAPL','MSFT','CSCO'], ['2016-10-04', '2016-10-05']),:]
check3


# In[78]:


#What if I want all stock for a data
check4 = stocks_df.loc[(slice(None), ['2016-10-04', '2016-10-05']),'Close']
check4


# In[79]:


#What if I want all stock for a data
check5 = stocks_df.loc[(slice(None), ['2016-10-04', '2016-10-05']),'Volume']
check5


# In[83]:


pd.merge(check4, check5, left_index= True, right_index= True)


# In[ ]:

