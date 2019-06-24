"""
z test

average test score for 2015
http://money.com/money/4017881/average-sat-scores-2015/

attempted to compare NYC average SAT scores to the nation average, but the averages don't follow a normal distribution
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib
from csv import reader
import csv
from scipy.stats import normaltest
import scipy.stats
'''
df = pd.read_csv(r'/Users/VyHo/Downloads/scores.csv', sep = ',')

df.head()


total_scores = df['Average Score (SAT Math)'] + df['Average Score (SAT Reading)'] + df['Average Score (SAT Writing)']


df['Total_Scores'] = total_scores

df = df.dropna(subset=['Total_Scores'])

df.shape

plt.hist(df['Total_Scores'] )
plt.ylabel('Counts')
plt.xlabel('Average 2015 NYC SAT Scores (Math,Reading,Writing)')
plt.show()
df['Total_Scores'] .describe()

x = df['Total_Scores'] 

stat, p = normaltest(x)
print('Statistics = %.3f, p = %.3f' % (stat, p))

alpha = .05

if p > alpha:
    print('SAT Sample looks Gaussian')
else:
    print('SAT Sample doesn\'t look Gaussian')
    
#since average test scores from NYC schools don't follow a normal distribution. We cannot use the z-test
    


temp_file = pd.read_csv(r'/Users/VyHo/Downloads/GlobalLandTemperaturesByCountry.csv', sep = ',')

temp_file.head()

temp_file = temp_file[temp_file.Country == 'United States'] #drop data that are not from the U.S.
temp_file = temp_file.dropna()

plt.hist(temp_file)
plt.ylabel('Degree (C)')
plt.xlabel('Days)')

plt.show()


temp_file['AverageTemperature'].describe()

degree = temp_file['AverageTemperature']
stat, p = normaltest(degree)
print('Statistics = %.3f, p = %.3f' % (stat, p))

alpha = .05

if p > alpha:
    print('Sample looks Gaussian')
else:
    print('Sample doesn\'t look Gaussian')


sp500 = pd.read_csv(r'/Users/VyHo/Downloads/SP500.csv', sep = ',')

sp500.head()

sp500 = sp500['Close']
prices = pd.DataFrame(sp500)
returns = prices[:-1].values / prices[1:] - 1


plt.plot(returns)
plt.ylabel('Returns')
plt.xlabel('Days')


plt.show()


x = returns

stat, p = normaltest(x)
print('Statistics = %.3f, p = %.3f' % (stat, p))

alpha = .05

if p > alpha:
    print('Sample looks Gaussian')
else:
    print('Sample doesn\'t look Gaussian')
'''


athlete = pd.read_csv(r'/Users/VyHo/Downloads/athlete.csv', sep = ',')

athlete.head()

#dropping female heights

athlete = athlete[(athlete['Sex'] != 'F')]

athlete = athlete.dropna(subset=['Height'])

height = athlete['Height']


plt.hist(height)
plt.ylabel('Count')
plt.xlabel('Height cm')
plt.show()


x = height

stat, p = normaltest(x)
print('Statistics = %.3f, p = %.3f' % (stat, p))

alpha = .05

if p > alpha:
    print('Sample looks Gaussian')
else:
    print('Sample doesn\'t look Gaussian')
    
height.describe()

df = pd.read_csv(r'/Users/VyHo/Downloads/weight-height.csv', sep = ',')

df.head()


maleHeight = df['Height']* 2.54

maleHeight.describe()


#research question: does the mean of general male population height differs from olympic male athlete height?
