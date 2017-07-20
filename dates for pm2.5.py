# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 23:14:23 2017

@author: caitl
"""


import pandas as pd
import matplotlib as mt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

import datetime as DT
from dateutil.parser import parse

#df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\cleaned datas for Bandung.csv', 'r', delimiter = ',')
df = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\PM25_Singapore.csv', 'r', delimiter = ',')
print(df2['PM_conc_ugm3'].describe())


df['date start'] = pd.to_datetime(df['start_day'], yearfirst = True, format = '%Y,%m,%d,%H,')
df['date end'] = pd.to_datetime(df['stop_day'], yearfirst = True, format = '%Y,%m,%d,%H,', errors ='coerce')


new = pd.DataFrame(data={'PM2.5 abs': df2['PM_abs_ug'],'PM conc': df2['PM_conc_ugm3'],'date end':df1['date end'],'date start': df1['date start']}) 

dates1 = mdates.num2date(mdates.drange(DT.datetime(2014, 2, 22, 9),
                                      DT.datetime(2016, 1, 31, 9),
                                      DT.timedelta(days=1)))

newdates = pd.DatetimeIndex(dates1).tz_localize(None)

big_date_frame = pd.DataFrame(data={'DATE':newdates}).set_index('DATE')
start_index = new.set_index('date start')
end_index = new.set_index('date end')
end_index.rename({'PM2.5 abs': 'PM_abs_ug', 'PM conc': 'PM_conc_ugm3', 'date start': 'start date'})

#final = big_date_frame.join(start_index, how='outer')
final = pd.concat([start_index, end_index])
final = final.sort_index()
print(final.describe())


plt.scatter(final.index, final["PM2.5 abs"])
plt.legend(loc=1)
#mt.rcParams.update({'font.size': 18})
#fig, ax1 = plt.subplots(figsize=(9, 5))
#ax1.set_title("Singapore")
#plt.boxplot(df2["PM_conc_ugm3"])
#plt.ylabel("PM 2.5 Concentration")
#plt.legend(loc=1)
#plt.xlabel("Data points")
##loc, labels = plt.xticks()
##plt.setp(labels, rotation=45)
#
#fig = plt.gcf()
#fig.set_size_inches(12, 7)
#fig.savefig('test2png.png', dpi=100)
