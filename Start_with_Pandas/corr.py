#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt


# In[35]:


all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG', 'AMZN', 'KO']}


# In[36]:


type(all_data)


# In[48]:


peek_data = pd.DataFrame(all_data, index=[1,2,3,4,5,6])
peek_data


# In[38]:


price = pd.DataFrame({ticker: data['Adj Close']
for ticker, data in all_data.items()})


# In[47]:


price.tail()


# In[39]:


volume = pd.DataFrame({ticker: data['Volume']
for ticker, data in all_data.items()})


# In[40]:


returns = price.pct_change()
returns.tail()


# In[41]:


'''
The corr method of Series computes the correlation of the overlapping, non-NA,
aligned-by-index values in two Series. Relatedly, cov computes the covariance:
'''


# In[42]:


returns['AMZN'].corr(returns['MSFT'])


# In[43]:


returns['AMZN'].cov(returns['MSFT'])


# In[44]:


returns.corr()


# In[31]:


plt.matshow(returns.corr())
plt.show()


# In[ ]:




