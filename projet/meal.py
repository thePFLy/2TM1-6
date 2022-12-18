import csv
import logging

class Meal:
    """ class meal """

    def __init__(self, description, date, type, cooker):
        """"
            this function allows you to create a meal object
            PRE: an str Description , Date , type of cook , cooker who is the responsible of the meal and the list of participants
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
        POST: add a new person in the list of participants
        """
        self.participants.append(user.username)

    def unsubscribe(self,user):
        """
            this function allows a user to retire himself for a meal
            PRE: a meal object and a user object
            POST: remove a person from list of participants
        """
        self.participants.remove(user.username)


    def changeCooker(self,user):
        """
        this function allows you to change the meal's cooker
        PRE: a meal object and a user object
        POST: change the cooker name in cooker attribut of meal object
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

def addDataMeal(meal):
    """
        this function add a meal in a csv file
        PRE: a meal object
        POST: the meal is add in the meal.csv file
    """
    try:
        with open('meal.csv', 'a') as csvfile:
            fieldnames = ['Description', 'Date', 'Type', 'Participants', 'Cooker']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {'Description': meal._description, 'Date': meal.date, 'Type': meal.type,
                 'Participants': meal.participants, 'Cooker': meal.cooker})
    except OSError as e:
            print(type(e), e)


def initDataMeal():
    meal_list = []
    """
        initialise meal_list with the contents of the csv file meal.csv
        PRE: a csv file
        POST: a list of meal object in meal_list
    """
    try:
        with open('meal.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                meal = Meal(row["Description"], row["Date"], row["Type"], row["Cooker"])
                meal.participants = row["Participants"]
                meal_list.append(meal)
        return meal_list
    except IOError:
        logging.exception('')
    except FileNotFoundError:
        print('file not found')



meal_list = initDataMeal()

#test
facture = Meal("sandiwch","12-12-2014","Lunch","Markus")
addDataMeal(facture)
for i in meal_list:
    print(i.date+ " "+i._description)

