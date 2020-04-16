import pandas as pd
import os


"""
Stacking: For analytics propose, get perticular header level columns & transpose into as row 
level is called as stack.

Unstacking: Transposed stacked dataframe get back into it's original format we use unstack 
operation.
"""

if __name__ == "__main__":
    read_path = os.path.join(os.path.dirname(__file__),'../storage/company_stocks.xlsx')
    df = pd.read_excel(read_path, header=[0,1], index_col=[0])
    df1 = df.stack()
    print(df1)
    df2 = df1.unstack()
    print(df2)
    pd.DataFrame()



