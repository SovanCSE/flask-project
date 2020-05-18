from jsonschema import validate, exceptions

instance1 = [1,2,3,"sovan"]
instance2 = [1,2,4,"sovan"]
instance3 = [1,2,3, None]
schema = {
    "type":"array",
    "items": [
        {'type':'number'},
        {'type':'number'},
        {'type':'number'},
        {'type':'string',
         'enum':['sovan']},
    ]
}

try:
    validate(instance=instance1, schema=schema)
    validate(instance=instance2, schema=schema)
    validate(instance=instance3, schema=schema)

except exceptions.ValidationError as e:
    print("Error:{}".format(e))