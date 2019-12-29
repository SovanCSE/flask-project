import pandas as pd

"""
 Different between read_table & read_csv ??
 Answer: Main different is that read_table default delimiter is 'tab(\t)' 
         but in case of read_csv having default delimiter as ','
"""

"""
 How to select a pandas series from a dataframe?
"""
ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())
print(type(ufo))#pandas.core.frame.DataFrame

#dot notation to select pandas series
print(ufo.City)
print(type(ufo.City))#pandas.core.series.Series

#bucket notation  to select pandas series
print(ufo['Colors Reported'])
print(type(ufo['Colors Reported']))#pandas.core.series.Series

#added new column address to existed dataframe
ufo['Address'] = ufo.City +', '+ ufo.State
print(ufo.head())




