

import requests, shutil, os, glob
from zipfile import ZipFile
import pandas as pd
from xlrd import open_workbook
import csv

# zipfilename = 'desiya_hotels'
# try:
#     # downloading zip file
#     r = requests.get('http://staticstore.travelguru.com/testdump/1300001176/Excel.zip', auth=('testdump', 'testdump'), verify=False,stream=True)   #Note web_link is https://
#     r.raw.decode_content = True
#     with open(os.path.join(os.path.dirname(__file__), 'storage/{}.zip'.format(zipfilename)), 'wb') as f:
#         shutil.copyfileobj(r.raw, f)
#
#     #extracting zip file as xls file
#     with ZipFile(glob.glob(os.path.join(os.path.dirname(__file__), 'storage/desiya*.zip'))[0], 'r') as zip:
#         zip.extractall(os.path.join(os.path.dirname(__file__), 'storage/'))
#     #Rename xls file name as "desiya_hotels"
#     if glob.glob(os.path.join(os.path.dirname(__file__), 'storage/*[0-9].xls')):
#         for filename in glob.glob(os.path.join(os.path.dirname(__file__), 'storage/*[a-zA-z].xls')):
#             os.remove(filename)
#         os.rename(glob.glob(os.path.join(os.path.dirname(__file__), 'storage/*[0-9].xls'))[0], os.path.join(os.path.dirname(__file__),'storage/{}.xls'.format(zipfilename)))
#     else:
#         print('unzipped xls file is not found in storare folder')
# except Exception as e:
#     print("Error while downloading zip file")

#read xls file
# xls = pd.ExcelFile(glob.glob(os.path.join(os.path.dirname(__file__), 'storage/desiya*.xls'))[0])
# df = pd.read_excel(xls, sheet_name=0, index_col=None)
# print(df['Name'])
# print(df.head(5))
# for index, row in df.iterrows():
#     print(index, row[3])

#convert xls to csvc
# df.to_csv(os.path.join(os.path.dirname(__file__),'storage/{}'.format('robot.csv')), encoding='utf-8', index=False)


#convert xls file to csv using xlrd module
xlsfile = glob.glob(os.path.join(os.path.dirname(__file__), 'storage/robot*.xls'))[0]
wb = open_workbook(xlsfile)
sheet = wb.sheet_by_name('robot_list')
with open(os.path.join(os.path.dirname(__file__), 'storage/robot_list.csv'), "w") as file:
    writer = csv.writer(file, delimiter=",")
    headers = [cell.value for cell in sheet.row(0)]
    writer.writerow(headers)
    for i in range(1, sheet.nrows):
        rowvalue_list = [str(cell.value).strip() if cell.value else None for cell in sheet.row(i)]
        writer.writerow(rowvalue_list)






