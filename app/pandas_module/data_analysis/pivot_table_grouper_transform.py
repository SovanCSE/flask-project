import pandas as pd
import os

"""
Use of pivot_table function in pandas dataframe??
Answer:
"""

read_path = os.path.join(os.path.dirname(__file__), '../storage/weather_v3.csv')

original_df = pd.read_csv(read_path)
print("Original Dataframe::\n", original_df)

#Convering date column values from string to datetime object
original_df['date'] = pd.to_datetime(original_df['date'])
df = original_df.pivot_table(index=pd.Grouper(freq='M',key='date'), columns='city')
print('Transform dataframe with aggregate with month wise::\n', df)

