from os import urandom
from hashlib import pbkdf2_hmac


class Users:
    """
    class users represent a co-house member and his attributes
    """

    def __init__(self, username: str, hashed_password=None, my_salt=None, cooker=False):
        """ this function allows us to create a user based on his username and his password
        PRE:
        :username, username (string)
        :hashed_password, a hashed password (bytes set to None by default)
        :my_salt, a salt (bytes)
        POST: a User object created
        """
        self._username = username
        self._hashed_password = hashed_password
        self._my_salt = my_salt
        self._cooker = cooker

    def __str__(self):
        return f'{self._username},{self._hashed_password},{self._my_salt},{self._cooker}'

    @property
    def username(self):
        return self._username

    @property
    def cooker(self):
        return self._cooker

    @property
    def change_cooker(self):
        self._cooker = not self._cooker

    def is_correct_password(self, password: str):
        """ this function allows you to verify a password (str) correspond to the hashed password of user object
        PRE:
        :password, password (string len > 0)
        POST: return True if the password correspond to the hashed password of user object and False if not
        """
        return str(pbkdf2_hmac('sha256', password.encode(), self._my_salt.encode(), 100000)) == str(self._hashed_password)

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
        self._my_salt = str(urandom(16))
        self._hashed_password = pbkdf2_hmac('sha256', new_password.encode(), self._my_salt.encode(), 100000)
