from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

## all sections as list
section_list = parser.sections()
print("section_list::",section_list)

## items in a perticular section
item_list = parser.items('settings')
print("item_list::",item_list)

## get perticular item value from a section
debug_value = parser['settings']['debug']
print("debug_value::",debug_value)

## get dev settings info
dev_settings = parser['main settings']['setting.dev']
print("dev_settings::",dev_settings)

## read as integer
secret_key = parser.getint('settings','secret_key')
print("secret_key::",secret_key)
print("secret_key type::",type(secret_key))

## read as boolean
bol_value = parser.getboolean('settings', 'debug')
print("bol_value::",bol_value)
print("bol_value type::",type(bol_value))

