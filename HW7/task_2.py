'''
Write a program that takes a file name from command line and prints the number of lines in that file.
If the provided argument does not refer to a file an error should be printed. Exceptions handling required
Example Usage:
python countlines.py /etc/shells
11

python countlines.py /foo/bar
Sorry, file /foo/bar not found
'''


import sys
import os

# def f():
#     path = sys.argv[1]
#     if not os.path.isfile(path):
#         raise FileNotFoundError('Sorry, file {} not found'.format(path))
#     return len(open(path, 'r').readlines())

def f(path):
    return len(open(path, 'r').readlines())

if __name__ == '__main__':
    try:
        print(f(sys.argv[1]))
    except FileNotFoundError as e:
        print('file not found')
