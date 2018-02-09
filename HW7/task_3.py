'''
Write a decorator named logger. It should log function calls and execution time
(for example: function f was called w/ params <a, b> and  took <time> to execute).
Decorator may accept argument file - file to write logs to. If no param was provided - simply print logs to console.
    Decorator should be implemented as class.
'''


import time

#TODO Decorator should be implemented as class.


class logger:

    def __init__(self, file=None):
        self.file = file

    def __call__(self, func):
        def wrapper(*args):
            start = time.time()
            func(*args)
            time_ = time.time() - start
            result = 'function {} was called w/ params {} and took {} to execute\n'.\
                format(func.__name__, ", ".join([str(arg) for arg in args]), time_)
            if self.file:
                with open(self.file, 'a') as f:
                    f.write(result)
            else:
                print(result)
        return wrapper


@logger('task_3.txt')
def f(a, b):
    return a + b

@logger('task_3.txt')
def f2(a, b):
    return a - b

@logger()
def f3(a, b):
    return a * b

f(4, 5)
f2(4, 5)
f3(4, 5)

# def logger(file=None):
#     def decorator(func):
#         def wrapper(*args):
#             start = time.time()
#             func(*args)
#             time_ = time.time() - start
#             result = 'function {} was called w/ params {} and took {} to execute'.\
#                 format(func.__name__, ", ".join([str(arg) for arg in args]), time_)
#             if file:
#                 with open(file, 'w') as f:
#                     f.write(result)
#             else:
#                 print(result)
#         return wrapper
#     return decorator


