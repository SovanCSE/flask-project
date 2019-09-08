import requests, shutil, os, glob
from zipfile import ZipFile
import pandas as pd
from xlrd import open_workbook
import csv
import os


try:
    desiya_filename = 'desiya_hotels'
    # # Create storage folder while not esixted
    # if not os.path.exists(os.path.join(os.path.dirname(__file__), 'storage')):
    #     os.makedirs(os.path.join(os.path.dirname(__file__), 'storage'))
    # # Create inventory_storage folder while not esixted
    # if not os.path.exists(os.path.join(os.path.dirname(__file__), 'inventory_storage')):
    #     os.makedirs(os.path.join(os.path.dirname(__file__), 'inventory_storage'))
    # #Download Text zip file
    # r = requests.get('http://staticstore.travelguru.com/testdump/1300001176/Text.zip', auth=('testdump', 'testdump'), verify=False, stream=True)
    # r.raw.decode_content = True
    # with open(os.path.join(os.path.dirname(__file__), 'storage/{}.zip'.format(desiya_filename)), 'wb') as f:
    #     shutil.copyfileobj(r.raw, f)
    #
    # #Unzip Text zip file  and store HotelOverview txt file into same zip directory
    # with ZipFile(glob.glob(os.path.join(os.path.dirname(__file__), 'storage/{}.zip'.format(desiya_filename)))[0]) as zipObj:
    #     # Get a list of all archived file names from the zip
    #     listOfFileNames = zipObj.namelist()
    #     #Iterate over the file names
    #     for fileName in listOfFileNames:
    #         # Check filename endswith csv
    #         if 'HotelOverview' in fileName:
    #             # Extract a single file from zip
    #             zipObj.extract(fileName, path=glob.glob(os.path.join(os.path.dirname(__file__), 'storage'))[0])

   # #Convert from HotelOverview.txt file to desiya_hotels csv file.
   #  for filename in glob.glob(os.path.join(os.path.dirname(__file__),'storage/{}.txt'.format("HotelOverview"))):
   #      if 'HotelOverview' in filename:
   #          df = pd.read_fwf(filename)
   #          df.to_csv(os.path.join(os.path.dirname(__file__), 'inventory_storage/{}.csv'.format(desiya_filename)))
   #          #Delete storage folder if not existed
   #          if os.path.exists(os.path.join(os.path.dirname(__file__), 'storage')):
   #              shutil.rmtree(os.path.join(os.path.dirname(__file__), 'storage'))


    with open(glob.glob(os.path.join(os.path.dirname(__file__),'storage/{}.txt'.format("HotelOverview")))[0], "r") as text_file:
        in_reader = csv.reader(text_file, quotechar='"', delimiter='|', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        rowsaslist = list(in_reader)
        with open(os.path.join(os.path.dirname(__file__), 'inventory_storage/{}.csv'.format(desiya_filename)), "w") as out_csv:
            out_writer = csv.writer(out_csv, delimiter=",", quoting=csv.QUOTE_ALL)
            for row in rowsaslist:
                out_writer.writerow(row)

except Exception as e:
    print("ERROR: "+str(e))
