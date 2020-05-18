from jsonschema import validate, exceptions

schema = {
     "type" : "object",
     "properties" : {
         "price" : {"type" : "number"},
         "name" : {"type" : "string"},
     },
}

instance= {"price":"120.12", "name":"sovan"}
try:
    validate(instance=instance, schema=schema)
except exceptions.ValidationError as e:
    print("Error: {}".format(e))