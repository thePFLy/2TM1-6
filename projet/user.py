from csv import reader
import os
import hashlib
import hmac

users_list = []


def read_file(path):
    # add(user(pwd,hash,salt))
    with open(path, mode="r") as csvfile:
        spam_reader = reader(csvfile)
        for lines in spam_reader:
            # create user object from lines
            if Users(lines[0], lines[1], lines[2]) not in users_list:
                users_list.append(Users(lines[0], lines[1], lines[2]))


def add_user_database(user):
    """this function allows you to add User (username hashed_password) on database (csv file)

    PRE: receive a User object
    POST: Check if file is already in database, if not add it
    """
    print(user.__str__())
    flag = False
    for users in users_list:
        if users.__str__() == user.__str__():
            flag = True
    print(flag)
    if flag is False:
        users_list.append(user)




def delete_user_database(user):
    """this function allows you to delete User on database (csv file)

    PRE: receive a User object
    POST: look for the line of the user and delete it
    """
    path = "database/users.csv"
    lookup = user.__str__()
    the_line = 0
    with open(path) as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup in line:
                the_line = num

    with open(path, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
        # pointer for position
        ptr = 1
        # opening in writing mode
        with open(path, 'w') as fw:
            for line in lines:
                # remove the line of User object
                if ptr != the_line:
                    fw.write(line)
                ptr += 1


def hash_new_password(password: str):
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, pw_hash


def is_correct_password(salt: bytes, pw_hash: bytes, password: str):
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )


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

    @property
    def username(self):
        return self._username

    def change_password(self, new_password, old_password=None):
        """this function allows you to change the password of a User object

        PRE: receive a new password for the User object
        POST: change the password and encrypt it
        """
        if self._hashed_password is None and self._my_salt is None:
            self._my_salt, self._hashed_password = hash_new_password(new_password)
        elif is_correct_password(self._my_salt, self._hashed_password, old_password):
            self._my_salt, self._hashed_password = hash_new_password(new_password)
        else:
            print(f'old password incorrect')

    def __str__(self):
        return f'{self._username},{self._hashed_password},{self._my_salt}'


print(read_file("database/users.csv"))
print(add_user_database(Users("brice","ok","test")))
print(users_list)