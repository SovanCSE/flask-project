import pandas as pd

"""
What is multi index concept?
 Answer: MultiIndex is nothing but a dataframe having more than one index columns.
"""

df = pd.read_csv('http://bit.ly/smallstocks')
print("stock dataframe::\n", df)
print("Get Index info::\n",df.index)

#Get mean closing price for each symbol(each company)
series1 = df.groupby(['Symbol','Date'])['Close'].mean()
print("Mean Price of each Symbol as series::\n", series1)
print("Get Index info::\n", series1.index)

#Convert series to dataframe in pandas
print("Series::\n", type(series1))
print("way1 Dataframe::\n", type(series1.unstack()))
print("way2 Dataframe::\n", type(series1.to_frame()))
print("Show Dataframe 1 covert series to dataframe::\n", series1.to_frame())
df1 = series1.unstack()
print("Show Dataframe 2::\n", df1)
df2 = df.pivot_table(values='Close', index='Symbol', columns='Date')
print("Show same as above dataframe::\n", df2)

##Select statement on multi index series
print("Get all AAPL series data::\n", series1.loc['AAPL'])
print("Gell AAPL series data with specific date::\n", series1.loc['AAPL','2016-10-03'])
print("Get all symbol data at perticular date::\n", series1.loc[:,'2016-10-03'])

##Set Multi index means Symbol & Date as index from stocks dataframe
stocks = df
stocks.set_index(['Symbol', 'Date'], inplace=True)
stocks.sort_index(inplace=True)
print("Multi index dataframe::\n", stocks)
print("Get Index info::\n", stocks.index)