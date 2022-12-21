import unittest
from user import Users


class TestUsers(unittest.TestCase):
    def test_init(self):
        # Test the initialization of the Users class
        user = Users('test_user', hashed_password=b'hashed_password', my_salt=b'salt', cooker=True)
        self.assertEqual(user._username, 'test_user')
        self.assertEqual(user._hashed_password, b'hashed_password')
        self.assertEqual(user._my_salt, b'salt')
        self.assertTrue(user._cooker)

    def test_str(self):
        # Test the string representation of the Users class
        user = Users('test_user', hashed_password=b'hashed_password', my_salt=b'salt', cooker=True)
        self.assertEqual(str(user), 'test_user,b\'hashed_password\',b\'salt\',True')

    def test_username(self):
        # Test the username property
        user = Users('test_user', hashed_password=b'hashed_password', my_salt=b'salt', cooker=True)
        self.assertEqual(user.username, 'test_user')

    def test_cooker(self):
        # Test the cooker property
        user = Users('test_user', hashed_password=b'hashed_password', my_salt=b'salt', cooker=True)
        self.assertTrue(user.cooker)
        user = Users('test_user', hashed_password=b'hashed_password', my_salt=b'salt', cooker=False)
        self.assertFalse(user.cooker)

    def test_change_cooker(self):
        # Test the change_cooker property
        user = Users('test_user', hashed_password=b'hashed_password', my_salt=b'salt', cooker=True)
        self.assertTrue(user.cooker)
        user.change_cooker
        self.assertFalse(user.cooker)

    def setUp(self):
        # Create a user object to be used in the test functions
        self.user = Users('test_user')
        self.user.change_password('password')

    def test_is_correct_password(self):
        # Test the is_correct_password function
        self.assertTrue(self.user.is_correct_password('password'))
        self.assertFalse(self.user.is_correct_password('wrong_password'))

    def test_change_password(self):
        # Test the change_password function
        self.user.change_password('new_password', 'password')
        self.assertTrue(self.user.is_correct_password('new_password'))
        self.assertFalse(self.user.is_correct_password('password'))

    def test_change_bad_password(self):
        # Test the change_password function
        self.user.change_password('new_password', 'wrong_password')

if __name__ == '__main__':
    unittest.main()
