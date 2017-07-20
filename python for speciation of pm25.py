# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:53:33 2017

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
df = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\Speciation PM25_Hanoi.csv', 'r', delimiter = ',')

m1 = (df['Ammoniated_Sulfate'].mean())
m2 = (df['Ammonium_Nitrate'].mean())
m3 = (df['Crustal_Material'].mean())
m4 = (df['  Residual_Material'].mean())
m5 = (df['Sea_Salt'].mean())
m6 = (df['Equivalent_Black_Carbon'].mean())
m7 = (df['Trace_Element_Oxides'].mean())
m8 = (df['Particle-Bound Water (RH=0.35)'].mean())
#m9 = (df['kappa_volume'].mean())    #divide by 1000 here

thesum=(m1+m2+m3+m4+m5+m6+m7+m8)
unknowns = [m1/thesum, m2/thesum, m3/thesum, m4/thesum, m5/thesum, m6/thesum, m7/thesum, m8/thesum]
print("Ammoniated sulfate is {}, Ammonium Nitrate is {}, Crustal material is {}, TEO is {}, Residual material is {}, Sea salt is {}, Equiv BC is {}, particle bound water is {}".format(*unknowns))




figure(1, figsize=(5,5))
ax = axes([0.2, 0.2, 1.6, 1.6])
labels = 'Ammoniated Sulfate', 'Ammonium Nitrate', 'Crustal Material', 'TEO', 'Residual Material', 'Sea Salt', 'Equiv. Black Carbon', 'Particle-Bound Water'
fracs = [m1, m2, m3, m7, m4, m5, m6, m8]  ##out of 100, need to divide by 100 and make sure all the same units

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