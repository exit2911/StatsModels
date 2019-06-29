'''
one sample t test

regardless of population distribution, central limit theorem says samples drawn

from the bigger sample are approximately normal. drawn number should be at least 10

use t test when sample size is less than 30

standard deviation is unknown

(sampleMean - hypoMean)/(sampleStandardDev/m.sqrt(n))

t critical value determined by df= n -1 

'''


from scipy import stats
#Studnt, df=999, p<0.05, 2-tail

print(stats.t.ppf(1-0.025, 999))

#Studnt critical value, n=6, p<0.01%, Single tail
#df = 5

print(stats.t.ppf(1-0.01, 5))

#Studnt critical value, n=6, p<0.05%, Single tail, 2 sample t test
#df = 5. 
print(stats.t.ppf(1-0.05, 5))
