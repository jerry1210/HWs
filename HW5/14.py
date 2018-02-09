'''
Write a Python program to check if all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
'''


def f(list_):
    '''
    >>> f([{},{},{}])
    True

    >>> f([{1:2},{},{}])
    False

    :param list_:
    :return:
    '''

    return not bool([item for item in list_ if isinstance(item, dict) and item])
