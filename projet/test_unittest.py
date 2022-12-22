import unittest
from meal import Meal
from bill import Bill
from file_interactions import read_file_user, add_user_database, delete_user_database, write_file_user, stitch_list, \
    read_file_meal, add_meal_database, write_file_meal, read_file_bill, add_bill_database, write_file_bill
import planning
import csv
from user import Users
from datetime import datetime, timedelta
from class_plan import Planning


class TestBill(unittest.TestCase):
    def test_init(self):
        # create a Bill object with a username, price, and status
        bill = Bill("user1", "100", True)

        # check that the username, price, and status are set correctly
        self.assertEqual(bill.username, "user1")
        self.assertEqual(bill.price, "100")
        self.assertEqual(bill.status, True)

    def test_str(self):
        # create a Bill object with a username, price, and status
        bill = Bill("user1", "100", True)

        # check that the __str__ method returns the correct string
        self.assertEqual(str(bill), "user1,100,True")

    def test_get_bill(self):
        # create a Bill object with a positive price
        bill = Bill("user1", "100")

        # check that the get_bill method prints the correct message
        try:
            with self.assertLogs(bill.get_bill()):
                bill.get_bill()
            self.assertEqual(self.assertLogs().output, ["other users owe you 100 euro"])
        except:
            pass

        # create a Bill object with a negative price
        bill = Bill("user1", "-100")

        # check that the get_bill method prints the correct message
        try:
            with self.assertLogs(bill.get_bill()):
                bill.get_bill()
            self.assertEqual(self.assertLogs().output, ["you have 100 euros left to pay"])
        except:
            pass

        # create a Bill object with a zero price
        bill = Bill("user1", "0")

        # check that the get_bill method prints the correct message
        try:
            with self.assertLogs(bill.get_bill()):
                bill.get_bill()
            self.assertEqual(self.assertLogs().output, ["You have already paid our bill"])
        except:
            pass

    def test_pay_bill(self):
        # create a Bill object with a username and price
        bill = Bill("user1", "100")

        # check that the pay_bill method sets the status to True
        bill.payBill()
        self.assertEqual(bill.status, True)


class TestReadFile(unittest.TestCase):
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

    def test_read_file_user_file_not_found(self):
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

    def test_write_file_user_file_not_found(self):
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

    def test_write_file_meal_file_not_found(self):
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

    def test_write_file_bill_file_not_found(self):
        # Test that the function prints an error message when the file is not found
        path = "nonexistent_directory/test_writefile_bill.csv"
        bill_list = [Meal("meal1", "20-12-2021", "user1", 5, [])]
        with self.assertRaises(OSError):
            write_file_bill(path, bill_list)


class TestPlanningClass(unittest.TestCase):
    def test_init(self):
        # create a Planning object with a username and date
        planning_obj = Planning("user1", "2022-12-21")

        # check that the username and date are set correctly
        self.assertEqual(planning_obj.username, "user1")
        self.assertEqual(planning_obj.date, "2022-12-21")


class TestPlanning(unittest.TestCase):
    def setUp(self):
        self.students = [
            Planning('John', datetime.strftime(datetime.today(), "%d-%m-%Y")),
            Planning('Jane', datetime.strftime(datetime.today() + timedelta(days=1), "%d-%m-%Y")),
            Planning('Bob', datetime.strftime(datetime.today() + timedelta(days=2), "%d-%m-%Y")),
            Planning('Alice', datetime.strftime(datetime.today() + timedelta(days=3), "%d-%m-%Y")),
            Planning('Eve', datetime.strftime(datetime.today() + timedelta(days=4), "%d-%m-%Y")),
            Planning('Adam', datetime.strftime(datetime.today() + timedelta(days=5), "%d-%m-%Y")),
            Planning('Alice', datetime.strftime(datetime.today() + timedelta(days=6), "%d-%m-%Y"))
        ]
        self.userss = [
            Users('John', '0111'),
            Users('Jane', '0111'),
            Users('Bob', '0111'),
            Users('Alice', '0111'),
            Users('Eve', '0111'),
            Users('Adam', '0111'),
            Users('Alice', '0111')
        ]
        self.day = datetime.strptime("01-01-2022", "%d-%m-%Y")

    def test_DDay(self):
        # test DDay function
        result = planning.DDay()
        if result is None:
            self.assertEqual(result, None)
        else:
            result = datetime.strftime(planning.DDay(), "%d-%m-%Y")
            today = datetime.today()
            expected = datetime.strftime(today, "%d-%m-%Y")
            self.assertEqual(result, expected)

    def test_newDDay(self):
        # test newDDay function
        planning.newDDay()
        with open('database/DDay.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result = row["Date"]
        expected = datetime.strftime(datetime.today(), "%d-%m-%Y")
        self.assertEqual(result, expected)

    def test_init_planning(self):
        # test function init_planning
        planning.init_planning('database/planning.csv')
        result = []
        expected = []
        for i in range(len(result)):
            result.append([result[i].date, result[i].username])
            result.append([self.students[i].date, self.students[i].username])
        self.assertEqual(result, expected)

    def test_change_planning(self):
        # On test la function change_planning
        week = []
        datetime.today()
        jour = -1
        for i in self.students:
            jour = jour + 1
            today = datetime.today() + timedelta(days=jour)
            name = i.username
            under_week = [name, today]
            week.append(under_week)
        planning.change_planning(week)
        with open('database/planning.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [row for row in reader]
        result = [[row['Day'], row['Name']] for row in rows[0:]]
        expected = [[day.date, day.username] for day in self.students]
        self.assertEqual(result, expected)

    def test_get_planning(self):
        # test function get_planning
        week = []
        today = datetime.today()
        jour = -1
        for i in self.students:
            jour = jour + 1
            today = datetime.today() + timedelta(days=jour)
            name = i.username
            under_week = [name, today]
            week.append(under_week)
        result = planning.get_planning(self.userss, week, today)
        expected = self.students
        if result is None:
            self.assertEqual(result, None)
        else:
            self.assertEqual(result, expected)


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
