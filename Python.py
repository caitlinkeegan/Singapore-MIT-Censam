# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 04:48:25 2017

@author: caitl
"""

import pandas as pd
import itertools
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import datetime as DT
import math

df1 = pd.read_csv('C:\\Users\\caitl\Documents\CENSAM\Danum Valley GAW, Malaysia\Cleaned data\CO2 Daily cleaned.csv', 'r', delimiter = ',')
df2 = pd.read_csv('C:\\Users\\caitl\Documents\CENSAM\Danum Valley GAW, Malaysia\Cleaned data\O3 Daily cleaned.csv', 'r', delimiter = ',')

datearray1 = df1.as_matrix(columns=df1.columns[:1]).tolist()
datearray2 = df2.as_matrix(columns=df2.columns[:1]).tolist()

chemarray1 = df1['CO2'].values
chemarray1 = [ abs(x) for x in chemarray1]
chemarray2 = df2['O3'].values.tolist()
for i in chemarray2:
    float(i)
chemarray2 = [ abs(x) for x in chemarray2]

da1 = list(itertools.chain(*datearray1))   
da2 = list(itertools.chain(*datearray2))

datetime1 = pd.to_datetime(arg = da1, infer_datetime_format = True)
datetime2 = pd.to_datetime(arg = da2, infer_datetime_format = True)

dates1 = mdates.num2date(mdates.drange(DT.datetime(1996, 9, 1),
                                      DT.datetime(2014, 12, 31),
                                      DT.timedelta(days=1)))

newdates = pd.DatetimeIndex(dates1).tz_localize(None)

big_date_frame = pd.DataFrame(data={'DATE':newdates})

big_date_frame = big_date_frame.set_index('DATE')


small_date_frame1 = pd.DataFrame(data={'DATE':datetime1, 'CO2':chemarray1}).set_index('DATE')
small_date_frame2 = pd.DataFrame(data={'DATE':datetime2, 'O3':chemarray2}).set_index('DATE')

result2 = big_date_frame.join(small_date_frame1, how='outer')
result5 = result2.join(small_date_frame2, how='outer')


result5.astype(object).convert_objects()



fig,ax = plt.subplots(figsize=(17,10))
plt.scatter(x=small_date_frame1.index,y=small_date_frame1["CO2"], marker='o', c='r', s=10)
plt.show()

fig,ax = plt.subplots(figsize=(17,10))
plt.scatter(x=small_date_frame2.index,y=small_date_frame2["O3"], marker='o', c='b', s=10)
plt.show()

fig,ax = plt.subplots(figsize=(14,6))
ax.scatter(x=result5.index,y=result5["CO2"],marker='o',c="r", s=10)
plt.title('CO2 and O3 trends over time in Danum Valley GAW, Malaysia')
ax.set(xlabel="Dates", ylabel="CO2 measurements (units)")
plt.legend(loc=1)
ax1=ax.twinx()
ax1.scatter(x=result5.index,y=result5["O3"],marker="o",s=10)
ax1.set(ylabel="O3 measurements (units)")
plt.legend(loc=2)
plt.show()