import bcrypt


class Users:
    """
    class users represent a co-house member
    """

    def __init__(self, name, password):
        """ this function allows us to create a user based on his name and his password
            PRE: receive name and password
            POST: a user object

        """
        self.hashed_password = None
        self._name = name
        self._password = password

    @property
    def name(self):
        return self._name

    def change_password(self, new_password):
        self._password = new_password
        self.hash_password()

    def hash_password(self):
        byte_password = self._password.encode('utf8')
        # Generate Salt (Salt is an additional random string to prevent attack)
        my_salt = bcrypt.gensalt()
        # Hash password
        hashed = bcrypt.hashpw(byte_password, my_salt)
        self.hashed_password = hashed

    def check_password(self):
        byte_password = self._password.encode('utf8')
        # True if pwd correspond to hashed
        return bcrypt.checkpw(byte_password, self.hashed_password)

    def add_user_database(self):
        # path of file to write
        path = "database/users.csv"
        # text to write in file
        text = self._name + ' ' + str(self.hashed_password) + 'n'
        # check in the user is already in database

        def check_in_file(file_name, text_value):
            with open(file_name, 'r') as read_obj:
                for line in read_obj:
                    if text_value in line:
                        return True
            return False

        if check_in_file(path, self._name):
            return None
        # add user and password on database
        else:
            file = open(path, 'a')
            file.write("\n" + text)
            file.close()

    def delete_user_database(self):
        path = "database/users.csv"
        with open(path, 'r') as read_obj:
            for line in read_obj:
                if self._name in line:
                    print("present")
                    return True

test = Users("simon", "test")
test.add_user_database()

test.delete_user_database()