'''
Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in
a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''


def f(string):
    """
    >>> f('green-red-yellow-black-white')
    'black-green-red-white-yellow'

    :param string:
    :return:
    """
    return '-'.join(sorted(string.split('-')))
