# Find factorials of a list of numbers

def factorialize(numbers):
    """ Return factorials of a list of numbers.
    
     factorialize([1, 2, 3, 4, 5])
     [1, 2, 6, 24, 120]
    """

    def factorial(number):
        return 1 if number == 1 else number * factorial(number - 1)

    return list(map(factorial, numbers))


print(factorialize([1, 2, 3, 4, 5]))
