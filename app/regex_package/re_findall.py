full_str = """
path: www.google.com
path: www.crome.com
path: www.finesrc.com
path: www.abc.com
"""
full_str_v2 ="""
 my name is Sovan and age is 32
 my name is Kushal and age is 23
"""
import re
find_result = re.findall('path:\s([\w.]*)', full_str)
print(find_result)

names = re.findall('[A-Z][a-z]*', full_str_v2)
ages = re.findall('\d{1,3}', full_str_v2)
print(dict([(name, age) for name, age in zip(names, ages)]))


