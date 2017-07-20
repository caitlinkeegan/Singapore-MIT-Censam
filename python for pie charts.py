# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:30:57 2017

@author: caitl
"""
import pandas as pd 
import matplotlib as mpl
mpl.rcParams['font.size'] = 35.0
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as DT
from dateutil.parser import parse
from pylab import *
df = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\Bandung under limit.csv', 'r', delimiter = ',')

m1 = (df['SSR_BC'].mean())
m2 = (df['IC_Cl'].mean())
m3 = (df['IC_NO3'].mean())
m4 = (df['IC_PO4'].mean())
m5 = (df['IC_SO4'].mean())
m6 = (df['IC_Na'].mean())
m7 = (df['IC_NH4'].mean())
m8 = (df['IC_K'].mean())
m9 = (df['IC_Mg'].mean())    #divide by 1000 here
m10 = (df['ICP_Al'].mean()/1000)
m11 = (df['ICP_Fe'].mean()/1000)
m12 = (df['ICP_Ti'].mean()/1000)
m13 = (df['ICP_TEO'].mean()/1000)
m14 = (df['ICP_Zn'].mean()/1000)

thesum=(m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11+m12+m13+m14)
unknowns = [m1/thesum, m2/thesum, m3/thesum, m4/thesum, m5/thesum, m6/thesum, m7/thesum, m8/thesum, m9/thesum, m10/thesum, m11/thesum, m12/thesum, m13/thesum, m14/thesum]
print("BC is {}, Cl is {}, NO3 is {}, PO4 is {}, SO4 is {}, Na is {}, NH4 is {}, K is {}, Mg is {}, Al is {}, Fe is {}, Ti is {}, TEO is {}, Zn is {}".format(*unknowns))




figure(1, figsize=(6,6))
ax = axes([0.2, 0.2, 1.6, 1.6])
labels = 'BC', '', 'NO3', 'PO4', 'SO4', 'Na', 'NH4', 'K', '', '', '', '', 'TEO', ''
fracs = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14]  ##out of 100, need to divide by 100 and make sure all the same units

#patches, texts = plt.pie(fracs, labels=labels, autopct='%1.1f%%', startangle=90, radius=1.2)
#new_labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, fracs)]
#
#sort_legend = True
#if sort_legend:
#    patches, new_labels, dummy =  zip(*sorted(zip(patches, labels, fracs),
#                                          key=lambda x: x[2],
#                                          reverse=True))
#
#plt.legend(patches, new_labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
#           fontsize=8)
#
#plt.savefig('piechart.png', bbox_inches='tight')       
#        
        
        
        
        
#        
pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

#plt.legend( loc = 'right', labels=['%s, %1.1f %%' % (l,s) for l, s in zip(labels, fracs)])





##title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
#
##show()
#
#df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\Bandung under limit.csv', 'r', delimiter = ',')
#am1 = (df1['SSR_BC'].mean())
#am2 = (df1['IC_Cl'].mean())
#am3 = (df1['IC_NO3'].mean())
#am4 = (df1['IC_PO4'].mean())
#am5 = (df1['IC_SO4'].mean())
#am6 = (df1['IC_Na'].mean())
#am7 = (df1['IC_NH4'].mean())
#am8 = (df1['IC_K'].mean())
#am9 = (df1['IC_Mg'].mean())
#am10 = (df1['ICP_Al'].mean())
#am11 = (df1['ICP_Fe'].mean())
#am12 = (df1['ICP_Ti'].mean())
#am13 = (df1['ICP_TEO'].mean())
#am14 = (df1['ICP_Zn'].mean())
#
#figure(1, figsize=(6,6))
#ax = axes([0.2, 0.2, 1.6, 1.6])
#
#labels = 'BC', 'Cl', 'NO3', 'PO4', 'SO4', 'Na', 'NH4', 'K', 'Mg', 'Al', 'Fe', 'Ti', 'TEO', 'Zn'
#fracs = [am1, am2, am3, am4, am5, am6, am7, am8, am9, am10, am11, am12, am13, am14]
#
#pie = plt.pie(fracs, labels=labels,autopct='%1.1f%%', shadow=False, startangle=90)
#plt.legend( loc = 'right', labels=['%s, %1.1f %%' % (l,s) for l, s in zip(labels, fracs)])