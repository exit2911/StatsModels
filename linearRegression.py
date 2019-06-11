#linear regression


import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib

#load the excel

file = "/Users/VyHo/Downloads/linearRegression.xlsx"

df = pd.read_excel(file)

#convert columns data to numpy array data

x = [] #independent variable is study hour

for i in df['study hours']:
    x.append(i)
    
x = np.array(x)

y = [] #dependent variable is grade

for i in df['grade']:
    
    y.append(i)

y = np.array(y)
#linear regression plot with fitted line
    
df = pd.DataFrame({'Grade':y, 'Study Hours':x})
sns.regplot('Study Hours','Grade',data = df)
plt.show()

A = np.vstack([x, np.ones(len(x))]).T

m, c = np.linalg.lstsq(A, y)[0]


print('Fitted Line : ', 'y = ',m,'x + ',c)

plt.plot(x, y, 'o', label='Original data', markersize=8)
plt.plot(x,m*x+c, 'r', label='Fitted line')
plt.legend()
plt.ylabel('Grade')
plt.xlabel('Hours Studied')
plt.show()
