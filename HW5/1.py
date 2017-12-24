'''
Write a Decorator named after5 that will ignore the decorated function in the first 5 times it is called. Example Usage:
@after5
def doit(): print("Yo!")
# ignore the first 5 calls
doit()
doit()
doit()
doit()
doit()

# so only print yo once
doit()
'''


def after_5(func):
    func.calls_count = 0
    def wrapper():
        func.calls_count += 1
        if func.calls_count > 5:
            func()
    return wrapper

@after_5
def doit():
    print('Yo!')


doit()
doit()
doit()
doit()
doit()
doit()