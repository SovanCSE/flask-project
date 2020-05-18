from jsonschema import validate, exceptions

instance1 = True
instance2 = 'kk'
schema = {"type":"boolean"}

try:
    validate(instance=instance1,schema=schema)
    validate(instance=instance2,schema=schema)
except exceptions.ValidationError as e:
    print("Error:{}".format(e))