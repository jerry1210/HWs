'''

•	Provided the test file test_contacts.py. Write the module required to make the test pass:
import unittest
from lib.contacts import Contacts

class TestContacts(unittest.TestCase):
    def setUp(self):
        self.home_book = Contacts()
        self.work_book = Contacts()

    def test_create_and_search(self):
        self.home_book.add('Tom', { 'lives_in': 'USA', 'email': 'tomthecat@gmail.com' })
        self.home_book.add('Bob', { 'lives_in': 'USA', 'email': 'bob@gmail.com' })
        self.work_book.add('Mike', { 'lives_in': 'Marks', 'email': 'mike@gmail.com' })

        results = self.home_book.contacts_by_lives_in('USA')
        self.assertTrue('Tom' in results)
        self.assertTrue('Bob' in results)
        self.assertEqual(len(results), 2)
'''


from contacts import Contacts

class TestContacts:
    def setup_method(self):
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

