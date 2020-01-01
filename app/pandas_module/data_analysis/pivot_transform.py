import pandas as pd
import os

"""
Use of pivot function in pandas dataframe??
Answer: Pivot allows you to transform & reshape data.
        It allows you to changes index rows & header 
        values to reshape & get ne transform dataframe  
"""

read_path = os.path.join(os.path.dirname(__file__), '../storage/weather_v1.csv')

original_df = pd.read_csv(read_path)
print("Original Dataframe::\n", original_df)

df = original_df.pivot(index='date', columns='city')
print("Dataframe after changes of index as date & header column value as city names::\n",df)

df = original_df.pivot(index='date', columns='city', values=['temperature'])
print("Get transform dataframe only for temperature column::\n", df)

