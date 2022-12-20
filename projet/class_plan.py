class Planning:
    """
        this class represent a day of the planning
    """
    def __init__(self, username: str, date: str):
        """
        this functions allows you to create a Planning objects
        PRE:
        :username, string which contains the username which cook
        :date, string of the date cook
        POST: a bill object created
        """
        self.username = username
        self.date = date

