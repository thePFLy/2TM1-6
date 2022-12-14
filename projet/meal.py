import csv

class Meal:
    """ class meal """

    def __init__(self, description, date, type, cooker):
        """"
            this function allows you to create a meal object
            PRE: Description , Date , type of cook , cooker who is the responsible of the meal and the list of participants
            POST: create a meal object
        """
        self._description = description
        self.date = date
        self.type = type
        self.participants = []
        self.cooker = cooker

    def getDescription(self):
        """
             this function is aimed to return a textual description of the meal
             PRE: an meal object
             POST: a textual representation
        """
        return self._description

    def getTotalPrice(self,listofIngredients):
        """
            this function allows you to calculate the amount of a meal based of differents ingredients used
             PRE: a meal object and a list of ingredient objects
             POST: a textual representation of the amount of the meal
        """
        total_price = 0
        for ingredient in listofIngredients:
            total_price += ingredient.price
        return total_price

    def subscribe(self, user):
        """
        this function allows a user to take part of a meal
        PRE: a meal object and a user object
        POST: a new list of participants
        """
        self.participants.append(user.username)

    def unsubscribe(self,user):
        """
            this function allows a user to retire himself for a meal
            PRE: a meal object and a user object
            POST: a new list of participants
        """
        self.participants.remove(user.username)


    def changeCooker(self,user):
        """
        this function allows you to change the meal's cooker
        PRE: a meal object and a user object
        POST: a new value for cooker attribut
        """
        self.cooker = user

    def getParticipants(self):
        """
            this function allows you to display all the participants of a meal
            PRE: a meal object
            POST: a textual representation of participants
        """
        return self.participants

    def getCooker(self):
        """
            this function allows you to display the responsible of a meal
            PRE: a meal object
            POST: a textual representation of the cooker
        """
        return f"the cooker is {self.cooker}"
