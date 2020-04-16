import pandas as pd
import os
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday

class MyOwnHolidayCalendar(AbstractHolidayCalendar):
    ##obeervance is using to if holiday is in weekend then nearest working day will be as holiday
    # as well
    rules =[
        Holiday("birthday",month=4, day=19, observance=nearest_workday)
    ]


def get_dataframe(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '../storage/AAPL_v3.csv')
    print(file_path)
    df = get_dataframe(file_path)
    print(df.head())

    #creation time range to consider us holiday as well at 4th july(independence day)
    us_daterange = CustomBusinessDay(calendar=USFederalHolidayCalendar()) # exclude weekends as
    # well as us holidays
    create_daterange = pd.date_range(start='2017-07-01', end='2017-07-21', freq=us_daterange)

    df.set_index(create_daterange, inplace=True)
    print(df.head())

    #custom holiday calendar frequency
    myown_cal = CustomBusinessDay(calendar=MyOwnHolidayCalendar())
    custom_daterange = pd.date_range(start='2020-04-01', end='2020-04-2', freq=myown_cal)
    print(custom_daterange)

    #Get daterange where friday and saturday is holliday
    image_cal = CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu')
    date_range = pd.date_range(start='2020-04-01', end='2020-04-20', freq=image_cal)
    print(date_range)

    #Get daterange where friday and saturday is holliday and 1th & 2th april is holliday
    image_cal = CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu', holidays=['2020-04-01',
                                                                            '2020-04-02'])
    date_range = pd.date_range(start='2020-04-01', end='2020-04-20', freq=image_cal)
    print(date_range)
