'''
Write a Python program to convert a string to datetime.
Sample String : Jan 1 2014 2:43PM
Expected Output : 2014-07-01 14:43:00
'''


from time import strptime
string = 'Jan 1 2014 2:43PM'
s = strptime(string, '%b %d %Y %I:%M%p')
print(f'{s.tm_year}-{s.tm_mon}-{s.tm_mday} {s.tm_hour}:{s.tm_min}:{s.tm_sec}')