'''
Write a Python program to find all the values in a list are greater than a specified number
'''


def f(list_, number):
    return [item for item in list_ if item > number]

print(f([1,2,3,4,5,6,7], 5))