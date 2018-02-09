'''
•	Write a function that unflattens flatten dict (reverse of prev function)
    """
    Unflattens flatten dictionary (reverse of flatten_dict).

     unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
    """

'''


result = dict()

def unflatten_dict(input_dict):
    for key, value in input_dict.items():
        if '.' in key:
            result.setdefault(key.split('.')[0], {}).update({key.split('.')[1]: value})
        else:
            result.update({key: value})
    return result


print(unflatten_dict({'a': 1, 'b.x': 2, 'b.y.z': 3, 'c': 4})) #{'a': 1, 'b': {'x': 2, 'y': {'z': 3}}, 'c': 4}
