import csv

class Bill:
    """
    this class reprensent a bill for every members of the co-house
    """

    def __init__(self, date, status=False):
        """
            this functions allows you to create a bill for every member of the co-house
             PRE: a str date and a boolean status
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
        bill_str = "Bill for meal on {}:\n".format(self.date)
        bill_str += "Meal: {}\n".format(meal.getDescription())
        bill_str += "Total price: {}\n".format(meal.getTotalPrice())
        return bill_str

    def payBill(self, user):
        """
            this function permits a user to pay his bill
            PRE: a bill object and a user object
            POST: status = True that means bill has been paid
        """
        self.status = True
        print(f"{user.username} has paid the bill.")

def addDataBill(bill):
    """
        this function add a bill in a csv file
        PRE: a bill object
        POST: the bill is add in the bill.csv file
    """
    with open('bill.csv', 'a') as csvfile:
        fieldnames = ['Date', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(
            {'Date': bill.date, 'Status': bill.status})


def initDataBill():
    list = []
    """
        initialise bill_list with the contents of the csv file bill.csv
        PRE: a csv file
        POST: a list of bill object in bill_list
    """
    with open('bill.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bill = Bill(row["Date"], row["Status"])
            list.append(bill)
    return list

bill_list = initDataBill()
            
#test
facture = Bill("12-12-2014")
addDataBill(facture)
for i in bill_list:
    print(i.date+ " " + i.status)
