# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 23:55:30 2017

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

datelist = (df['stop_year'].astype(str)+df['stop_month'].astype(str)+df['stop_day'].astype(str)).tolist()
datetime2 = pd.to_datetime(arg = datelist, format = '%Y%m%d')
df3 = pd.DataFrame({'Datetime': datetime2})
result = df.join(df3)

datearray1 = df1.as_matrix(columns=df1.columns[:1]).tolist()
da1 = list(itertools.chain(*datearray1))   
datetime1 = pd.to_datetime(arg = da1, format = '%Y%m%d')


#fig,ax = plt.subplots(figsize=(14,7))
#ax.scatter(x=result["Datetime"],y=result["PM_conc_ugm3"],marker="o",s=10, color = "c")
#plt.title('SPARTAN Singapore Trends for PM25')
#ax.set(xlabel="Dates", ylabel="PM25 measurements")


#ax1=ax.twinx()
#ax1.scatter(x=,y=df["PM_conc_ugm3"],marker="o",s=10, color = 'black')
#ax1.set(ylabel="PM25 measurements")
#plt.legend(loc=2)

SINGAPORE = df1["PM25M"]

Time = result["Datetime"]
SPARTAN = result["PM_conc_ugm3"]

df4 = pd.DataFrame({'Time': Time, 'SPARTAN': SPARTAN})

fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(111)
ax.plot_date(x=df4.Time, y=df4.SPARTAN, marker='o', color = 'red')
plt.title('2 Data Set Comparison for Singapore Trends for PM25 (using stop year)')
plt.legend(loc=2)

ax1=ax.twinx()
ax1.scatter(x=datetime1,y= SINGAPORE,marker="o",s=15, color = 'black')
ax1.set(ylabel="PM25 measurements")
plt.legend(loc=1)
