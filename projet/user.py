import os
import hashlib


path_database = "database/users.csv"


def read_file(path: str):
    """this function allows you to read a file and append each line as user
    PRE:
    :path, a path already created (string)
    POST: returns a list that contains the user objects from the lines of the file as parameter
    """
    out = []
    with open(path, mode="r") as csvfile:
        for line in csvfile.readlines():
            tmp_line = line.strip().split(",")
            out.append(Users(tmp_line[0], tmp_line[1], tmp_line[2]))
    return out


def add_user_database(new_user, users_list):
    """this function allows you to add User (username hashed_password, my_salt) on database (csv file)

    PRE:
    :new_user, a User object
    :users_list, a list of users empty or not
    POST: append the user object to the list if the name of the object is not already in this list
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


def write_file(path, users_list):
    """this function allows you to write objects (username hashed_password, my_salt) from list to file
    PRE:
    :path, a path already created of file
    :users_list, user list empty or not
    POST: write from a list the users object (username hashed_password, my_salt) for each lines of the file
    """
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
        PRE:
        :username, username (string)
        :hashed_password, a hashed password (bytes set to None by default)
        :my_salt, a salt (bytes)
        POST: a user object created
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
        """ this function allows you to verify a password (str) correspond to the hashed password of user object
        PRE:
        :password, password (string len > 0)
        POST: return True if the password correspond to the hashed password of user object and False if not
        """
        return hashlib.pbkdf2_hmac('sha256', password.encode(), self._my_salt, 100000) == self._hashed_password

    def change_password(self, new_password: str, old_password: str = None):
        """this function allows you to change the password of a User object

        PRE:
        :new_password, a new password (str len >0) for the User object
        :old_password, an old password (str len >0) already created or which don't exist for the User object
        POST: Change the hash and salt of user object if old password correspond or is not defined
        """
        if old_password is not None and not self.is_correct_password(old_password):
            print(f"wrong password")
            return
        self._my_salt = os.urandom(16)
        self._hashed_password = hashlib.pbkdf2_hmac('sha256', new_password.encode(), self._my_salt, 100000)
