'''
2 sample t test (paired, dependent, df = n-1)

investigating whether or not vitamin c reduces the frequency of common colds

sample: pairs of children from the same family. one taking vitamin c and one taking fake vitamin c 
(paired, dependent, df = n - 1)

test the null hypothesis at the 0.05 level of significance

h0: vitamin c doesn't reduce the number of cold children get per year (mean difference >= 0)
h1: vitamin c reduces  the number of cold children get per year (mean difference < 0)

'''


import math as m
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib
from csv import reader
import csv
from scipy.stats import normaltest
import scipy.stats



df = pd.read_csv(r'/Users/VyHo/Downloads/vitaminc.csv', sep = ',')

df.head()

df['difference']= df['vitamin_c'] - df['fake_vitamin_c']

#column sums
df.sum(axis=0) 

#find sample mean and standard deviation for difference 

df['difference'].describe()

mean =  -1.500000
std = 1.269296

#Studnt, df=9, p<0.05, single tail
#t critical value is negative because we are testing the left side of the hypo mean (0)
t_critial_value = print(-stats.t.ppf(1-0.05, 9))

standar_error = std/m.sqrt(10)

t_test= (mean - 0)/standar_error

'''
since t_test value is less than t critical value, reject the null hypo.

conclusion: study shows that vitamin c reduces the numbers of colds children from the same households get per year 
'''
