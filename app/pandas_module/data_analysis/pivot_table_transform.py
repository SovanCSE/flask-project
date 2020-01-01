import pandas as pd
import os

"""
Use of pivot_table function in pandas dataframe??
Answer: Pivot table is used to summarize and aggregate data inside of reshape dataframe. 
"""

read_path = os.path.join(os.path.dirname(__file__), '../storage/weather_v2.csv')

original_df = pd.read_csv(read_path)
print("Original Dataframe::\n", original_df)

df = original_df.pivot_table(index='date', columns='city')#by default aggregate function is mean
print('Transform dataframe with mean aggregate::\n', df)

df = original_df.pivot_table(index='date', columns='city', aggfunc='sum')
print('Transform dataframe with sum aggregate::\n', df)

df = original_df.pivot_table(index='date', columns='city', aggfunc='sum', margins=True)
print('Transform dataframe with sum aggregate & margins true::\n', df)





