'''
Write a decorator called accepts that checks if a function was called with correct argument types. Usage example:
# make sure function can only be called with a float and an int
@accepts(float, int)
def pow(base, exp):
  pass

# raise AssertionError
pow('x', 10)
'''


def accepts(*types):
    def decorator(func):
        def wrapper(*args):
            assert {isinstance(item[0], item[1]) for item in zip(args, types)} == {True}, \
                'Arguments with wrong types passed'
            return func(*args)
        return wrapper
    return decorator

@accepts(float, int)
def pow(base, exp):
    print(base**exp)


pow(7.0, 2)