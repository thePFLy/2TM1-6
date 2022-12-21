
class Meal:
    """ class meal """

    def __init__(self, description, date, cooker, price_by_user: int, participants=None):
        """"
        this function allows you to create a meal object
        PRE: a str Description, Date, cooker who is the responsible for the meal and the list of participants
        :description, string with description of the meal
        :date, string date of the meal
        :cooker, string username of cooker (from Users)
        :price_by_user, int cost of meal
        :participants, list of participants
        POST: create a meal object
        """
        if participants is None:
            participants = []
        self._description = description
        self.date = date
        self.participants = participants
        self.cooker = cooker
        self.price_by_user = price_by_user

    def __str__(self):
        return f'{self._description},{self.date},{self.cooker},{self.price_by_user},{self.participants}'

    @property
    def description(self):
        return self._description

    def get_description(self):
        """
        this function is aimed to return a textual description of the meal
        PRE: a meal object
        POST: a textual representation
        """
        return self._description

    @staticmethod
    def get_total_price(list_ingredients):
        """
        this function allows you to calculate the amount of a meal based of different ingredients used
        PRE:
        :list_ingredients, list of ingredients objects
        POST: a textual representation of the amount of the meal
        """
        total_price = 0
        for ingredient in list_ingredients:
            total_price += ingredient.price
        return total_price

    def subscribe(self, user):
        """
        this function allows a user to take part of a meal
        PRE:
        :user, a User object
        POST: add a new username in the list of participants
        """
        self.participants.append(user.username)

    def unsubscribe(self, user):
        """
        this function allows a user to retire himself for a meal
        PRE:
        :user, a User object
        POST: remove a person from list of participants
        """
        self.participants.remove(user.username)

    def change_cooker(self, user):
        """
        this function allows you to change the meal's cooker
        PRE: a meal object and a user object
        :user a User object
        POST: change the cooker name in cooker attribute of meal object
        """
        self.cooker = user

    def get_participants(self):
        """
        this function allows you to display all the participants of a meal
        PRE: a meal object
        POST: a textual representation of participants
        """
        return self.participants

    def get_cooker(self):
        """
        this function allows you to display the responsible for a meal
        PRE: a meal object
        POST: a textual representation of the cooker
        """
        return f"the cooker is {self.cooker}"
