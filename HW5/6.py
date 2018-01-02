'''
•	Write a function that flattens a dict
    """
    Flattens a nested dictionary by joining the keys with "." character.

         flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
         {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

    """
'''


def flatten_dict(input_dict):
    result = dict()
    for key, value in input_dict.items():
        if isinstance(value, dict):
            result.update({'.'.join([str(key), k]):v for k,v in value.items()})
        else:
            result.update({key: value})
    return result


print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))