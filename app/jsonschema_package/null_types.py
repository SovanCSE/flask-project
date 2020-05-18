from jsonschema import validate, exceptions

instance1 = None
instance2 = 'Sovan'
schema = {"type":"null"}
try:
    validate(instance=instance1,schema=schema)
    validate(instance=instance2,schema=schema)
except exceptions.ValidationError as e:
    print("Error:{}".format(e))