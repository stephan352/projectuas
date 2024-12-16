import enemy
import random
import food
import items

class Biome():
    def __init__(self, game):
        self.game = game
        self.position = [0,0] #blm selesai
        self.icon = ""
        self.enemies = self.generateEnemies()
        self.item = self.generateItems()
    
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
        if random.randint(0, 100) < 95:
            items.append(random.choice(self.getPossibleFoods())(self.game))
        if random.randint(0, 100) < 95:
            items.append(random.choice(self.getPossibleItems())(self.game))
        return items
    
    def getPossibleItems(self):
        possibleGears = items.gearTypes.copy()
        possibleWeapons = items.weaponTypes.copy()
        return possibleGears + possibleWeapons
    
    def popItem(self):
        return self.item.pop(0)

class Desert(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🏜️"      

class Jungle(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🌴"

class Meadow(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🏞️"

class Tundra(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "❄️"


biomeTypes = Biome.__subclasses__()
