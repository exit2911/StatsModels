'''
one sample t test

regardless of population distribution, central limit theorem says samples drawn

from the bigger sample are approximately normal. drawn number should be at least 10

use t test when sample size is less than 30

standard deviation is unknown

(sampleMean - hypoMean)/(sampleStandardDev/m.sqrt(100))

t critical value determined by df= n -1

use wilcoxon t test if cant assume normality

'''
import math as m
from scipy import stats
#Studnt, n=999, p<0.05, 2-tail

print(stats.t.ppf(1-0.025, 999))

#Studnt critical value, n=6, p<0.01%, Single tail
#df = 5

print(stats.t.ppf(1-0.01, 5))

'''
does the mean gas milage for some population of cars drop below the legally required min
of 45 mpg?

h0: mean >= 45
h1: mean < 45
'''

a= [40,44,46,41,43,44]
b = pd.DataFrame(np.array(a).reshape(6,1), columns = list("a"))
b.describe()

mean = 43
hypo_mean = 45
std = 2.19089
std_erro = std/m.sqrt(6)
#sample mean less than hypo_mean, t critical value will be negative

t_critical_value = - stats.t.ppf(1-0.01, 5)

t = (mean-hypo_mean)/std_erro


#t value is greater than t critical value, so cannot reject null hypo
#the mean gas milage for some population of cars isnt below the legally required min
#of 45 mpg
