'''
•	Write a python program that takes a list of file extensions and prints all the files from the current
directory matching the extension given. The following extensions and meaning should be supported:
•	c should find and print all .c and .h file names
•	py should find and print all .py and .pyc file names
•	pl should find and print all .pl and .pm file names
Bonus: Read extension and meaning from a configuration file.
'''


import os

def func(*extensions):
    if 'c' in extensions:
        extensions += 'h',
    if 'py' in extensions:
        extensions += 'pyc',
    if 'pl' in extensions:
        extensions += 'pm',

    return '\n'.join([item for item in os.listdir(os.curdir) for extension in extensions if item.endswith(extension)])


print(func('c', 'py', 'txt'))