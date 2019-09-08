import os
import pandas as pd
import numpy as np
import glob, sys
from itertools import islice



def read_csvfile(filename):
    dataframe = pd.read_csv(filename)
    print(dataframe['Name'])

def read_xlsfile(filename):
    # number_of_lines = 5
    # with open(filename, 'r+', encoding = "latin-1") as input_file:
    #     lines_cache = islice(input_file, number_of_lines)
    #     for current_line in lines_cache:
    #         print(current_line)
    chunk_size = 100
    xls = pd.ExcelFile(filename)
    df = pd.read_excel(xls, sheet_name='robot_list', index_col=None, header=None, skiprows=1)
    #split indexes
    idxes = np.array_split(df.index.values, chunk_size)
    print(sys.getsizeof(idxes))
    exit()

    chunks = [df.ix[idx] for idx in idxes]
    for chunk in chunks:
        for index, row in chunk.iterrows():
            print(index, row[0])

    # for sheetname in xls.sheet_names:
    #     print(sheetname)
    #     reader = xls.parse(sheetname, chunksize=1000)
    #     for chunk in reader:
    #         print(chunk)

        #df = pd.read_excel(xls, sheet_name=0, index_col=None)

if __name__ == '__main__':
    filename = os.path.join('.', 'storage/robot_list.xls')
    # read_csvfile(filename)
    read_xlsfile(filename)
