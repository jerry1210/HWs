from task_7 import AddressBook

class TestAddressBook:
    def setup_method(self):
        self.address_book = AddressBook()

    def test_add(self):
        self.address_book.add(name='ynon', email='ynon@ynonperek.com', likes='red')
        assert self.address_book.result[0] == {'name': 'ynon', 'email': 'ynon@ynonperek.com', 'likes': 'red'}

    def teardown_method(self):
        self.address_book.result.clear()
