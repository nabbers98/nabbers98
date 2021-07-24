
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


f = open("file.txt", "r")


# In[3]:


data = f.readlines()


# In[4]:


type(data)


# In[5]:


df = pd.DataFrame(data)


# In[6]:


df


# In[7]:


ndf = df[0][0]


# In[8]:


type(ndf)


# In[9]:


import ast


# In[10]:


list_of_dictionaries = ast.literal_eval(ndf)


# In[11]:


type(list_of_dictionaries)


# In[12]:


arebhai = list(list_of_dictionaries)


# In[13]:


pdf = pd.DataFrame(arebhai)


# In[14]:


pdf.tail()


# In[15]:


pdf['Date'] = pd.to_datetime(pdf['ctmString'])


# In[16]:


pdf.head()


# In[17]:


pdf.set_index('Date')


# In[18]:


usable_data = []
data = pd.DataFrame(usable_data)


# In[19]:


data['Open'] = pdf['open']


# In[20]:


data['High'] = pdf['high']
data['Low'] = pdf['low']
data['Close'] = pdf['close']
data['Date'] = pdf['Date']


# In[21]:


data.head()


# In[22]:


data.set_index('Date',inplace=True)


# In[23]:


data.head()


# In[24]:


#data.to_excel('UK100 Data.xlsx')


# In[25]:


data['High Price'] = data['Open'] + data['High']


# In[26]:


data['Low Price'] = data['Open'] + data['Low']


# In[27]:


data.head()


# In[28]:


#data.to_excel('Daily Data.xlsx')


# In[29]:


data['High'].plot(kind='box')


# In[30]:


data['Low'].plot(kind='box')


# In[31]:


data['High'].quantile([0.36,0.5,0.99])


# In[32]:


data['Low'].quantile([0.01,0.5,0.63])


# In[33]:


data.tail()


# In[34]:


calm


# In[35]:


rol_mn = data['Open'].rolling(5).mean()
high_mn = data['High Price'].rolling(5).mean()
low_mn = data['Low Price'].rolling(5).mean()


# In[36]:


data['Open'].plot(figsize=(16,9),xlim=('2014-10-26','2015-06-19'),ylim=(60000,75000), c='black')
#rol_mn.plot()
high_mn.plot()
low_mn.plot(c='r')


# In[37]:


from statsmodels.tsa.seasonal import seasonal_decompose


# In[38]:


wata = data['Open']
wata.plot()


# In[39]:


decomp = seasonal_decompose(wata,freq=30)


# In[40]:


decomp.plot()


# In[41]:


data['Open'].pct_change().plot(figsize=(20,10))

