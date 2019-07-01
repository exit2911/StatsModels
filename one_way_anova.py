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



'''

EXAMPLE # 2

alpha = 0.05

H0: mean sample 0 = mean sample 24 = mean sample 48
H1: there is at least one difference in aggression score mean
    
    
    
'''
#agression scores

zero = [0,4,2] #group deprived of sleep for 0 hrs
twenty_four = [3,6,6] #group deprived of sleep for 24 hrs
forty_eight = [6,8,10] #group deprived of sleep for 48 hrs


#get F value : stats.f_oneway(array1,array2,array3)
print(stats.f_oneway(zero,twenty_four,forty_eight))

#get F critical value : stats.f.ppf(q=1-alpha, dfn=dfbetween, dfd=dfwithin)
print(stats.f.ppf(q=1-0.05, dfn=2, dfd=6))

#F value is greater than F critical value. reject H0

