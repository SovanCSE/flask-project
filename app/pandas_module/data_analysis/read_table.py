import pandas as pd
"""
 How to read a tabular data file using pandas? 
"""
orders = pd.read_table('http://bit.ly/chiporders')
orders.head()
movieusers = pd.read_table('http://bit.ly/movieusers', delimiter='|', names=['user_id', 'age', 'gender','occupation','zipcode'])
print(movieusers.head())