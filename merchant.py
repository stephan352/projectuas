import character
import random
import food
import items

class Merchant(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.inventory = self.generateInventory()
    
    def generateInventory(self):
        noOfItems = random.randint(5, 10)
        possibleitems = items.gearTypes + items.weaponTypes + food.foodtypes
        inventory = []
        for i in range(noOfItems):
            item = random.choice(possibleitems)(self.game)
            item.price = random.randint(5, 20)
            inventory.append(item)
        return inventory

