
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np


# In[ ]:

with open('dmv504n00.mmd.as.cn.co2.nl.mo.dat','r') as f:
    #next(f) # skip first row
    df = pd.DataFrame(l.rstrip().split() for l in f)
    copy2_df = df.copy()
    copy2_df = copy2_df.drop(df.index[range(0,37)])

print(copy2_df)


# In[1]:

with open('dmv504n00.mmd.as.cn.co2.nl.mo.dat','r') as f:
    #next(f) # skip first row
    df = pd.DataFrame(l.rstrip().split() for l in f)
    copy_a_df = df.copy()
    copy_a_df = copy_a_df.drop(df.index[range(0,37)]) 
    

    copy_b_df = copy_a_df.copy()
    copy_b_df = copy_b_df.drop(df.index[range(1,4)], axis=1)

    copy_c_df = copy_b_df.copy()
    copy_c_df = copy_c_df.drop(df.index[range(5,7)], axis=1)
    
    copy_d_df = copy_c_df.copy()
    copy_d_df = copy_d_df.drop(df.index[range(7,10)], axis=1)
    
    #copy_d_df.index[37] = copy_d_df.index[37].shift(1)
    

print(copy_d_df)


# In[ ]:



