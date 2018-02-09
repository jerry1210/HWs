'''
Write a Python program to determine whether a given year is a leap year.
'''


def f(year):
    return year % 4 == 0

print(f(2016))
print(f(2018))