'''
•	Modify the class so the following will also work (Hint: read about __getitem__):

with AddressBook('contacts.txt') as ab:
       print(ab['Eve'])
'''


import re


class AddressBook:

    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __getitem__(self, item):
        with open(self.file, 'r') as f:
            return re.search(item + ': (.*)', f.read()).group(1)


# with AddressBook('contacts.txt') as ab:
#     print(ab['Eve'])
