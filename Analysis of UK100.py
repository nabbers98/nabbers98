
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
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


pdf.head()


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


data['High'].quantile([0.4,0.5,0.85])


# In[32]:


data['Low'].quantile([0.15,0.5,0.6])


# In[33]:


nontradingdays = data[(data['Low'] < -850) | (data['High'] > 850)]


# In[34]:


msngdys = len(nontradingdays)/len(data)
print(msngdys)


# In[35]:


untradable_day = data[(data['Low'] > -120.1) | (data['High'] < 120.1)]


# In[36]:


untradable_day.head()


# In[37]:


#untradable_day.to_excel('Untradable Days.xlsx')


# In[38]:


pct_bad_days = len(untradable_day)/len(data)


# In[39]:


print(pct_bad_days)


# In[40]:


data['Low'].median()


# In[41]:


data['High'].median()


# In[42]:


data['High'].plot(figsize=(16,9))
data['Low'].plot(c='r')
plt.axhline(120,c='black')
plt.axhline(-120,c='black')


# In[43]:


untradable_day['High'].plot(figsize=(16,9))
untradable_day['Low'].plot(c='r')
plt.axhline(120,c='black')
plt.axhline(-120,c='black')


# In[44]:


np.corrcoef(untradable_day['High'],untradable_day['Low'])


# In[45]:


daily_uk100 = [data['Open'],data['High'],data['Low'],data['Close']]


# In[46]:


placeholder = pd.concat(daily_uk100,axis=1)


# In[47]:


placeholder.head()


# In[48]:


placeholder['High Price'] = placeholder['Open'] + placeholder['High']


# In[49]:


placeholder['Low Price'] = placeholder['Open'] + placeholder['Low']


# In[50]:


placeholder['Spread'] = placeholder['High Price'] - placeholder['Low Price'] 


# In[51]:


placeholder.head()


# In[52]:


placeholder.drop(columns=['High','Low'],inplace=True)


# In[53]:


placeholder.head()


# In[54]:


type(placeholder)


# In[55]:


placeholder['Spread'].quantile([0.01,0.1,0.25])


# In[56]:


logic = ({'Open'  : 'first',
         'High Price'  : 'max',
         'Low Price'   : 'min',
         'Close' : 'last'})

offset = pd.offsets.timedelta(days=-6)

placeholder.resample('W', loffset=offset).apply(logic).head()


# In[57]:


weekly_uk100 = placeholder.resample('W', loffset=offset).apply(logic).dropna()


# In[58]:


weekly_uk100.head()


# In[59]:


weekly_uk100['High'] = weekly_uk100['High Price'] - weekly_uk100['Open']


# In[60]:


weekly_uk100['High'].quantile([0.1,0.5])


# In[61]:


weekly_uk100['Low'] = weekly_uk100['Open'] - weekly_uk100['Low Price']


# In[62]:


weekly_uk100['Low'].quantile([0.1,0.5])


# In[63]:


import numpy as np


# In[64]:


np.corrcoef(weekly_uk100['Low'],weekly_uk100['High'])


# In[65]:


#weekly_uk100['Open'].plot(figsize=(16,9))
weekly_uk100['High Price'].plot(figsize=(16,9))
weekly_uk100['Low Price'].plot()


# In[66]:


weekly_uk100['High'].plot(figsize=(16,9),c='green',xlim=('2009-10-06','2020-06-09'),ylim=(0,11000))
weekly_uk100['Low'].plot(c='r')
plt.axhline(120,c='black')


# In[67]:


anom_weeks = weekly_uk100[(weekly_uk100['Low'] < 120.1) | (weekly_uk100['High'] < 120.1)]


# In[68]:


pct_untradable_weeks = len(anom_weeks)/len(weekly_uk100)
print(pct_untradable_weeks)


# In[69]:


weekly_uk100.head()


# In[70]:


weekly_uk100.to_csv('Weekly Data.csv')


# In[71]:


anom_weeks.tail()


# In[72]:


anom_weeks['High'].plot(figsize=(16,9),c='g',xlim=('2009-11-09','2020-06-01'),ylim=(0,7000))
anom_weeks['Low'].plot(c='r')


# In[73]:


weekly_uk100['High'].quantile([0.5,0.8,0.99])


# In[74]:


weekly_uk100['Low'].quantile([0.5,0.8,0.99])


# In[75]:


anom_low = weekly_uk100[(weekly_uk100['Low'] < 120.1)]


# In[76]:


anom_high = weekly_uk100[(weekly_uk100['High'] < 120.1)]


# In[77]:


anom_low['High'].quantile([0.99])


# In[78]:


anom_high['Low'].quantile([0.99])


# In[79]:


weekly_uk100['High Price'].plot(figsize=(16,9),xlim=('2014-01-01','2014-02-11'),ylim=(60000,69000))
weekly_uk100['Low Price'].plot()

