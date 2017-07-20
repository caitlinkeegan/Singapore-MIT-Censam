
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime
from dateutil.parser import parse



# In[2]:xx

    #this does the same thing as the below shell but with fewer lines 
#with open('Documents\CENSAM\Bukit Koto Tabang, Indonesia\CO Monthly Mean.csv','r') as f:  ##note:  if this won't open look at string existing already above and then get rid of the first backslash
df = pd.read_csv('C:\\Users\\caitl\Documents\CENSAM\Bukit Koto Tabang, Indonesia\CO Monthly Mean.csv','r')
x_axis = 'DATE'
y_axis = 'CO'
yeet = list(range(22))
yeet[0] = x_axis
yeet[4] = y_axis
    
    #df = pd.DataFrame((l.rstrip().split() for l in f), columns=yeet)


copy_a_df = df.copy()
copy_a_df = copy_a_df.drop(df.index[range(0,37)])    ##remove unnessary columns and rows
copy_a_df = copy_a_df.drop(df.index[range(1,4)], axis=1)
copy_a_df = copy_a_df.drop(df.index[range(5,7)], axis=1)
copy_a_df = copy_a_df.drop(df.index[range(7,10)], axis=1)
copy_a_df = copy_a_df.drop(df.index[10], axis=1) 
 
 # In[ ]:
 
     #here I will attempt to plot this data in a scatterplot
    copy_c_df = copy_a_df.copy()
    copy_c_df = copy_c_df.T
    copy_c_df = copy_c_df.drop(df.index[range(11,22)], axis=0)  #remove unnecessary column
    copy_c_df = copy_c_df.T
    copy_c_df = copy_c_df.drop(df.index[37])
    copy_c_df = copy_c_df.T   #comment this out to plot
 
    copy_d_df = copy_c_df.copy()
    
    for i in copy_d_df[x_axis]:
        pd.to_datetime(copy_d_df[x_axis], infer_datetime_format = True)
    copy_d_df[x_axis] = pd.to_datetime(copy_d_df[x_axis], infer_datetime_format = True)
    print('Keegan')
    #for i in copy_d_df['DATE']:
        #convert_d = datetime.strptime(i, '%Y-%m-%d')
    
    copy_d_df[y_axis] = pd.to_numeric(copy_d_df[y_axis], errors = 'coerce')
 #copy_d_df = copy_d_df.T
    print('Keegan')
    copy_e_df = copy_d_df.copy()
 
 
    #ax = copy_e_df[[x_axis, y_axis]].set_index(x_axis).plot(kind = "area", stacked = False, title = 'CO levels over time in Bukit Koto Tabang, Indonesia',  figsize=(15,8))#uncommented when above is commented out  #doesn't reach this
    #ax.set(xlabel="Time", ylabel="CO measurements (ppm)")
# In[]:
    