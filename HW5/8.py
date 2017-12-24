'''
•	Wirte a custom power function (using recursion)
     def my_pow(number, x) -> return number ^ x
'''


def my_pow(number, x):
    if x == 0:
        return 1
    elif x == 1:
        return number
    return number * my_pow(number, x-1)


print(my_pow(3,3))