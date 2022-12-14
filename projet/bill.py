class Bill:

    """
    this class reprensent a bill for every members of the co-house

    """

    def __init__(self, date, status=False):

        """
            this functions allows you to create a bill for every member of the co-house
             PRE: date and status
            POST: a bill object created

        """
        self.date = date
        self.status = status


    def displayBill(self, meal):
        """
            this function allows you to print a bill based on meal
            PRE: a bill object and a meal object
            POST: textual representation of the bill
        """
        print("Bill for meal on {}:".format(self.date))
        print("Meal: {}".format(meal.getDescription()))
        print("Total price: {}".format(meal.getTotalPrice()))
        
    def payBill(self,user):
        """
            this function permits a user to pay his bill
            PRE: a bill object and a user object
            POST: status= True that means bill has been paid
        """
        self.status = True
        print(f"{user.username} has paid the bill.")
