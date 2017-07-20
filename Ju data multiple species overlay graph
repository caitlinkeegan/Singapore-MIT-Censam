
# coding: utf-8

# In[1]:

import pandas as pd
import itertools
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import datetime as DT
import math


# In[2]:

df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\Converted\\All_four_species_all_3_years.csv', 'r', delimiter = ',')


# In[3]:

datearray1 = df1.as_matrix(columns=df1.columns[:1]).tolist()
datearray2 = df2.as_matrix(columns=df2.columns[:1]).tolist()
datearray3 = df3.as_matrix(columns=df3.columns[:1]).tolist()
#datearray4 = df4.as_matrix(columns=df4.columns[:1]).tolist()
datearray5 = df5.as_matrix(columns=df5.columns[:1]).tolist()
#datearray6 = df6.as_matrix(columns=df6.columns[:1]).tolist()chemarray1 = df1['CH4'].values


# In[29]:

chemarray1 = df1['CH4'].values
chemarray1 = [ abs(x) for x in chemarray1]
chemarray2 = df2['CO'].values
chemarray2 = [ abs(x) for x in chemarray2]
chemarray3 = df3['CO2'].values
chemarray3 = [ abs(x) for x in chemarray3]
#chemarray4 = df4['NO2'].values
#chemarray4 = [ abs(x) for x in chemarray4]
chemarray5 = df5['O3'].values
chemarray5 = [ abs(x) for x in chemarray5]
#chemarray6 = df6['O3'].values
#chemarray6 = [ abs(x) for x in chemarray6]


# In[30]:

da1 = list(itertools.chain(*datearray1))   
da2 = list(itertools.chain(*datearray2)) 
da3 = list(itertools.chain(*datearray3)) 
#da4 = list(itertools.chain(*datearray4)) 
da5 = list(itertools.chain(*datearray5)) 
#da6 = list(itertools.chain(*datearray6)) 


# In[31]:

datetime1 = pd.to_datetime(arg = da1, infer_datetime_format = True)
datetime2 = pd.to_datetime(arg = da2, infer_datetime_format = True)
datetime3 = pd.to_datetime(arg = da3, infer_datetime_format = True)
#datetime4 = pd.todates1 = mdates.num2date(mdates.drange(DT.datetime(1996, 9, 1),DT.datetime(2014, 12, 31),DT.timedelta(days=1)))_datetime(arg = da4, infer_datetime_format = True)
datetime5 = pd.to_datetime(arg = da5, infer_datetime_format = True)
#datetime6 = pd.to_datetime(arg = da6, infer_datetime_format = True)


# In[32]:

dates1 = mdates.num2date(mdates.drange(DT.datetime(1996, 9, 1),
                                      DT.datetime(2014, 12, 31),
                                      DT.timedelta(days=1)))


# In[33]:

newdates = pd.DatetimeIndex(dates1).tz_localize(None)


# In[34]:

big_date_frame = pd.DataFrame(data={'DATE':newdates})


# In[35]:

small_date_frame1 = pd.DataFrame(data={'DATE':datetime1, 'CH4':chemarray1}).set_index('DATE')
small_date_frame2 = pd.DataFrame(data={'DATE':datetime2, 'CO':chemarray2}).set_index('DATE')
small_date_frame3 = pd.DataFrame(data={'DATE':datetime3, 'CO2':chemarray3}).set_index('DATE')
#small_date_frame4 = pd.DataFrame(data={'DATE':datetime4, 'NO2':chemarray4}).set_index('DATE')
small_date_frame5 = pd.DataFrame(data={'DATE':datetime5, 'O3':chemarray5}).set_index('DATE')
#small_date_frame6 = pd.DataFrame(data={'DATE':datetime6, 'O3':chemarray6}).set_index('DATE')


# In[36]:

big_date_frame = big_date_frame.set_index('DATE')


# In[37]:

result2 = big_date_frame.join(small_date_frame1, how='outer')
result3 = result2.join(small_date_frame2, how='outer')
result4 = result3.join(small_date_frame3, how='outer')
result5 = result4.join(small_date_frame5, how='outer')


# In[38]:

result5.astype(object).convert_objects()


# In[151]:

fig,ax = plt.subplots(figsize=(17,10))
plt.scatter(x=small_date_frame1.index,y=small_date_frame1["CH4"], marker='o', c='r', s=10)
plt.show()


# In[132]:

fig,ax = plt.subplots(figsize=(14,6))
ax.scatter(x=result5.index,y=result5["CH4"],marker='o',c="r", s=10)
plt.title('CH4 and CO2 trends over time in Bukit Koto Tabang, Indonesia')
ax.set(xlabel="Dates", ylabel="CH4 measurements (ppb)")
plt.legend(loc=1)
ax1=ax.twinx()
ax1.scatter(x=result5.index,y=result5["CO2"],marker="o",s=10)
ax1.set(ylabel="CO2 measurements (ppm)")
plt.legend(loc=2)
plt.show()


# In[145]:

df2 = df2.set_index(datetime2)
fig,ax = plt.subplots(figsize=(17,10))
plt.scatter(df2.index,df2["CO"], marker='o', s=10, c='g')
plt.ylim(0,1000)
plt.show()


# In[148]:

df3=df3.set_index(datetime3)
fig,ax = plt.subplots(figsize=(17,10))
plt.scatter(x=df3.index, y=df3["CO2"], marker='o', s=10, c='black')
plt.show()


# In[140]:

df5 = df5.set_index(datetime5)
fig,ax = plt.subplots(figsize=(25,10))
plt.scatter(x=df5.index, y=df5["O3"],marker='o', c='c',s=10)
plt.ylim(0,50)
plt.show()
#yaxis = plt.gca()
#yaxis.set_range(range[0,15])
#plt.ylim(0,15)


# In[127]:

fig,ax = plt.subplots(figsize=(25,10))
ax.scatter(x=result5.index,y=result5["CH4"],marker="o",s=5, color = "red")
plt.title('CH4, CO2, CO, and O3 trends over time in Bukit Koto Tabang, Indonesia')
ax.set(xlabel="Dates", ylabel="CH4 measurements (ppb)")
plt.legend(loc=1)



# In[128]:


ax1=ax.twinx()
ax1.scatter(x=result5.index,y=result5["CO2"],marker="o",s=5, color = 'black')
ax1.set(ylabel="CO2 measurements (ppm)")
plt.legend(loc=2)




# In[129]:

ax2=ax1.twinx()
ax2.scatter(x=result5.index,y=result5["CO"],marker="o",s=5, color = 'g')
ax1.set(ylabel="CO measurements (ppm)")
plt.ylim(0,1000)
plt.legend(loc=3)




# In[130]:

ax1=ax2.twinx()
ax1.scatter(x=result5.index,y=result5["O3"],marker="o",s=5, color = 'c')
ax1.set(ylabel="O3 measurements (ppm)")
plt.ylim(0,50)
plt.legend(loc=4)

plt.show()


# In[ ]:




# In[ ]:



