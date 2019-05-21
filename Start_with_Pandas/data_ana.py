#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import Series, DataFrame 
import numpy as np
import matplotlib as mp
import seaborn as sb
import scipy as sp
import matplotlib.pyplot as plt


# In[3]:


raw_df = pd.read_csv("C:/Users/vipatha/Documents/2. 2019_DeepDives/Softlines_DeepDive/DD-Analysis/All_Softlines_CPLF/softlines_neg.csv",encoding = "ISO-8859-1")


# In[5]:


type(raw_df)


# In[10]:


raw_df.size
raw_df.shape
raw_df.index


# In[12]:


raw_df.dtypes
raw_df is None


# In[14]:


# DROP UNNAMED COLUMNx
raw_df.drop(raw_df.columns[raw_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)


# In[21]:


raw_df.duplicated()
raw_df.isnull()
raw_df.fillna(0)


# In[28]:


#Changing Data Types 
raw_df['mcid'] = raw_df['mcid'].astype(str)
raw_df['gl_product_group'] = raw_df.gl_product_group.astype(str)


# In[30]:


raw_df.head(2)


# In[53]:


raw_df.columns


# In[62]:


data = raw_df.set_index(['item_size', 'gl_product_group'])
data


# In[63]:


data_small = data.loc['Small']
data_small.shape
#data_small_193.index


# In[64]:


data_small.describe()


# In[67]:


data_small['cplf'].corr(data_small['ob_cpu'])


# In[73]:


corr_small = data_small.corr()
type(corr_small)


# In[79]:


corr_small


# In[78]:


corr_small_unstack.sort_values()

