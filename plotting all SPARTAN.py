# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 04:29:38 2017

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

datelist = (df['start_year'].astype(str)+df['start_month'].astype(str)+df['start_day'].astype(str)).tolist()
datetime2 = pd.to_datetime(arg = datelist, format = '%Y%m%d')
df3 = pd.DataFrame({'Datetime': datetime2})
result = df.join(df3)

Time = result["Datetime"]
BC = result["SSR_BC"]
SO4 = result["IC_SO4"]
NH4 = result["IC_NH4"]

df4 = pd.DataFrame({'Time': Time, 'BC': BC, 'SO4': SO4, 'NH4': NH4})

fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(111)
ax.plot_date(x=df4.Time, y=df4.BC, marker='o', color = 'red')
plt.title('BC, SO4, and NH4 in Singapore (SPARTAN)')
plt.legend(loc=1)

locs, labels = plt.xticks()
plt.setp(labels, rotation=45)

ax1=ax.twinx()
ax1.plot_date(x=df4.Time, y= df4.SO4, marker="o", color = 'black')
##ax1.set(ylabel="PM25 measurements")
plt.legend(loc=2)

ax2=ax1.twinx()
ax2.plot_date(x=df4.Time, y=df4.NH4, marker='o', color="green")
plt.legend(loc=3)
