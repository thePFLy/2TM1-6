from user import Users
from meal import Meal
from bill import Bill


def read_file_user(path: str):
    """this function allows you to read a file and append each line as user
    PRE:
    :path, a path already created (string)
    POST: returns a list that contains the User objects from the lines of the file as parameter
    RAISE: print error if the file is not found
    """
    out = []
    try:
        with open(path, mode="r") as csvfile:
            for line in csvfile.readlines():
                tmp_line = line.strip().split(",")
                out.append(Users(tmp_line[0], tmp_line[1], tmp_line[2], tmp_line[3] == "True"))
        return out
    except FileNotFoundError:
        print('File not found.')
    except IOError:
        print('Error IO.')


def add_user_database(new_user, users_list):
    """this function allows you to add User (username hashed_password, my_salt) on list of Users object
    PRE:
    :new_user, a User object
    :users_list, a list of Users empty or not
    POST: append the User object to the list if the name of the object is not already in this list
    """
    for user in users_list:
        if user.username == new_user.username:
            return
    users_list.append(new_user)


def delete_user_database(old_user, users_list):
    """this function allows you to delete User from a list
    PRE:
    :old_user, an old User object (already in list)
    :users_list, a list empty or not
    POST: delete the object if the name of the object is already in list
    """
    for user in users_list:
        if user.username == old_user.username:
            del user


def write_file_user(path, users_list):
    """this function allows you to write objects (username hashed_password, my_salt) from list to file
    PRE:
    :path, a path already created of file
    :users_list, User list empty or not
    POST: write from a list the Users object (username hashed_password, my_salt) for each lines of the file
    """
    try:
        tmp = ""
        for user in users_list:
            tmp += str(user) + "\n"
        with open(path, mode="w") as csvfile:
            csvfile.write(tmp)
    except OSError as e:
        print(type(e), e)


def stitch_list(lst):
    """this function allows you to from a list with different strings and these strings can contain arrays,
    this function will combine these arrays even if they are not part of the same string
    PRE:
    :lst, a list with string
    POST: write from a list, a new list with from string list "[...", "...", "...]" -> "[.........]"
    """
    out = []
    flg = False
    tmp = []
    for i in lst:
        flg2 = False
        if i[0] == "[":
            tmp.append(i[2:-1])
            flg = True
            flg2 = True

        if i[-1] == "]":
            flg = False
            if flg2:
                tmp[-1] = tmp[-1][:-1]
            else:
                tmp.append(i[1:-2])
            out.append(tmp)
            tmp = []
            continue

        if flg and not flg2:
            tmp.append(i)

        if not flg:
            out.append(i)
    return out


def read_file_meal(path: str):
    """this function allows you to read a file and append each line as Meal
    PRE:
    :path, a path already created (string)
    POST: returns a list that contains the Meal objects from the lines of the file as parameter
    RAISE: print error if the file is not found
    """
    out = []
    try:
        with open(path, mode="r") as csvfile:
            for line in csvfile.readlines():
                tmp_line = stitch_list(line.strip().split(","))
                out.append(Meal(tmp_line[0], tmp_line[1], tmp_line[2], tmp_line[3], tmp_line[4]))
        return out
    except FileNotFoundError:
        print('File not found.')
    except IOError:
        print('Error IO.')


def add_meal_database(new_meal, meal_list):
    """this function allows you to add Meal (description(str), date(date), cooker(str), price_by_user (int),
    participants (tab)) on Meal list
    PRE:
    :new_meal, a Meal object
    :meal_list, a list of Meal empty or not
    POST: append the Meal object to the list if the name of the object is not already in this list
    """
    for meal in meal_list:
        if meal.date == new_meal.date:
            return
    meal_list.append(new_meal)


def write_file_meal(path, meal_list):
    """this function allows you to write objects (description(str), date(date), cooker(str), price_by_user (int),
    participants (tab)) from list to file
    PRE:
    :path, a path already created of file
    :meal_list, Meal list empty or not
    POST: write from a list the Meal object (description(str), date(date), cooker(str), price_by_user (int),
    participants (tab)) for each lines of the file
    """
    try:
        tmp = ""
        for meal in meal_list:
            tmp += str(meal) + "\n"
        with open(path, mode="w") as csvfile:
            csvfile.write(tmp)
    except OSError as e:
        print(type(e), e)


def read_file_bill(path: str):
    """this function allows you to read a file and append each line as Bill
    PRE:
    :path, a path already created (string)
    POST: returns a list that contains the Bill objects from the lines of the file as parameter
    """
    out = []
    try:
        with open(path, mode="r") as csvfile:
            for line in csvfile.readlines():
                tmp_line = line.strip().split(",")
                out.append(Bill(tmp_line[0], tmp_line[1], tmp_line[2]))
        return out
    except FileNotFoundError:
        print('File not found.')
    except IOError:
        print('Error IO.')


def add_bill_database(new_bill, bill_list):
    """this function allows you to add Bill (username(str), price(int), status(bool)) on database (csv file)

    PRE:
    :new_bill, a Bill object
    :bill_list, a list of Bill empty or not
    POST: append the Bill object to the list if the name of the object is not already in this list
    """
    for bill in bill_list:
        if bill.username == new_bill.username:
            return
    bill_list.append(new_bill)


def write_file_bill(path, bill_list):
    """this function allows you to write Bill objects (username(str), price(int), status(bool)) from list to file
    PRE:
    :path, a path already created of file
    :bill_list, Bill list empty or not
    POST: write from a list the Bill object (username(str), price(int), status(bool)) for each lines of the file
    """
    try:
        tmp = ""
        for bill in bill_list:
            tmp += str(bill) + "\n"
        with open(path, mode="w") as csvfile:
            csvfile.write(tmp)
    except OSError as e:
        print(type(e), e)
