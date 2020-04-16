import pandas as pd
import  os
# from matplotlib

"""
Time series analytics in pandas:
  Time series is a set of data points indexed in time order.
  
Several topic are:
 1. DatetimeIndex
 2. Resampleling  
"""

if __name__ == "__main__":
    read_path = os.path.join(os.path.dirname(__file__),'../storage/AAPL.csv')
    df = pd.read_csv(read_path, parse_dates=['Date'], index_col='Date')

    #Retrieve only January 20 stock prices
    # print(df['2020-01'])

    #What is the average prices of apple's stock in january 2020
    # print(df['2020-01'].mean())

    #Retrieve between january 1 or 7 data in 2020
    # print(df['2020-01-01':'2020-01-07'])

    #resamping close price with month wise to get mean results
    # print(df.Close.resample('M').mean())

    # resamping all prices with quater wise to get mean results
    print(df.resample('Q').mean())


