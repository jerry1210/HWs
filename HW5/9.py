'''
•	Write a multiplication function (using addition (recursion))
 def my_mul(a, b) -> return a times b
'''


def my_mul(a, b):
    '''
    >>> my_mul(5,4)
    20

    :param a:
    :param b:
    :return:
    '''
    if b == 0:
        return 0
    elif b == 1:
        return a
    return a + my_mul(a, b-1)
