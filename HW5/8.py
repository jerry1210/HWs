'''
•	Wirte a custom power function (using recursion)
     def my_pow(number, x) -> return number ^ x
'''


def my_pow(number, x):
    '''
    >>> my_pow(3,3)
    27

    >>> my_pow(3,0)
    1

    >>> my_pow(2,-2)
    0.25

    :param number:
    :param x:
    :return:
    '''
    if x == 0:
        return 1
    elif x == 1:
        return number
    elif x < 1:
        return 1 / number * my_pow(number, x+1)
    else:
        return number * my_pow(number, x-1)

