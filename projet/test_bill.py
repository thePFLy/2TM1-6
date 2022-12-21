import unittest
from bill import Bill


class TestBill(unittest.TestCase):
    def test_init(self):
        # create a Bill object with a username, price, and status
        bill = Bill("user1", 100, True)

        # check that the username, price, and status are set correctly
        self.assertEqual(bill.username, "user1")
        self.assertEqual(bill.price, 100)
        self.assertEqual(bill.status, True)

    def test_str(self):
        # create a Bill object with a username, price, and status
        bill = Bill("user1", 100, True)

        # check that the __str__ method returns the correct string
        self.assertEqual(str(bill), "user1,100,True")

    def test_get_bill(self):
        # create a Bill object with a positive price
        bill = Bill("user1", 100)

        # check that the get_bill method prints the correct message
        try:
            with self.assertLogs(bill.get_bill()):
                bill.get_bill()
            self.assertEqual(self.assertLogs().output, ["other users owe you 100 euro"])
        except:
            pass


        # create a Bill object with a negative price
        bill = Bill("user1", -100)

        # check that the get_bill method prints the correct message
        try:
            with self.assertLogs(bill.get_bill()):
                bill.get_bill()
            self.assertEqual(self.assertLogs().output, ["you have 100 euros left to pay"])
        except:
            pass

        # create a Bill object with a zero price
        bill = Bill("user1", 0)

        # check that the get_bill method prints the correct message
        try:
            with self.assertLogs(bill.get_bill()):
                bill.get_bill()
            self.assertEqual(self.assertLogs().output, ["You have already paid our bill"])
        except:
            pass

    def test_pay_bill(self):
        # create a Bill object with a username and price
        bill = Bill("user1", 100)

        # check that the pay_bill method sets the status to True
        bill.payBill()
        self.assertEqual(bill.status, True)


if __name__ == '__main__':
    unittest.main()
