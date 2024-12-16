import character
import random
import food
import items

class Merchant(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.gold = 500
        self.buyingprice = random.randint(3,5)
        self.inventory = self.generateInventory()
    
    def generateInventory(self):
        noOfItems = random.randint(2,5)
        possibleitems = items.gearTypes + items.weaponTypes + food.foodtypes
        inventory = []
        self.prices = {}
        for i in range(noOfItems):
            item = random.choice(possibleitems)(self.game)
            price = random.randint(5, 20)
            self.prices[item] = price
            inventory.append(item)
        return inventory
    
    def lose(self, item):
        if item in self.inventory:
            self.prices.pop(item)
            self.inventory.remove(item)
    
    def gain(self, item, price):
        self.inventory.append(item)
        self.prices[item] = price
    
    #def giveItem(self):

