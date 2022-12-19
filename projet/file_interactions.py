from user import Users
from meal import Meal


def read_file_user(path: str):
    """this function allows you to read a file and append each line as user
    PRE:
    :path, a path already created (string)
    POST: returns a list that contains the User objects from the lines of the file as parameter
    """
    out = []
    with open(path, mode="r") as csvfile:
        for line in csvfile.readlines():
            tmp_line = line.strip().split(",")
            out.append(Users(tmp_line[0], tmp_line[1], tmp_line[2], tmp_line[3] == "True"))
    return out


def add_user_database(new_user, users_list):
    """this function allows you to add User (username hashed_password, my_salt) on database (csv file)

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
    tmp = ""
    for user in users_list:
        tmp += str(user) + "\n"
    with open(path, mode="w") as csvfile:
        csvfile.write(tmp)


def read_file_meal(path: str):
    """this function allows you to read a file and append each line as user
    PRE:
    :path, a path already created (string)
    POST: returns a list that contains the User objects from the lines of the file as parameter
    """
    out = []
    with open(path, mode="r") as csvfile:
        for line in csvfile.readlines():
            tmp_line = line.strip().split(",")
            out.append(Meal(tmp_line[0], tmp_line[1], tmp_line[2], tmp_line[3]))
    return out


def add_meal_database(new_meal, meal_list):
    """this function allows you to add User (username hashed_password, my_salt) on database (csv file)

    PRE:
    :new_user, a User object
    :users_list, a list of Users empty or not
    POST: append the User object to the list if the name of the object is not already in this list
    """
    for meal in meal_list:
        if meal.date == new_meal.date:
            return
    meal_list.append(new_meal)


def write_file_meal(path, meal_list):
    """this function allows you to write objects (username hashed_password, my_salt) from list to file
    PRE:
    :path, a path already created of file
    :users_list, User list empty or not
    POST: write from a list the Users object (username hashed_password, my_salt) for each lines of the file
    """
    tmp = ""
    for meal in meal_list:
        tmp += str(meal) + "\n"
    with open(path, mode="w") as csvfile:
        csvfile.write(tmp)
