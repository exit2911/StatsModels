'''
example

k: group
n: sample size
dfbetween = group - 1
dfwithin = n - group 
dftotal = dfbetween + dfwithin

alpha: level of significant 

H0: sample mean 1 = sample mean 2 = sample mean 3
H1: there is a least one difference between the means


'''
import scipy.stats as stats

a = [1,2,5]
b = [2,4,2]
c = [2,3,4]

#get F value : stats.f_oneway(array1,array2,array3)
print(stats.f_oneway(a,b,c))

#get F critical value : stats.f.ppf(q=1-alpha, dfn=dfbetween, dfd=dfwithin)
print(stats.f.ppf(q=1-0.05, dfn=2, dfd=6))

#F value is less than F critical value. fail to reject H0

