from jsonschema import validate, exceptions

##Example1::====>
# instance1 ={"a":1,"b":2}
# instance2 = {
#     0.01: "cm",
#     1: "m",
#     1000: "km"
# }
# instance3 ="Hi, I am Sovan"
# schema = {"type": "object"}
#
# try:
#     validate(instance=instance1, schema=schema)
#     validate(instance=instance2, schema=schema)
#     validate(instance=instance3, schema=schema)
# except exceptions.ValidationError as e:
#     print("Error:{}".format(e))
#     raise ValueError()

