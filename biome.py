import enemy
import random
import food
import items
import merchant

class Biome():
    def __init__(self, game):
        self.game = game
        self.icon = ""
        self.enemies = self.generateEnemies()
        self.item = self.generateItems()
        self.merchant = self.generateMerchant()
    
    def getType(self):
        return self.__class__.__name__
    
    def getIcon(self):
        return self.icon
    
    def getPossibleEnemies(self):
        possibleenemies = []
        for enemytype in enemy.enemyTypes:
            if enemytype.nativeTo == self.getType():
                possibleenemies.append(enemytype)
        return possibleenemies
    
    def getTargetItem(self):
        if self.item:
            return self.item[0]
        else:
            return None
    
    def getItemName(self):
        if self.item:
            return self.item[0].__class__.__name__
        else:
            return "-"
    
    def generateAnEnemy(self):
        enemy = random.choice(self.getPossibleEnemies())(self.game)
        self.game.enemies.append(enemy)
        return enemy
    
    def generateEnemies(self):
        randompercentage = random.randint(0, 100)
        chance = 20
        if randompercentage < 100 - chance:
            return []
        else:
            numberofenemies = random.randint(1,2)
            return [self.generateAnEnemy() for i in range(numberofenemies)]
    
    def getPossibleFoods(self):
        possiblefoods = []
        for foodtype in food.foodtypes:
            if foodtype.nativeTo == self.getType():
                possiblefoods.append(foodtype)
        return possiblefoods
    
    def generateItems(self):
        items = []
        if random.randint(0, 100) < 20:
            items.append(random.choice(self.getPossibleFoods())(self.game))
        if random.randint(0, 100) < 30:
            items.append(random.choice(self.getPossibleItems())(self.game))
            print(self.getPossibleItems())
        return items
    
    def getPossibleItems(self):
        possibleGears = items.gearTypes.copy()
        possibleWeapons = items.weaponTypes.copy()
        return possibleGears + possibleWeapons
    
    def popItem(self):
        return self.item.pop(0)
    
    def removeItem(self, item):
        try:
            self.item.remove(item)
        except ValueError:
            pass
    
    def generateMerchant(self):
        if random.randint(0, 100) < 90:
            return merchant.Merchant(self.game)
        else:
            return None

class Desert(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🏜️"
        self.imagesrc = "desert.png"

class Jungle(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🌴"
        self.imagesrc = "jungle.png"

class Meadow(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🏞️"
        self.imagesrc = "meadow.png"

class Tundra(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "❄️"
        self.imagesrc = "tundra.png"


biomeTypes = Biome.__subclasses__()
