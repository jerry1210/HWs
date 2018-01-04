# Insert a string after a word in a specific line of a text file

"""

Input file
line 1: value1
line 2: value2
line 3: value3
line 4: value4
line 5: value5

Insert, for example, "NAME" in the line number 3 just after "line" so
the file would become:

Output file
line 1: value1
line 2: value2
line NAME 3: value3
line 4: value4
line 5: value5

"""


def insert_string(in_file, line, position, insertion):
    """ Return a list of lines after inserting a word in a specific line. """
    file = open(in_file, 'r')
    text = file.readlines()
    file.close()
    text[line-1] = text[line-1][:position] + insertion + ' ' + text[line-1][position:]
    return ''.join(text)


def write_to(outfile, from_infile):
    """ Write to a new file lines returned by the above function """
    # file = open(outfile, 'w')
    # file.write(from_infile)
    # file.close()


    with open(outfile, 'w') as file:
        file.write(from_infile)


write_to('output.txt', insert_string('input.txt', 3, 5, 'NAME'))
