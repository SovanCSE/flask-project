import pandas as pd
import os
import numpy as np

def get_dataframe(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '../storage/AAPL_v2.csv')
    print(file_path)
    df = get_dataframe(file_path)
    # print(df.head())

    # create_daterange = pd.date_range(start='2019-04-01', end='2020-03-15', freq='B')
    create_daterange = pd.date_range(start='2019-04-01', periods=250, freq='B')
    # print(create_daterange)

    #set index as datetime as index to the existing dataframe
    df.set_index(create_daterange, inplace=True)
    # print(df.head(n=10))

    #get data on weekend as well
    df = df.asfreq('D', method='pad')
    # print(df.head(n=10))

    #get weekly prices
    print(df.asfreq('W', method='pad'))


   # """
   #  Demo series using numpy
   # """
    ts = pd.Series(np.random.randint(1,10, len(create_daterange)), index=create_daterange)
    print(ts.head())
