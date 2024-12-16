import enemy
import random
import food

class Biome():
    def __init__(self, game):
        self.game = game
        self.position = [0,0] #blm selesai
        self.icon = ""
        self.enemies = self.generateEnemies()
        self.item = self.generateFood()
    
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
    
    def getFoodName(self):
        if self.item:
            return self.item[0].__class__.__name__
        else:
            return "-"
    
    def generateAnEnemy(self):
        return random.choice(self.getPossibleEnemies())(self.game)
    
    def generateEnemies(self):
        randompercentage = random.randint(0, 100)
        if randompercentage < 5:
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
    
    def generateFood(self):
        if random.randint(0, 100) < 15:
            return [random.choice(self.getPossibleFoods())()]
        else:
            return []
    
    def popFood(self):
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
