import  pandas as pd

"""
How do I rename columns in pandas dataframe?
"""

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())

#Rename specified minimum columns using replace function
ufo.rename(columns={'Colors Reported': 'color reported', 'Shape Reported': 'shape reported'}, inplace=True)
print(ufo.head())

#Rename all columns together
ufo.columns = ['City', 'Colors Reported', 'Shape Reported', 'State', 'Time']
print(ufo.head())

#Rename columns  by replace space with underscore with column names
ufo.columns = ufo.columns.str.replace(' ','_')
print(ufo.head())

##Rename column while reading csv file
new_cols = ['city','color','shape', 'state', 'time']
ufo1 = pd.read_csv('http://bit.ly/uforeports', names=new_cols, header=0)
print(ufo1.head())
