import pandas as pd
import numpy as np

"""
Use of replace function in pandas dataframe ?
"""

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())

#Replace some value with some other values in everywhere
ufo.replace({'Ithaca':'Kolkata', 'Holyoke': 'Mumbai'}, inplace=True)
print(ufo.head())

#Repalce some old value with new value but column wise
ufo.replace({'Colors Reported':None,'City':None},'Comming Soon', inplace=True)
print(ufo.head())

#Replace some old value with new value everywhere
ufo.replace('Comming Soon',np.NaN, inplace=True)
print(ufo.head())

#Replace old value with ne value as sequence wise
ufo.replace(['Kolkata','Mumbai'],['Abilene','Willingboro'], inplace=True)
ufo.head()

# ufo.replace('[A-Za-z]','', regex=True)