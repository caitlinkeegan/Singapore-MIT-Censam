# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 23:31:34 2017

@author: caitl
"""

import csv
import itertools

with open('C:\\Users\\caitl\\Documents\\CENSAM\\Converted\\O3_2014_grouped_daily_max_min.txt', 'r') as in_file:
    in_file.split(",")
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    #grouped = itertools.izip(*[lines])
    with open('C:\\Users\\caitl\\Documents\\CENSAM\\Converted\\O3_2014_grouped_daily_max_min_attempt.txt', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('CO 2014'))
        writer.writerows(lines)