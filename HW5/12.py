'''
•	You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase
    letters and vice versa. For Example:
  Www.HackerRank.com → wWW.hACKERrANK.COM
      Pythonist 2 → pYTHONIST 2
'''


def swap_case(input_string):
    return ''.join([item.upper() if item.islower() else item.lower() for item in input_string])


string = 'Pythonist 2'
print(swap_case(string))