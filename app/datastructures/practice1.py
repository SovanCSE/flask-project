
with open('stock_prices.csv') as f:
    stock_prices =[]
    for line in f:
        tokens = line.split(',')
        date = tokens[0]
        price = float(tokens[1])
        stock_prices.append([date,price])

print(stock_prices)