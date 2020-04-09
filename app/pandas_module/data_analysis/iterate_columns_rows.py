import pandas as pd

orders = pd.read_table('http://bit.ly/chiporders')
print(orders.head(n=5))

# Iterate one by one column(header) from dataframe
for column in orders:
    print(column)

# Iterate one by one row  from dataframe
for index, row in orders.iterrows():
    print(index, row)

#Iterate each row item_price column value one by one
for index, row in orders.iterrows():
    print(row['item_price'])

# Itearte each row third column(item_name) value one by  one
for index, row in orders.iterrows():
    print(row[2])

