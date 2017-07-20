# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:24:22 2017

@author: caitl
"""

import os
import glob
import pandas as pd
import datetime as dt
import numpy as np


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Jakarta Observatory, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Jakarta PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Jakarta PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Jakarta TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Jakarta TEMP STD'})
#
main_dataframe = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])

df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Bangkok, Thailand.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Bangkok PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Bangkok PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Bangkok TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Bangkok TEMP STD'})
#
main_dataframe2 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Ho Chi Minh City, Vietnam.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Ho Chi Minh PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Ho Chi Minh PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Ho Chi Minh TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Ho Chi Minh TEMP STD'})
#
main_dataframe3 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Singapore, Singapore.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Singapore PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Singapore PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Singapore TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Singapore TEMP STD'})
#
main_dataframe4 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Yangon, Myanmar.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Yangon PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Yangon PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Yangon TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Yangon TEMP STD'})
#
main_dataframe5 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Surabaya, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Surabaya PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Surabaya PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Surabaya TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Surabaya TEMP STD'})
#
main_dataframe6 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Quezon City, Philippines.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Quezon City PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Quezon City PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Quezon City TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Quezon City TEMP STD'})
#
main_dataframe7 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Bandung, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Bandung PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Bandung PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Bandung TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Bandung TEMP STD'})
#
main_dataframe8 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Medan, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Medan PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Medan PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Medan TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Medan TEMP STD'})
#
main_dataframe9 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Tangerang, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Tangerang PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Tangerang PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Tangerang TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Tangerang TEMP STD'})
#
main_dataframe10 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Hai Phong, Vietnam.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Hai Phong PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Hai Phong PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Hai Phong TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Hai Phong TEMP STD'})
#
main_dataframe11 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Manila, Philippines.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Manila PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Manila PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Manila TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Manila TEMP STD'})
#
main_dataframe12 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Semarang, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Semarang PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Semarang PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Semarang TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Semarang TEMP STD'})
#
main_dataframe13 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Palembang, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Palembang PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Palembang PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Palembang TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Palembang TEMP STD'})
#
main_dataframe14 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])

df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Kuala Lumpur, Malaysia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Kuala Lumpur PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Kuala Lumpur PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Kuala Lumpur TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Kuala Lumpur TEMP STD'})
#
main_dataframe15 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])




df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\South Tangerang, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'South Tangerang PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'South Tangerang PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'South Tangerang TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'South Tangerang TEMP STD'})
#
main_dataframe16 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Makassar, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Makassar PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Makassar PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Makassar TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Makassar TEMP STD'})
#
main_dataframe17 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Phom Penh, Cambodia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1["YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Phnom Penh PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Phnom Penh PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Phnom Penh TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Phnom Penh TEMP STD'})
#
main_dataframe18 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Batam, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Batam PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Batam PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Batam TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Batam TEMP STD'})
#
main_dataframe19 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Pekan Baru, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Pekan Baru PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Pekan Baru PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Pekan Baru TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Pekan Baru TEMP STD'})
#
main_dataframe20 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Bogor, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Bogor PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Bogor PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Bogor TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Bogor TEMP STD'})
#
main_dataframe21 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])





df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Da Nang, Vietnam.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Da Nang PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Da Nang PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Da Nang TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Da Nang TEMP STD'})
#
main_dataframe22 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Bandar Lampung, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Bandar Lampung PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Bandar Lampung PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Bandar Lampung TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Bandar Lampung TEMP STD'})
#
main_dataframe23 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Mandalay, Myanmar.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Mandalay PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Mandalay PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Mandalay TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Mandalay TEMP STD'})
#
main_dataframe24 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Padang, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Padang PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Padang PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Padang TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Padang TEMP STD'})
#
main_dataframe25 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])




df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Cebu City, Philippines.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Cebu City PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Cebu City PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Cebu City TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Cebu City TEMP STD'})
#
main_dataframe26 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Denpasar, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Denpasar PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Denpasar PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Denpasar TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Denpasar TEMP STD'})
#
main_dataframe27 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Zamboanga City, Philippines.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Zamboanga City PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Zamboanga City PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Zamboanga City TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Zamboanga City TEMP STD'})
#
main_dataframe28 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])





df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Ipoh, Malaysia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Ipoh PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Ipoh PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Ipoh TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Ipoh TEMP STD'})
#
main_dataframe29 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Taguig, Philippines.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Taguig PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Taguig PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Taguig TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Taguig TEMP STD'})
#
main_dataframe30 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Tasikmalaya, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Tasikmalaya PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Tasikmalaya PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Tasikmalaya TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Tasikmalaya TEMP STD'})
#
main_dataframe31 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Banjarmasin, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Banjarmasin PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Banjarmasin PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Banjarmasin TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Banjarmasin TEMP STD'})
#
main_dataframe32 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])




df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Balikpapan, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Balikpapan PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Balikpapan PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Balikpapan TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Balikpapan TEMP STD'})
#
main_dataframe33 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Serang, Indonesia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Serang PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Serang PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Serang TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Serang TEMP STD'})
#
main_dataframe34 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])



df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Petaling Jaya, Malaysia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Petaling Jaya PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Petaling Jaya PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Petaling Jaya TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Petaling Jaya TEMP STD'})
#
main_dataframe35 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])


df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Kuching, Malaysia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP  ']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

            
datetime1 = pd.to_datetime(arg = df1[" YEARMODA"], yearfirst = True, format = "%Y%m%d", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])

g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Kuching PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Kuching PRCP STD'})

temp_monthly_avg = g.aggregate({'   TEMP': np.mean}).rename(columns={'   TEMP': 'Kuching TEMP MEAN'})
temp_std = g.aggregate({'   TEMP':  np.std}).rename(columns={'   TEMP': 'Kuching TEMP STD'})
#
main_dataframe36 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])






final_frame = main_dataframe2.join([main_dataframe, main_dataframe3, main_dataframe4, main_dataframe5, main_dataframe6, main_dataframe7, main_dataframe9, main_dataframe10, main_dataframe11, main_dataframe12, main_dataframe13, main_dataframe14, main_dataframe16, main_dataframe17, main_dataframe18, main_dataframe19, main_dataframe20, main_dataframe21, main_dataframe22, main_dataframe23, main_dataframe24, main_dataframe25, main_dataframe26, main_dataframe27, main_dataframe28, main_dataframe29, main_dataframe30, main_dataframe31, main_dataframe32, main_dataframe33, main_dataframe34, main_dataframe35, main_dataframe36])
final_frame.to_csv('C:\\Users\\caitl\\Documents\\CENSAM\\Final Frame.csv')





