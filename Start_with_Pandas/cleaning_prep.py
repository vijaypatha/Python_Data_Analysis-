#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from pandas import Series, DataFrame 
import numpy as np
import matplotlib as mp
import seaborn as sb
import scipy as sp
import matplotlib.pyplot as plt


# In[4]:


'''
Cleaning Data:

1) Load the data
    df.pd.read_csv()
2) Missing values
    df.isnull()
    df is none
    df.dropna()
3) Duplicates
    df.duplicated()
    df.drop_duplicates()
    df.drop_duplicates(['column_name'])
    df.drop_duplicates(['column_name', 'column_name'], keep='last') # drop the first duplicate 
'''


# In[5]:


raw_df = pd.read_csv("...")


# In[6]:


raw_df.head(2)


# In[7]:


#raw_df.isnull()


# In[8]:


raw_df is None


# In[9]:


#raw_df.dropna()


# In[10]:


# DROP UNNAMED COLUMN
raw_df.drop(raw_df.columns[raw_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)


# In[11]:


raw_df.head(2)


# In[12]:


#Checking for duplicates

#raw_df.duplicated() #indicating whether each row is a duplicate across all the columsn in the dataframe 


# In[13]:


#raw_df.dtypes


# In[14]:


# CHANGING THE DATATYPES 
raw_df['mcid'] = raw_df.mcid.astype(str)
raw_df['gl_product_group'] = raw_df.gl_product_group.astype(str)

#raw_df.dtypes


# In[15]:


# Adding a new column
raw_df['Unique_id'] = raw_df.asin + raw_df.mcid
raw_df.head(2)


# In[16]:


data = raw_df.set_index('Unique_id')
data.head(2)


# In[17]:


x = data.plot.scatter('shipping_costs','fullfillment_fee')


# In[18]:


from pandas.plotting import scatter_matrix


# In[19]:


index = data.index
columns = data.columns
print(columns)


# In[20]:


data_sub = data[['neg_cplf_ex_ads', 'neg_cplf_units_zone6_or_more',
       'total_units_zone6_or_more', 'neg_cplf_units_zone5_or_more',
       'total_units_zone5_or_more']]


# In[21]:


data_sub2 = data_sub.head(5)
data_sub2


# In[22]:


scatter_matrix(data_sub2, alpha=0.2, figsize=(6, 6), diagonal='kde')


# In[23]:


samp_data = data.sample(n=10000)
samp_data.head()


# In[24]:


samp_data.describe()


# In[25]:


x = samp_data.plot.scatter('neg_cplf_units_zone6_or_more','neg_cplf_ex_ads')


# In[26]:


samp_data['neg_cplf_units_zone6_or_more'].corr(samp_data['neg_cplf_ex_ads'])


# In[27]:


samp_data['neg_cplf_ex_ads'].corr(samp_data['neg_cplf_units_zone6_or_more'])


# In[28]:


#samp_data['asin_profitability_cplf'].corr(samp_data['item_size'])


# In[29]:


'''
Index(['asin', 'mcid', 'pg_rollup', 'gl_product_group', 'brand', 'item_name',
       'asin_profitability_cplf', 'is_hazmat', 'is_special_delivery',
       'sort_type', 'asin_profitability_cplf_ex_ads', 'asp',
       'monthly_velocity_band', 'avg_months_of_cover', 'item_size',
       'rate_card', 'warehouse_type', 'return_rate', 'ib_freq_bands',
       'asin_box_allocation', 'asin_count', 'gms', 'units', 'cp', 'cp_ex_ads',
       'cplf', 'cplf_ex_ads', 'neg_units', 'neg_gms', 'neg_cplf',
       'neg_cplf_ex_ads', 'neg_cplf_units_zone6_or_more',
       'total_units_zone6_or_more', 'neg_cplf_units_zone5_or_more',
       'total_units_zone5_or_more', 'shipping_rev', 'bad_debt', 'fee_amt',
       'other_rev', 'giftwrap', 'revshare', 'subscription_fee',
       'credit_card_cost', 'closing_fee', 'seller_credits', 'variable_cs_cost',
       'product_gms', 'fullfillment_fee', 'refunds_cost', 'refund_rev',
       'shipping_costs', 'ob_cpu', 'reimbursement_total'],
      dtype='object')
'''
plt.matshow(samp_data.corr())


# In[30]:


c = samp_data.corr()
s = c.unstack()
so = s.sort_values(kind="quicksort")
so.to_csv("corells.csv", encoding='utf8')


# In[31]:


#samp_data.dtypes


# In[ ]:




