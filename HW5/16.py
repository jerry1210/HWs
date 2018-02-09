'''
Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''


def f(list_):
    for item in list_:
        if list_.count(item) > 1:
            list_.remove(item)
    return list_

print(f([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))

