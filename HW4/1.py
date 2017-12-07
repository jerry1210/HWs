'''
Write a function groupby that takes a key-function and a list.
The function should call key-function on all items in the
list and return a dictionary whose keys are the results of key-function and
values are all values from the list that product that key.

Example Usage:

groupby(lambda(s): s[0], 'hello', 'hi', 'help', 'bye', 'here')

returns: { h: ['hello', 'hi', 'help', 'here'], b: ['bye'] }
'''


def group_by(f, *args):
    dict_ = {}
    for k,v in [(f(item), item) for item in args]:
        dict_.setdefault(k, []).append(v)
    return dict_

print(group_by(lambda s: s[0], 'hello', 'hi', 'help', 'bye', 'here'))