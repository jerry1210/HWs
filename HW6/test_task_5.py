from task_5 import AddressBook


class TestAddressBook:

    def setup_method(self):
        self.path = '.\HW6\contacts.txt'

    def test_add(self):
        with AddressBook(self.path) as ab:
            ab.add('Eve', 'eve@gmail.com')
            ab.add('Alice', 'alice@walla.co.il')
        with open(self.path, 'r') as f:
            result = f.read()
        assert result == 'Eve: eve@gmail.com\nAlice: alice@walla.co.il\n'

    def test_email(self):
        with AddressBook(self.path) as ab:
            ab.add('Eve', 'eve@gmail.com')
            result = ab.email('Eve')
        assert result == 'eve@gmail.com'

    def teardown_method(self):
        with open(self.path, 'w') as f:
            f.truncate()