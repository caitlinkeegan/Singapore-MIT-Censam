# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 03:08:04 2017

@author: caitl
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

import datetime as DT
from dateutil.parser import parse

#df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\a bit of cleaning pm2.5 dates.csv', 'r', delimiter = ',')
df2 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\PM25_Manila.csv', 'r', delimiter = ',')
#print(df1['date start'].values)


#df1.apply(datetime.strptime(df1['date end'], "%Y,%m,%e,%H,", assume_datetime_format=True), axis=1)

#df1['date end'] = df1['date end'].astype('datetime64[ns]')


#df1['date start'] =df1['date start'].astype('datetime64[ns]')



#df1['date start'] = pd.to_datetime(df1['date start'], yearfirst = True, format = '%Y,%m,%d,%H,')
#df1['date end'] = pd.to_datetime(df1['date end'], yearfirst = True, format = '%Y,%m,%d,%H,', errors ='coerce')


#new = pd.DataFrame(data={'PM2.5 abs': df2['PM_abs_ug'],'PM conc': df2['PM_conc_ugm3'],'date end':df1['date end'],'date start': df1['date start']}) 

#dates1 = mdates.num2date(mdates.drange(DT.datetime(2014, 2, 22, 9),
#                                      DT.datetime(2016, 1, 31, 9),
#                                      DT.timedelta(days=1)))

#newdates = pd.DatetimeIndex(dates1).tz_localize(None)

#big_date_frame = pd.DataFrame(data={'DATE':newdates}).set_index('DATE')
#start_index = new.set_index('date start')
#end_index = new.set_index('date end')
#end_index.rename({'PM2.5 abs': 'PM_abs_ug', 'PM conc': 'PM_conc_ugm3', 'date start': 'start date'})

#final = big_date_frame.join(start_index, how='outer')
#final = pd.concat([start_index, end_index])
#final = final.sort_index()


 
# Plot
plt.pie(, shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()