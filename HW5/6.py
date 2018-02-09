'''
•	Write a function that flattens a dict
    """
    Flattens a nested dictionary by joining the keys with "." character.

         flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
         {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

    """
'''


def flatten_dict(input_dict, result=None):
    """
    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': {'z': 3}}, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y.z': 3, 'c': 4}

    :param input_dict:
    :return:
    """
    if result is None:
        result = dict()

    for key, value in input_dict.items():
        if isinstance(value, dict):
            flatten_dict({'.'.join([str(key), k]): v for k, v in value.items()}, result=result)
        else:
            result.update({key: value})
    return result


if __name__ == '__main__':
    print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': {'z': 3}}, 'c': 4}))
