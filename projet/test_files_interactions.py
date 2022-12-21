from user import Users
from meal import Meal
from bill import Bill
from file_interactions import read_file_user, add_user_database, delete_user_database, write_file_user, stitch_list, \
    read_file_meal, add_meal_database, write_file_meal, read_file_bill, add_bill_database, write_file_bill
import unittest


class TestReadFileUser(unittest.TestCase):
    def test_read_file_user(self):
        # Test that the function reads a file correctly and returns a list of User objects
        path = "unittest/test_readfile_user.csv"
        with open(path, "w") as f:
            f.write("user1,password1,salt1,True\n")
            f.write("user2,password2,salt2,False\n")
        users = read_file_user(path)
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, "user1")
        self.assertEqual(users[0]._hashed_password, "password1")
        self.assertEqual(users[0]._my_salt, "salt1")
        self.assertTrue(users[0].cooker)
        self.assertEqual(users[1].username, "user2")
        self.assertEqual(users[1]._hashed_password, "password2")
        self.assertEqual(users[1]._my_salt, "salt2")
        self.assertFalse(users[1].cooker)

    def test_read_file_user_filenotfound(self):
        # Test that the function prints an error message when the file is not found
        path = "nonexistent_file.txt"
        with self.assertRaises(FileNotFoundError):
            read_file_user(path)

    def test_add_user_database(self):
        # Test that a new user is added to the list
        users_list = [Users("user1", "password1", "salt1", True)]
        new_user = Users("user2", "password2", "salt2", False)
        add_user_database(new_user, users_list)
        self.assertEqual(len(users_list), 2)
        self.assertEqual(users_list[1].username, "user2")
        self.assertEqual(users_list[1]._hashed_password, "password2")
        self.assertEqual(users_list[1]._my_salt, "salt2")
        self.assertFalse(users_list[1].cooker)

    def test_add_existing_user_database(self):
        # Test that a user is not added to the list if the username already exists
        users_list = [Users("user1", "password1", "salt1", True)]
        new_user = Users("user1", "password2", "salt2", False)
        add_user_database(new_user, users_list)
        self.assertEqual(len(users_list), 1)
        self.assertEqual(users_list[0].username, "user1")
        self.assertEqual(users_list[0]._hashed_password, "password1")
        self.assertEqual(users_list[0]._my_salt, "salt1")
        self.assertTrue(users_list[0].cooker)

    def test_delete_user_database(self):
        # Test that a user is deleted from the list
        users_list = [Users("user1", "password1", "salt1", True), Users("user2", "password2", "salt2", False)]
        old_user = Users("user1", "password1", "salt1", True)
        delete_user_database(old_user, users_list)
        self.assertEqual(len(users_list), 1)
        self.assertEqual(users_list[0].username, "user2")
        self.assertEqual(users_list[0]._hashed_password, "password2")
        self.assertEqual(users_list[0]._my_salt, "salt2")
        self.assertFalse(users_list[0].cooker)

    def test_delete_nonexistent_user_database(self):
        # Test that a user is not deleted from the list if it doesn't exist
        users_list = [Users("user1", "password1", "salt1", True)]
        old_user = Users("user2", "password2", "salt2", False)
        delete_user_database(old_user, users_list)
        self.assertEqual(len(users_list), 1)
        self.assertEqual(users_list[0].username, "user1")
        self.assertEqual(users_list[0]._hashed_password, "password1")
        self.assertEqual(users_list[0]._my_salt, "salt1")
        self.assertTrue(users_list[0].cooker)

    def test_write_file_user(self):
        # Test that the function writes a list of users to a file correctly
        path = "unittest/test_writefile_user.csv"
        users_list = [Users("user1", "password1", "salt1", True), Users("user2", "password2", "salt2", False)]
        write_file_user(path, users_list)
        with open(path, "r") as f:
            self.assertEqual(f.read(), "user1,password1,salt1,True\nuser2,password2,salt2,False\n")

    def test_write_file_user_filenotfound(self):
        # Test that the function prints an error message when the file is not found
        path = "nonexistent_directory/test_writefile_user.csv"
        users_list = [Users("user1", "password1", "salt1", True)]
        with self.assertRaises(OSError):
            write_file_user(path, users_list)

    def test_stitch_list(self):
        # Test that the function stitches lists correctly
        lst = ["abc", "[def", "ghi]", "jkl", "[mno", "pqr]"]
        self.assertEqual(stitch_list(lst), ['abc', ['e', 'h'], 'jkl', ['n', 'q']])

    def test_stitch_empty_list(self):
        # Test that the function handles empty lists correctly
        lst = []
        self.assertEqual(stitch_list(lst), [])

    def test_stitch_single_element_list(self):
        # Test that the function handles lists with a single element correctly
        lst = ["abc"]
        self.assertEqual(stitch_list(lst), ["abc"])

    def test_read_file_meal(self):
        # Test that the function reads a file correctly and returns a list of Meal objects
        path = "unittest/test_readfile_meal.csv"
        with open(path, "w") as f:
            f.write("meal1,20-12-2021,user1,5,[]\n")
            f.write("meal2,21-12-2021,user2,10,[]\n")
        meals = read_file_meal(path)
        self.assertEqual(len(meals), 2)
        self.assertEqual(meals[0].description, "meal1")
        self.assertEqual(meals[0].date, "20-12-2021")
        self.assertEqual(meals[0].cooker, "user1")
        self.assertEqual(meals[0].price_by_user, "5")

    def test_add_meal_database(self):
        # Test that a new meal is added to the list
        meal_list = [Meal("meal1", "20-12-2021", "user1", 5, [])]
        new_meal = Meal("meal2", "21-12-2021", "user2", 10, [])
        add_meal_database(new_meal, meal_list)
        self.assertEqual(len(meal_list), 2)
        self.assertEqual(meal_list[1].description, "meal2")
        self.assertEqual(meal_list[1].date, "21-12-2021")
        self.assertEqual(meal_list[1].cooker, "user2")
        self.assertEqual(meal_list[1].price_by_user, 10)
        self.assertEqual(meal_list[1].participants, [])

    def test_add_existing_meal_database(self):
        # Test that a user is not added to the list if the username already exists
        meal_list = [Meal("meal1", "20-12-2021", "user1", 5, [])]
        new_meal = Meal("meal1", "20-12-2021", "user1", 5, [])
        add_meal_database(new_meal, meal_list)
        self.assertEqual(len(meal_list), 1)
        self.assertEqual(meal_list[0].description, "meal1")
        self.assertEqual(meal_list[0].date, "20-12-2021")
        self.assertEqual(meal_list[0].cooker, "user1")
        self.assertEqual(meal_list[0].price_by_user, 5)
        self.assertEqual(meal_list[0].participants, [])

    def test_write_file_meal(self):
        # Test that the function writes a list of users to a file correctly
        path = "unittest/test_writefile_meal.csv"
        meal_list = [Meal("meal1", "20-12-2021", "user1", 5, []), Meal("meal2", "21-12-2021", "user2", 10, [])]
        write_file_meal(path, meal_list)
        with open(path, "r") as f:
            self.assertEqual(f.read(), "meal1,20-12-2021,user1,5,[]\nmeal2,21-12-2021,user2,10,[]\n")

    def test_write_file_meal_filenotfound(self):
        # Test that the function prints an error message when the file is not found
        path = "nonexistent_directory/test_writefile_meal.csv"
        meal_list = [Meal("meal1", "20-12-2021", "user1", 5, [])]
        with self.assertRaises(OSError):
            write_file_meal(path, meal_list)

    def test_read_file_bill(self):
        # Test that the function reads a file correctly and returns a list of Meal objects
        path = "unittest/test_readfile_bill.csv"
        with open(path, "w") as f:
            f.write("user1,10,False\n")
            f.write("user2,5,False\n")
        bill = read_file_bill(path)
        self.assertEqual(len(bill), 2)
        self.assertEqual(bill[0].username, "user1")
        self.assertEqual(bill[0].price, "10")
        self.assertEqual(bill[0].status, "False")

    def test_add_bill_database(self):
        # Test that a new meal is added to the list
        bill_list = [Bill("user1", "10", False)]
        new_bill = Bill("user2", "5", False)
        add_bill_database(new_bill, bill_list)
        self.assertEqual(len(bill_list), 2)
        self.assertEqual(bill_list[1].username, "user2")
        self.assertEqual(bill_list[1].price, "5")
        self.assertEqual(bill_list[1].status, False)

    def test_add_existing_bill_database(self):
        # Test that a user is not added to the list if the username already exists
        bill_list = [Bill("user1", "10", False)]
        new_bill = Bill("user1", "10", False)
        add_bill_database(new_bill, bill_list)
        self.assertEqual(len(bill_list), 1)
        self.assertEqual(bill_list[0].username, "user1")
        self.assertEqual(bill_list[0].price, "10")
        self.assertEqual(bill_list[0].status, False)

    def test_write_file_bill(self):
        # Test that the function writes a list of users to a file correctly
        path = "unittest/test_writefile_bill.csv"
        bill_list = [Meal("meal1", "20-12-2021", "user1", 5, []), Meal("meal2", "21-12-2021", "user2", 10, [])]
        write_file_bill(path, bill_list)
        with open(path, "r") as f:
            self.assertEqual(f.read(), "meal1,20-12-2021,user1,5,[]\nmeal2,21-12-2021,user2,10,[]\n")

    def test_write_file_bill_filenotfound(self):
        # Test that the function prints an error message when the file is not found
        path = "nonexistent_directory/test_writefile_bill.csv"
        bill_list = [Meal("meal1", "20-12-2021", "user1", 5, [])]
        with self.assertRaises(OSError):
            write_file_bill(path, bill_list)


if __name__ == '__main__':
    unittest.main()
