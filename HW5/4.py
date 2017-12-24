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
    def decoraror(func):
        def wrapper(*args):
            assert isinstance(func(*args), exected_type), '{} expected'.format(exected_type)
            print(func(*args))
        return wrapper
    return decoraror

@returns(str)
def same(word):
    return word


same('word')