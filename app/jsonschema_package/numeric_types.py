from jsonschema import validate, exceptions

#Example1:===>
# instance1 = 12
# instance2 = -12
# instance3 = '12'
# schema = {'type':'number'}
# try:
#     validate(instance=instance1, schema=schema)
#     validate(instance=instance2, schema=schema)
#     validate(instance=instance3, schema=schema)
# except exceptions.ValidationError as e:
#     print("Error:{}".format(e))
#     raise ValueError()

#Example2:===>
# instance1 = 0
# instance2 = 100
# instance3 = 120
# schema = {
#      "type":'number',
#      "minimum": 0,
#      "maximum":100,
#      "multipleOf":5
#  }
# try:
#     validate(instance=instance1, schema=schema)
#     validate(instance=instance2, schema=schema)
#     validate(instance=instance3, schema=schema)
# except exceptions.ValidationError as e:
#     print("Error:{}".format(e))
    # raise ValueError()

#Exmaple3: ==>
instance1 = 0
instance2 = 100
instance3 = 120
schema = {
     "type":'number',
     "minimum": 0,
     "maximum":100,
     "exclusiveMinimum":0,
     "exclusiveMaximum":100
 }
try:
    validate(instance=instance1, schema=schema)
    validate(instance=instance2, schema=schema)
    validate(instance=instance3, schema=schema)
except exceptions.ValidationError as e:
    print("Error:{}".format(e))

