from user import Users
from Ingredient import Ingredient
from meal import Meal

ing1 = Ingredient('pattes', 1, 10)
ing2 = Ingredient('creme cullinaire', 2, 2)
user1 = Users('brice', '0000')
user2 = Users('ronald', '0001')
user3 = Users('toto', '0002')
user4 = Users('tata', '0003')

listofIngredient = [ing1, ing2]

meal1 = Meal('pattes aux lardons ', '02/05/2000', 'dinner', user1, listofIngredient)
meal1.subscribe(user2)
meal1.subscribe(user3)
meal1.subscribe(user4)
meal1.getCooker()


meal1.getParticipants()
print(meal1.getTotalPrice())

