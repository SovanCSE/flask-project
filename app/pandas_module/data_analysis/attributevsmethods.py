import pandas as pd

"""
Why do some of pandas commands end with parentheses or others not?
Answer: Main cause is which are not having parentheses at end they are 
        attibutes(describe the dataframe propertics) & which are having parentheses
        at end they are methods(provide action on dataframe)
"""

movies = pd.read_csv('http://bit.ly/imdbratings')
#dataframe with attributes
print(movies.shape)
print(movies.dtypes)
print(movies.columns)
#dataframe with functions
print(movies.head())
print(movies.describe())
print(movies.describe(include=[object]))
