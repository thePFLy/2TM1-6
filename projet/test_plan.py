import unittest
from class_plan import Planning


class TestPlanning(unittest.TestCase):
    def test_init(self):
        # create a Planning object with a username and date
        planning = Planning("user1", "2022-12-21")

        # check that the username and date are set correctly
        self.assertEqual(planning.username, "user1")
        self.assertEqual(planning.date, "2022-12-21")


if __name__ == '__main__':
    unittest.main()
