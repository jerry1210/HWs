'''
•	Write a Python program to sort a list alphabetically in a dictionary.
     input: {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
output: {'n1': [1, 2, 3], 'n3': [2, 3, 4], 'n2': [1, 2, 5]}
'''


input_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
print({key: sorted(value) for key,value in input_dict.items()})