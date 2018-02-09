'''
Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
'''


def f(lists):
    '''
    >>> f([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])
    [10, 11, 12]

    :param list_:
    :return:
    '''

    result = lists[0]
    for i in range(1,len(lists)):
        if sum(lists[i]) > sum(result):
            result = lists[i]
    return result
