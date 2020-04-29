find_str = """
My      name  is sovan 
I am a python developer"""

import re
#remove extra space using regex sub function
replace_result = re.sub('\n', '',find_str)
replace_result = re.sub('  +', ' ',replace_result)
print(replace_result)