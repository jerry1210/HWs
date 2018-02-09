'''
Write a Python program to subtract five days from current date.
Sample Date :
Current Date : 2015-06-22
5 days before Current Date : 2015-06-17
'''


from datetime import date, timedelta

def f(days_count):
    return date.today() - timedelta(days_count)
    # current_date = date.today()
    # if current_date.day > days:
    #     return current_date.strftime('%Y-%m-' + str(current_date.day - days))

print(f(13))