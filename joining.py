#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Hierarchical indexing is an important feature of pandas that enables you to have multiple
(two or more) index levels on an axis. 

Somewhat abstractly, it provides a way for you to work with higher dimensional data in a lower dimensional form. 

Hierarchical indexing plays an important role in reshaping data and group-based
operations like forming a pivot table

'''


# In[9]:


import pandas as pd
from pandas import Series, DataFrame 
import numpy as np
import matplotlib as mp
import seaborn as sb
import scipy as sp
import matplotlib.pyplot as plt


# In[ ]:


'''
Let’s start
with a simple example; create a Series with a list of lists (or arrays) as the index:
'''


# In[18]:


#pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
report = pd.DataFrame(data = [[1, 10, 'John'],[1, 20, 'John'],[1, 30, 'Tom'],[1, 10, 'Bob'],[2, 25, 'John'],[2, 15, 'Bob']],
                      columns = ['IssueKey','TimeSpent','User'])
#practice Creating data = pd.DataFrame(data=[], columns=[], index=[])
#practice Creating data dict = {issueKey:[1,1,1,1,2,2],TimeSpent:[10,20,30,10,25,15], User:["John","John","Tom","Bob","John","Bob"] }
#report2 = pd.DataFrame(data=dict_report)
#report2
report 


# In[19]:


# Report is a ONE Dimensional Table with ONE Index level i.e. one index identifying each row 

#Say we want to merge (sum) all logs created by the same user to the same issue 
#(to get the total time spent on the issue by the user)

time_logged_by_user = report.groupby(['IssueKey', 'User']).TimeSpent.sum()

time_logged_by_user


# In[20]:


'''
Now our data index has 2 levels, as multiple users logged time to the same issue. 
The levels are IssueKey and User. The levels are parts of the index (only together they can 
identify a row in a DataFrame / Series).
'''


# In[21]:


'''
Having levels gives us opportunity to aggregate values within groups in respect to an index part (level) of our choice. 
E.g. if we want to assign the max time spent on an issue by any user, we can
'''
max_time_logged_to_an_issue = time_logged_by_user.groupby(level='IssueKey').transform('max')
max_time_logged_to_an_issue


# In[22]:


issue_owners = time_logged_by_user[time_logged_by_user == max_time_logged_to_an_issue]
issue_owners


# In[24]:


max_time_logged_to_an_issue.unstack()


# In[26]:


max_time_logged_to_an_issue.unstack().stack()


# In[33]:


df1 = pd.DataFrame({'key': ['a', 'b', 'c'], 'data1': [1,2,3]})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': [11,12,13]})

df1


# In[34]:


df2


# In[35]:


pd.merge(df1,df2)


# In[36]:


'''
If that information is not specified,
merge uses the overlapping column names as the keys. It’s a good practice to
specify explicitly
'''
pd.merge(df1,df2, on='key')


# In[38]:


pd.merge(df1,df2, on='key',how='left')


# In[39]:


pd.merge(df1,df2, on='key',how='right')


# In[37]:


df3 = pd.DataFrame({'lkey': ['a', 'b', 'c'], 'data1': [1,2,3]})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': [11,12,13]})

pd.merge(df3,df4, left_on='lkey', right_on='rkey')


# In[ ]:




