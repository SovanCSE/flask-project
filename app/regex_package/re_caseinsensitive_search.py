import re

test = 'UPPER TEXT, lower text, Mixed Text'
print(re.findall('text', test, flags=re.IGNORECASE))
#output:['TEXT', 'text', 'Text']