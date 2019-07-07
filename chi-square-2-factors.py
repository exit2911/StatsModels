'''



2 factor chi square test

initiate an array where elements are observations from different groups

array([group 1],[group 2])

chi2_contingency(array) will return the contigency table (with only expected values) as well as chi square 

result (first element in tuple)

df = (number of row - 1)(number of column - 1) 

python will calculate df. no manual calculations

                
'''


from scipy.stats import chi2_contingency


obs = np.array([[39, 30, 51], [21, 40, 19]])

chi2_contingency(obs)
