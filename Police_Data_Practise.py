#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv('..Police Data.csv')


# In[5]:


df.head()


# <h4> Remove the column that only contains empty values

# In[15]:


df.isnull().sum()


# In[20]:


df.info() # the total row is 65535


# In[12]:


# count the number of different value in the columns

df['country_name'].value_counts(dropna = False)


# In[22]:


df.drop(columns = 'country_name', inplace = True)


# <h4> For speeding, weremen or women stopped more often?

# In[24]:


df.head()


# In[45]:


df[df.violation == 'Speeding'].driver_gender.value_counts()


# <h4> Does gender affect who gets search during a stop?

# In[39]:


df.groupby('driver_gender').search_conducted.sum()


# In[42]:


df.search_conducted.value_counts() #from here, we can see that the sum only count the True value.


# <h4> What is the mean stop_duration?

# In[48]:


# use mapping and data-type casting 

df.stop_duration.value_counts()


# In[50]:


# df['column'] = df['column'].map({old:new,old:new}) *assuming we are doing 0-60 min.
df['sto_duration'] = df['stop_duration'].map({'0-15 Min':7.5, '16-30 Min':24, '30+ Min':45})


# In[52]:


df['sto_duration'].mean()


# <h4> Compare the distributions for each violation

# In[54]:


df.head()


# In[ ]:




