'''
Write a decorator called returns that checks that a function returns expected argument type. Usage example:
@returns(str)
def same(word)
  return word

# works:
same('hello')

# raise AssertionError:
same(10)
'''


def returns(exected_type):
    def decorator(func):
        def wrapper(*args):
            if not isinstance(func(*args), exected_type):
                raise AssertionError('{} expected'.format(exected_type.__name__))
            # assert isinstance(func(*args), exected_type), '{} expected'.format(exected_type)
            print(func(*args))
        return wrapper
    return decorator

@returns(str)
def same(word):
    return word


same(0)