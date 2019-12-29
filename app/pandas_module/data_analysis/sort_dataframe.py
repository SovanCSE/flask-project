import pandas as pd

"""
How do I sort a pandas dataframe or series?
"""

ufo = pd.read_csv('http://bit.ly/imdbratings')

#Sort pandas series values
#sort only single column title values as ascending order
print(ufo.title.sort_values())

#sort only single column title values as descending order
print(ufo.title.sort_values(ascending=False))

#Sort pandas framework
ufo.sort_values(['star_rating', 'title'], ascending=False, inplace=True)
print(ufo.head())




