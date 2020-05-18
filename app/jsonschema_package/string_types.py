from jsonschema import validate, exceptions

#Example 1:===>
instance1 = 'hello'
instance2 = ''
schema = {'type': 'string'}
try:
    validate(instance=instance1, schema=schema)
    validate(instance=instance2, schema=schema)
except exceptions.ValidationError as e:
    print("Error:{}".format(e))
    raise ValueError()


#Example 2:====>(minLength, maxLength constrain keyword in jsonschema)
# instance1 = 'AA'
# instance2 = 'BBBB'
# instance3 = "KKKKK"
# schema = {
#     'type':'string',
#     'minLength': 2,
#     'maxLength':4
# }
# try:
#     validate(instance=instance1, schema=schema)
#     validate(instance=instance2, schema=schema)
#     validate(instance=instance3, schema=schema)
# except exceptions.ValidationError as e:
#     print("Error:{}".format(e))
#     raise ValueError()


##Example 3: ==>(Pattern is json schema)
# instance1 = "5553-1212"
# instance2 = "(888)555-1212"
# instance3 = "(888)555-1212 ext. 532"
# schema = {
#         'type':'string',
#         'pattern':'^(\\(\d{3}\\))?\d{3}-\d{4}$'
# }
# try:
#     validate(instance=instance1, schema=schema)
#     validate(instance=instance2, schema=schema)
#     validate(instance=instance3, schema=schema)
# except exceptions.ValidationError as e:
#     print("Error:{}".format(e))
    # raise ValueError()


