
class Bill:
    """
    this class represent a bill for every member of the co-house
    """

    def __init__(self, username: str, price: str, status=False):
        """
            this functions allows you to create a bill for every member of the co-house
            PRE: a str date and a boolean status
            :username, string which contains the username to whom the invoice belongs
            :price, int the amount the user owes or others owe him
            :status, bool True if the invoice was paid
            POST: a bill object created
        """
        self.username = username
        self.price = price
        self.status = status

    def __str__(self):
        return f"{self.username},{self.price},{self.status}"

    def get_bill(self):
        """
        this function permits to get the bill of user
        PRE: a bill object
        POST: print the amount the user owes or others owe him
        """
        if int(self.price) < 0:
            print(f"you have {abs(int(self.price))} euros left to pay")
        if int(self.price) > 0:
            print(f"other users owe you {abs(int(self.price))} euro")
        if int(self.price) == 0:
            print(f"You have already paid our bill")

    def payBill(self):
        """
        this function permits a user to pay his bill
        PRE: a bill object and a user object
        POST: status = True that means bill has been paid
        """
        self.status = True
        print(f"{self.username} has paid the bill.")
