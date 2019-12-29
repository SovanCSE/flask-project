import csv
import os

def read_csv():
    rows = []
    with open('storage/aapl.csv', 'r') as csvfile:
        csvreader=csv.reader(csvfile)
        fields = next(csvreader)
        # print("fields = ",fields)
        for field in fields:
            print('%10s'%field, end=' ')
        print()
        for row in list(csvreader)[:2]:
             rows.append(row)
        # print(rows)

        for row in rows[0:5]:
            for col in row:
                print('%10s'%col, end=' ')
            print()



def create_csv():
    pass




if __name__ == '__main__':
    read_csv()