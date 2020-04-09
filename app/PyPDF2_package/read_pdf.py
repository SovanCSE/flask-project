import PyPDF2
pdfFileObj = open('jee.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pdfReader.decrypt('rosebud')

pageObj = pdfReader.getPage(0)
print(pageObj.getContents())
print(pageObj.extractText().encode('utf-8').decode('latin'))

import requests

requests.delete()