li = {"id": "qwerty",
      "nestednestedlist": [
          {"id": "xyz", "keyA": "blah blah blah"},
          {"id": "fghi", "keyZ": "blah blah blah"}],
      "anothernestednestedlist": [
          {"id": "asdf", "keyQ": "blah blah"},
          {"id": "yuiop", "keyW": "blah"}]
      }


def recursive_dict(v):
    if isinstance(v, dict):
        return v
    for val in v:
        return recursive_dict(val)
    return None


def recursive_key(key, dict_value):
    if key in dict_value:
        print(key)
        return True
    for dict_val in dict_value.values():
        if isinstance(dict_val, dict):
            return recursive_key(key, dict_val)
        elif isinstance(dict_val, list):
            dict_val = recursive_dict(dict_val)
            print("what", dict_val)
            if isinstance(dict_val, dict):
                return recursive_key(key, dict_val)
    return None

print("Is found?", recursive_key("keyA", li))


