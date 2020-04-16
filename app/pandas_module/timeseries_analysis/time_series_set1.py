import os
import  pandas as pd
# from matplotlib import pyplot


def get_dataframe(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '../storage/AAPL.csv')
    print(file_path)
    df = get_dataframe(file_path)
    """
     Below following using DatetimeIndex concepts
    """

    #Following below show data records for april, 2019 only
    #print(df['2019-05'])

    #Find average close stock price at apple for month of april, 2019
    #print(df['2019-04'].Close.mean())

    #Get record for particular date using date index
    #print(df['2019-04-15'])

    #Get data between time range
    # print(df['2019-04-15':'2019-04-21'])

    """
    Below following using resampling concepts
    """
    #documentation link:
     #https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
    #Show monthly average for close prices
    print(df.Close.resample('M').mean())
    # Show Quaterly average for close prices
    print(df.Close.resample('Q').mean())
