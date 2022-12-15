class Bill:
    """
    this class reprensent a bill for every members of the co-house

    """

    def __init__(self, date,  meal, user, status=False):
        """
            this functions allows you to create a bill for every member of the co-house
             PRE: date and status
            POST: a bill object created

        """
        self.user = user
        self.meal = meal
        self.date = date
        self.status = status
        self.amount = 0

    def displayBill(self):
        """
            this function allows you to print a bill based on meal
            PRE: a bill object and a meal object
            POST: textual representation of the bill
        """
        if self.meal.cooker == self.user.name:
            self.amount = self.amount + self.meal.getTotalPrice()
        if self.user.name in self.meal.participants:
            amountBill = self.meal.getTotalPrice() / len(self.meal.participants)
            self.amount = self.amount - amountBill

        print(f" votre facture actuelle est de {self.amount} ")

    def payBill(self):
        """
            this function permits a user to pay his bill
            PRE: a bill object and a user object
            POST: status= True that means bill has been paid
        """
        self.status = True
        self.amount = 0

    pass
