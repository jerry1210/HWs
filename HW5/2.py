'''
Calculation in the following fib function may take a long time. Implement a Decorator that remembers old calculations
so the function won't calculate a fib value more than once. Program Code:
@memoize
def fib(n):
    print("fib({})".format(n))
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

     Expected Output:
fib(10)
fib(9)
fib(8)
fib(7)
fib(6)
fib(5)
fib(4)
fib(3)
fib(2)
fib(1)
55
'''


def memoize(func):
    results = dict()
    def wrapper(number):
        if number in results:
            return results[number]
        results[number] = func(number)
        return func(number)
    return wrapper

@memoize
def fib(n):
    print("fib({})".format(n))
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(4))
print(fib(5))
print(fib(10))