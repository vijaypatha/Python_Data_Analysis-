#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from pandas import Series, DataFrame
#Series and DataFrame are the workhorse of pandas 


# In[ ]:


'''
pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean',
fill_value=None, margins=False, dropna=True, margins_name='All')

data : DataFrame
values : column to aggregate, optional
index : column, Grouper, array, or list of the previous
If an array is passed, it must be the same length as the data. The list can contain any of the other types (except list). Keys to group by on the pivot table index. If an array is passed, it is being used as the same manner as column values.

columns : column, Grouper, array, or list of the previous
If an array is passed, it must be the same length as the data. The list can contain any of the other types (except list). Keys to group by on the pivot table column. If an array is passed, it is being used as the same manner as column values.

aggfunc : function, list of functions, dict, default numpy.mean
If list of functions passed, the resulting pivot table will have hierarchical columns whose top level are the function names (inferred from the function objects themselves) If dict is passed, the key is column to aggregate and value is function or list of functions

fill_value : scalar, default None
Value to replace missing values with

margins : boolean, default False
Add all row / columns (e.g. for subtotal / grand totals)

dropna : boolean, default True
Do not include columns whose entries are all NaN

margins_name : string, default ‘All’
Name of the row / column that will contain the totals when margins is True.

'''


# In[3]:


dict = {"A": ["foo", "foo", "foo", "foo", "foo","bar", "bar", "bar", "bar"],
        "B": ["one", "one", "one", "two", "two","one", "one", "two", "two"],
        "C": ["small", "large", "large", "small","small", "large", "small", "small",
                          "large"],
        "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
        "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]}


# In[5]:


df = pd.DataFrame(dict)
df


# In[10]:


table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], 
                       aggfunc=np.sum)
table


# In[9]:


table2 = pd.pivot_table(df, values='E', index=['C'], columns=['A'], 
                       aggfunc=np.sum)
table2


# In[ ]:




