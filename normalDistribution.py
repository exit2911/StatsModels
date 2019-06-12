"""
import the data
graph the histogram
check normality using D’Agostino’s K^2 test 
find probability random variable X falls under certain range

The D’Agostino’s K^2 test calculates summary statistics from the data, namely kurtosis and skewness, to determine if the data distribution departs from the normal distribution, named for Ralph D’Agostino.

Skew is a quantification of how much a distribution is pushed left or right, a measure of asymmetry in the distribution.
Kurtosis quantifies how much of the distribution is in the tail. It is a simple and commonly used statistical test for normality.

"""



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib
from csv import reader
from scipy.stats import normaltest
import scipy.stats


df = pd.read_csv(r'C:\Users\vyho0\Downloads\weight-height.csv', sep = ',')

df.head()



#convert columns data to numpy array data

x = [] #independent variable is study hour

for i in df['Height']:
    x.append(i)
    
x = np.array(x)

#checking for normality with histogram

plt.hist(x)
plt.ylabel('Count')
plt.xlabel('Height (inches)')

stat, p = normaltest(x)
print('Statistics = %.3f, p = %.3f' % (stat, p))

alpha = .05

if p > alpha:
    print('Sample looks Gaussian')
else:
    print('Sample doesn\'t look Gaussian')


#Since normality test shows normal, we can proceed to solve some normal curve problems
#Shows descriptive statistics

df.describe()

mu = 69.026346

sigma =  2.863362   



#scipy.stats.norm(mean,standarddeviation).cdf(x) to get the probability of x falling in a range


cdf = scipy.stats.norm(mu,sigma).cdf(74)

print("probability of men being less than 74 ft = %.3f" %(cdf*100),"%")
    

