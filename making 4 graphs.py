# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 23:20:11 2017

@author: caitl
"""
import matplotlib as mpl
mpl.rcParams['font.size'] = 20.0
import pandas as pd
import itertools
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import datetime as DT
import math

df = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\PM25_Singapore.csv', 'r', delimiter = ',')

df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\Converted\\All_four_species_all_3_years.csv', 'r', delimiter = ',')
datearray1 = df1.as_matrix(columns=df1.columns[:1]).tolist()
da1 = list(itertools.chain(*datearray1))   

datetime1 = pd.to_datetime(arg = da1, format = '%Y%m%d')
print(df1.describe())

fig,ax = plt.subplots(figsize=(14,7))
ax.scatter(x=datetime1,y=df1["PM25M"],marker="o",s=10, color = "red")
plt.title('Singapore Trends')
ax.set(xlabel="Dates", ylabel="PM25 measurements")
plt.legend(loc=1)



# In[128]:


ax1=ax.twinx()
ax1.scatter(x=datetime1,y=df1["COM"],marker="o",s=10, color = 'black')
ax1.set(ylabel="CO measurements")
plt.legend(loc=2)




# In[129]:

ax2=ax1.twinx()
ax2.scatter(x=datetime1,y=df1["NO2M"],marker="o",s=10, color = 'g')
ax2.set(ylabel="NO2 measurements")
plt.ylim(0,1000)
plt.legend(loc=3)




# In[130]:

ax3=ax2.twinx()
ax3.scatter(x=datetime1,y=df1["SO2M"],marker="o",s=10, color = 'c')
ax3.set(ylabel="SO2 measurements")
plt.ylim(0,50)
plt.legend(loc=4)

plt.show()