from unittest import TestCase
import unittest

from meal import Meal
from user import Users

user1 = Users('brice', '0000')
user2 = Users('ronald', '0001')
user3 = Users('toto', '0002')
user4 = Users('tata', '0003')

listofIngredient = ['creme cullinaire', 'lardon', 'pattes']

participants1 = [user2, user3]
participants2 = []




class TestMeal(TestCase):
    def setUp(self):
        # Configurez l'environnement de test et créez les objets nécessaires pour les tests
        self.obj1 = Meal('pattes aux lardons ', '02/05/2000', user1, 20)
        self.obj2 = Meal('pattes aux lardons ', '02/05/2000', user1, 10)
        self.obj1.participants = participants1
        self.obj2.participants = participants2


    def test_get_description(self):
        result = self.obj1.get_description()
        self.assertEqual(result, "pattes aux lardons ")

    def test_subscribe(self):
        result1 = self.obj1.subscribe(user4)
        result2 = self.obj2.subscribe(user4)
        self.assertEqual(len(result1), 3)
        self.assertEqual(len(result2), 1)

    def test_unsubscribe(self):
        result1 = self.obj1.unsubscribe(user2)
        self.assertEqual(len(result1), 2)
        self.assertEqual(self.obj1.participants[0].username, "toto", "Le seul participant devrait être ronald")

    def test_get_participants(self):
        result1 = self.obj1.get_participants()
        result2 = self.obj2.get_participants()
        self.assertEqual(len(result1), 2)
        self.assertEqual(self.obj1.participants[0].username, "ronald", "Le seul participant devrait être ronald")
        self.assertEqual(self.obj1.participants[1].username, "toto", "Le seul participant devrait être toto")
        self.assertEqual(len(result2), 0)









if __name__ == "__main__":
    unittest.main()




