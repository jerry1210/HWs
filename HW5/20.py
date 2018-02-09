'''
Write a Python script to display the
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
'''


import datetime

current_date_and_time = datetime.datetime.now()

print(current_date_and_time.strftime("Current date and time: %d-%m-%y %H:%M:%S"))
print(current_date_and_time.strftime("Current year: %Y"))
print(current_date_and_time.strftime("Month of year: %m (%B)"))
print(current_date_and_time.strftime("Week number of the year: %W"))
print(current_date_and_time.strftime("Weekday of the week: %A"))
print(current_date_and_time.strftime("Day of year: %j"))
print(current_date_and_time.strftime("Day of the month: %d"))
print(current_date_and_time.strftime("Day of week: %w"))