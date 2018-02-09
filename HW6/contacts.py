'''
class TestContacts:
    def setup_function(self):
        self.home_book = Contacts()
        self.work_book = Contacts()

    def test_create_and_search(self):
        self.home_book.add('Tom', { 'lives_in': 'USA', 'email': 'tomthecat@gmail.com' })
        self.home_book.add('Bob', { 'lives_in': 'USA', 'email': 'bob@gmail.com' })
        self.work_book.add('Mike', { 'lives_in': 'Marks', 'email': 'mike@gmail.com' })

        results = self.home_book.contacts_by_lives_in('USA')
        assert 'Tom' in results
        assert 'Bob' in results
        assert len(results) == 2
'''


class Contacts:
    def __init__(self):
        self.contacts = dict()

    def add(self, name, data):
        self.contacts.update({name: data})

    def contacts_by_lives_in(self, place):
        return [name for name in self.contacts.keys() if self.contacts[name]['lives_in'] == place]
