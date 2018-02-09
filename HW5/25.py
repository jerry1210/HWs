'''
Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog" 
'''


def f(string):
    '''
    >>> f("The quick brown fox jumps over the lazy dog")
    True

    >>> f('bla bla bla')
    False

    :param string:
    :return:
    '''
    return not bool([chr(i) for i in range(97, 123) if chr(i) not in string])

