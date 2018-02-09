'''
Write a function that flattens nested list
    """Flattens a nested list.

             flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
              [1, 2, 3, 4, 5, 6, 7]
        """
'''


def flatten_list(input_list, result=[]):
    '''
    >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
    [1, 2, 3, 4, 5, 6, 7]

    :param input_list:
    :param result:
    :return:
    '''
    for item in input_list:
        if isinstance(item, list):
            flatten_list(item)
        else:
            result.append(item)
    return result


if __name__ == '__main__':
    print(flatten_list([[1, 2, [3, 4]], [5, 6], 7]))