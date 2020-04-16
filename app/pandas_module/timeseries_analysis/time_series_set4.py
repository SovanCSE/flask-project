import pandas as pd
import  os
#Us date format: mm/dd/yyyy
#Europe date format: dd/mm/yyyy
##Pandas normally understand mm/dd/yyyy format

def get_dataframe(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '../storage/AAPL_v4.csv')
    print(file_path)
    df = get_dataframe(file_path)
    #using to_datetime fuction to convert Date column as datetime object and set as index
    print(type(df['Date'][0]))
    df['Date'] = pd.to_datetime(df["Date"], format='%Y-%m-%d')
    print(type(df['Date'][0]))
    df.set_index('Date', inplace=True)
    print(df.head())

    #converting list of string format into datetime object in pandas
    date_list = ['2017-01-15 2:10:00 AM','Jan 15, 2017 12:00:00 PM', '2017/01/15 12:00:00 PM','2017.01.15',
                 '01/15/2017','20170115']

    date_range = pd.to_datetime(date_list)
    print(date_range)

    #in eupore 5th january be like 05/01/2017
    europe_date = pd.to_datetime('05/01/2017', dayfirst=True)
    print(europe_date)

    #with custom format
    europe_date_v2 = pd.to_datetime('05##01$$2017', format='%d##%m$$%Y')
    print(europe_date_v2)

    date_list = ['2017-01-15 2:10:00 AM', 'Jan 15, 2017 12:00:00 PM', '2017/01/15 12:00:00 PM',
                 '2017.01.15',
                 '01/15/2017', '20170115','abc']

    #date_list with wrong format then don't convert at all
    date_format_v1 = pd.to_datetime(date_list, errors='ignore')
    print(date_format_v1)

    #date_list with wrong format then convert all other date without wrong one.
    date_format_v2 = pd.to_datetime(date_list, errors='coerce')
    print(date_format_v2)

    #Epoch (unix time) is number of seconds that have passed since Jan 1,1970 00:00:00 UTC
    convert_from_epochtime_v1 = pd.to_datetime(1587748358, unit='s')
    print(convert_from_epochtime_v1)

    #same date convert back into epoch
    convert_from_epochtime_v2 = pd.to_datetime([1587748358], unit='s')
    print(convert_from_epochtime_v2)
    convert_back_toepoch_time = convert_from_epochtime_v2.view('int64')
    print(convert_back_toepoch_time)





