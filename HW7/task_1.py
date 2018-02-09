'''
Write a python script for mass renaming music files according to labels. The script takes an existing format of files
in current directory and an expected output format and prints a list of old -> new file name tuples.
      Format can be any string that contains any number of the labels: <artist>, <album>, <track>, <year>

Assume file names match input format.

Sample list of input files:

Bob Dylan - 01 You're No Good (1962).mp3
Bob Dylan - 02 Talkin' New York (1962).mp3
Bob Dylan - 03 In My Time of Dyin' (1962).mp3
Bob Dylan - 04 Man of Constant Sorrow (1962).mp3
Bob Dylan - 05 Fixin' to Die (1962).mp3
Bob Dylan - 06 Pretty Peggy-O (1962).mp3
Sample input format:

<album> - <track> <title> (<year>).mp3

Sample output format:
Bob Dylan/<year> <album>/<track> <title>.mp3

Expected output:

Bob Dylan - 01 You're No Good (1962).mp3 -> Bob Dylan/1962 Bob Dylan/01 You're No Good.mp3
Bob Dylan - 02 Talkin' New York (1962).mp3 -> Bob Dylan/1962 Bob Dylan/02 Talkin' New York.mp3
Bob Dylan - 03 In My Time of Dyin' (1962).mp3 -> Bob Dylan/1962 Bob Dylan/03 In My Time of Dyin'.mp3
Bob Dylan - 04 Man of Constant Sorrow (1962).mp3 -> Bob Dylan/1962 Bob Dylan/04 Man of Constant Sorrow.mp3
Bob Dylan - 05 Fixin' to Die (1962).mp3 -> Bob Dylan/1962 Bob Dylan/05 Fixin' to Die.mp3
Bob Dylan - 06 Pretty Peggy-O (1962).mp3 -> Bob Dylan/1962 Bob Dylan/06 Pretty Peggy-O.mp3

Bonus: also rename the files and create required directories along the way
'''

import os

os.rename("Bob Dylan - 01 You're No Good (1962).mp3", 'Bob Dylan - 06 Pretty Peggy-O (1962).mp3')
