from task_6 import AddressBook


class TestAddressBook:

    def setup_method(self):
        self.path = '.\HW6\contacts.txt'

    def test_getitem(self):
        with open(self.path, 'w') as ab:
            ab.write('Eve: eve@gmail.com\n')
        with AddressBook(self.path) as ab:
            result = ab['Eve']
        assert result == 'eve@gmail.com'

    def teardown_method(self):
        open(self.path, 'w').close()