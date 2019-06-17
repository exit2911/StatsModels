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
from scipy.stats import normaltest
import scipy.stats


df = pd.read_csv(r'/Users/VyHo/Downloads/scores.csv', sep = ',')

df.head()

"""

#convert columns data to numpy array data

x = [] #independent variable is study hour

for i in df['Height']:
    x.append(i)
    
x = np.array(x)

"""

total_scores = df['Average Score (SAT Math)'] + df['Average Score (SAT Reading)'] + df['Average Score (SAT Writing)']


df['Total_Scores'] = total_scores

df = df.dropna(subset=['Total_Scores'])

df.shape

plt.hist(df['Total_Scores'] )
plt.ylabel('Counts')
plt.xlabel('Average 2015 NYC SAT Scores (Math,Reading,Writing)')

df['Total_Scores'] .describe()

x = df['Total_Scores'] 

stat, p = normaltest(x)
print('Statistics = %.3f, p = %.3f' % (stat, p))

alpha = .05

if p > alpha:
    print('Sample looks Gaussian')
else:
    print('Sample doesn\'t look Gaussian')
    
#since average test scores from NYC schools don't follow a normal distribution. We cannot use the z-test
    
