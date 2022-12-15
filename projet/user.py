class Users:
    """
    class users represent a co-house' member
    """

    def __init__(self, Name, Password, bill):
        """ this function allows us to create a user based on his name and his password
            PRE: receive name and password
            POST: an user object

        """
        self._name = Name
        self._password = Password
        self.bill = bill


    @property
    def name(self):
        return self._name

    def changePassword(self, new_password):
        self._password = new_password




    pass