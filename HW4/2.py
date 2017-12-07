'''
Implement own map function (the one from python stdlib - apply function to each item from iterable)
'''


def map_function(f, list_):
    return [f(item) for item in list_]

print(map_function(lambda x: x**2, range(5)))