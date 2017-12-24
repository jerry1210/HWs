'''
Write a function that flattens nested list
    """Flattens a nested list.

             flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
              [1, 2, 3, 4, 5, 6, 7]
        """
'''


result = []

def flatten_list(input_list):
    for item in input_list:
        if isinstance(item, list):
            flatten_list(item)
        else:
            result.append(item)
    return result


print(flatten_list([ [1, 2, [3, 4] ], [5, 6], 7]))