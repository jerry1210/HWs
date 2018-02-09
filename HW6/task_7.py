'''
•	Write the class AddressBook so the following code works:
c = AddressBook()

c.add(name='ynon', email='ynon@ynonperek.com', likes='red')
c.add(name='bob', email='bob@gmail.com', likes='blue')
c.add(name='ynon', email='ynon@gmail.com', likes='blue')

c.find_by(name='ynon')
# returns:
# [
#   {'name': 'ynon', 'email': 'ynon@ynonperek.com', 'likes': 'red'},
#   {'name': 'ynon', 'email': 'ynon@gmail.com', 'likes': 'blue}
# ]

c.find_by(likes='blue)
# returns:
# [
#   { 'name': 'bob', 'email': 'bob@gmail.com', 'likes': 'blue' },
#   {'name': 'ynon', 'email': 'ynon@gmail.com', 'likes': 'blue}
# ]
'''


class AddressBook:

    result = []

    def add(self, name, email, likes):
        self.result.append({'name': name, 'email': email, 'likes': likes})

    def find_by(self, name=None, email=None, likes=None):
        if name:
            return [item for item in self.result if item['name'] == name]
        elif email:
            return [item for item in self.result if item['email'] == email]
        elif likes:
            return [item for item in self.result if item['likes'] == likes]


c = AddressBook()

c.add(name='ynon', email='ynon@ynonperek.com', likes='red')
c.add(name='bob', email='bob@gmail.com', likes='blue')
c.add(name='ynon', email='ynon@gmail.com', likes='blue')

print(c.result)

print(c.find_by(name='ynon'))
# returns:
# [
#   {'name': 'ynon', 'email': 'ynon@ynonperek.com', 'likes': 'red'},
#   {'name': 'ynon', 'email': 'ynon@gmail.com', 'likes': 'blue}
# ]

print(c.find_by(likes='blue', name='ynon'))