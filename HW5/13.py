'''
•	remember decorator @after5 ?
•	please make a similar one, but that acceps times to skip as param (@after(<times_to_skip>))
'''

def after_n(n):
    def decorator(func):
        func.calls_count = 0
        def wrapper():
            func.calls_count += 1
            if func.calls_count > n:
                func()
        return wrapper
    return decorator

@after_n(3)
def doit():
    print('Yo!')


doit()
doit()
doit()
doit()
doit()
doit()