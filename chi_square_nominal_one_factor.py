'''

does the distribution of college student blood types comply with that described in U.S. blood bank bulletin?

'''

import numpy as np
import pandas as pd
import scipy.stats as stats

#finding critical value
# Find the critical value for 95% confidence, and df = groups - 1

crit = stats.chi2.ppf(q = 0.95, df = 3)

df = pd.read_csv('/Users/vyho/Documents/bloodtype.csv', sep = ',')

df.head()
df = df.dropna()

chi = stats.chisquare(f_obs= df['observed'],   # Array of observed counts
                f_exp= df['expected']) 

print(chi)

#since chi square is greater than critical value, rejecting null hypothesis. there is evidence that distribution of general student population differs for U.S. pop
