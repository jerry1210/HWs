# Use bubble sort to solve this problem.
# Wiki on the algorithm at https://en.wikipedia.org/wiki/Bubble_sort


def bubble_sort(numbers):
    """ Use bubble sort to sort a list of numbers in ascending order.
        Return the input list after mutating it with sorted numbers.
    
     bubble_sort([2, 19, 4, 1, -40])
     [-40, 1, 2, 4, 19]
    """

    # your code here
    for j in range(len(numbers)-1):
        for i in range(len(numbers)-j-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers


print(bubble_sort([2, 19, 4, 1, -40]))
