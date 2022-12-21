from unittest import TestCase
import unittest

from meal import Meal
from user import Users
from Ingredient import Ingredient
user1 = Users('brice', '0000')
user2 = Users('ronald', '0001')
user3 = Users('toto', '0002')
user4 = Users('tata', '0003')

ing1 = Ingredient('pattes', 1, 10)
ing2 = Ingredient('creme cullinaire', 2, 2)

listofIngredient = [ing1, ing2]


class TestMeal(TestCase):
    def setUp(self):
        # Configurez l'environnement de test et créez les objets nécessaires pour les tests
        self.obj1 = Meal('pattes aux lardons ', '02/05/2000', 'dinner', user1, listofIngredient)

    def test_get_description(self):
        result = self.obj1.get_description()
        self.assertEqual(result, "pattes aux lardons ")




if __name__ == "__main__":
    unittest.main()




