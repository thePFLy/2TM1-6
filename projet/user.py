import os
import hashlib


path_database = "database/users.csv"


def read_file(path):
    out = []
    with open(path, mode="r") as csvfile:
        for line in csvfile.readlines():
            tmp_line = line.strip().split(",")
            out.append(Users(tmp_line[0], tmp_line[1], tmp_line[2]))
    return out


def add_user_database(new_user, users_list):
    """this function allows you to add User (username hashed_password) on database (csv file)

    PRE: receive a User object
    POST: Check if file is already in database, if not add it
    """
    for user in users_list:
        if user.username == new_user.username:
            return
    users_list.append(new_user)


def delete_user_database(old_user, users_list):
    """this function allows you to delete User on database (csv file)

    PRE: receive a User object
    POST: look for the line of the user and delete it
    """
    for user in users_list:
        if user.username == old_user.username:
            del user


def write_file(path, users_list):
    tmp = ""
    for user in users_list:
        tmp += str(user) + "\n"
    with open(path, mode="w") as csvfile:
        csvfile.write(tmp)


class Users:
    """
    class users represent a co-house member and his attributes
    """

    def __init__(self, username: str, hashed_password: str = None, my_salt: str = None):
        """ this function allows us to create a user based on his username and his password
            PRE: receive username and password
            POST: a user object
            RAISE:

        """
        self._username = username
        self._hashed_password = hashed_password
        self._my_salt = my_salt

    def __str__(self):
        return f'{self._username},{self._hashed_password},{self._my_salt}'

    @property
    def username(self):
        return self._username

    def is_correct_password(self, password: str):
        return hashlib.pbkdf2_hmac('sha256', password.encode(), self._my_salt, 100000) == self._hashed_password

    def change_password(self, new_password, old_password=None):
        """this function allows you to change the password of a User object

        PRE: receive a new password for the User object
        POST: change the password and encrypt it
        """
        if old_password is not None and not self.is_correct_password(old_password):
            print(f"wrong password")
            return
        self._my_salt = os.urandom(16)
        self._hashed_password = hashlib.pbkdf2_hmac('sha256', new_password.encode(), self._my_salt, 100000)


user_list = read_file(path_database)
test = Users("rsf")
test.change_password("test")
add_user_database(test, user_list)
write_file(path_database, user_list)
