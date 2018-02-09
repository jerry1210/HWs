'''
Write a Python program to get the depth of a dictionary
'''


def depth(dict_, d=1):
    '''
    >>> depth({1:{1:{3:{3:{2:0}}}}})
    4
    >>> depth({})
    1

    :param dict_:
    :param d:
    :return:
    '''

    for item in dict_.values():
        if isinstance(item, dict):
            d += 1
            depth(item, d)
    return d

if __name__ == '__main__':
    depth({1:{1:{3:{3:2}}}})
