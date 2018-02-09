'''
Write a class named AddressBook that saves names and email addresses in a file.
The following code should work (and create the file if not already exists):

with AddressBook('contacts.txt') as ab:
    ab.add('Eve', 'eve@gmail.com')
    ab.add('Alice', 'alice@walla.co.il')

with AddressBook('contacts.txt') as ab:
   print(ab.email('Eve'))

•	Modify the class so the following will also work (Hint: read about __getitem__):

with AddressBook('contacts.txt') as ab:
       print(ab['Eve'])
'''
from collections import namedtuple
from typing import NamedTuple


class AddressBook:

    def __init__(self, file):
        self.file = file

    def __enter__(self):
        with open(self.file, 'r') as f:
            self.contacts = {item.split(':')[0].strip(): item.split(':')[1].strip() for item in f.readlines()}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: prepare info about params
        with open(self.file, 'w') as f:
            for key,value in self.contacts.items():
                f.writelines('{} : {}\n'.format(key, value))

    def add(self, name, mail):
        self.contacts.update({name: mail})

    def email(self, name):
        return self.contacts[name]

    def __getitem__(self, name):
        return self.email(name)


with AddressBook('contacts.txt') as ab:
    ab.add('Eve', 'eve@gmail.com')
    ab.add('Alice', 'alice@walla.co.il')

with AddressBook('contacts.txt') as ab:
   print(ab.email('Eve'))

with AddressBook('contacts.txt') as ab:
    print(ab['Eve'])



NT = namedtuple('NT', 'n t')

class NT1(NamedTuple):
    n: str = '42'