# Define a function that takes a list of lists and returns a new list of
# lists with a student's name and their average grade in each sublist.

def average_grade(lst):    
    """ Return students' names and their average grades.
    
     average_grade([['Bob', 56, 80, 72, 90], ['Alice', 60, 88, 44, 70]])
     [['Bob', 74.5], ['Alice', 65.5]]
    """

    # your code here
    return [[lst[i][0], sum(lst[i][1:])/len(lst[i][1:])] for i in range(len(lst))]

print(average_grade([['Bob', 56, 80, 72, 80], ['Alice', 60, 88, 44, 70]]))