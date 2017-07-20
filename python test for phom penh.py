# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:21:11 2017

@author: caitl
"""

df1 = pd.read_csv('C:\\Users\\caitl\\Documents\\CENSAM\\NOAA Data Cleaned\\Phnom Penh, Cambodia.csv', 'r', delimiter = ',')

new_list = []
for string in df1['PRCP']:
    for letter in string:
        if letter == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
            string = string[:-1]
            new_list.append(string)
            break
df1["Stripped PRCP"] = new_list


df1['Stripped PRCP'] = df1['Stripped PRCP'].replace('99.9', np.nan)

new_string = []
for string in df1["TEMP"]:
    string = string[:-4]
    new_string.append(string)
    break
df1['TEMP'] = new_string          
datetime1 = pd.to_datetime(arg = df1["YEARMODA,"], yearfirst = True, format = "%Y%m%d,", infer_datetime_format = True)

df1['YEAR'] = datetime1.dt.year
df1['MONTH'] = datetime1.dt.month
   
df1["Stripped PRCP"] = pd.to_numeric(df1["Stripped PRCP"])
df1["TEMP"] = pd.to_numeric(df1["TEMP"])
g = df1.groupby(['YEAR', 'MONTH'])

prcp_monthly_avg = g.aggregate({'Stripped PRCP':  np.mean}).rename(columns={'Stripped PRCP': 'Phnom Penh PRCP MEAN'})
prcp_std = g.aggregate({'Stripped PRCP':  np.std}).rename(columns={'Stripped PRCP': 'Phnom Penh PRCP STD'})

temp_monthly_avg = g.aggregate({'TEMP': np.mean}).rename(columns={'TEMP': 'Phnom Penh TEMP MEAN'})
temp_std = g.aggregate({'TEMP':  np.std}).rename(columns={'TEMP': 'Phnom Penh TEMP STD'})
#
main_dataframe18 = prcp_monthly_avg.join([prcp_std,temp_monthly_avg, temp_std])