import pandas as pd

"""
How do I remove columns from pandas dataframe?
"""

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())

#remove single column 'Colors Reported'
ufo.drop('Colors Reported', axis=1, inplace=True)
print(ufo.head())

#remove more columns in dataframe
ufo.drop(['City', 'Shape Reported'], axis=1, inplace=True)
print(ufo.head())

# remove first two rows
ufo.drop([0,1,2], inplace=True)
print(ufo.head())
