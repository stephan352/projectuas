import enemy
import random

class Biome():
    def __init__(self, game):
        self.game = game
        self.position = [0,0] #blm selesai
        self.icon = ""
        self.enemies = self.generateEnemies()
    
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
    
    def generateAnEnemy(self):
        return random.choice(self.getPossibleEnemies())(self.game)
    
    def generateEnemies(self):
        randompercentage = random.randint(0, 100)
        if randompercentage < 70:
            return []
        else:
            numberofenemies = random.randint(1,2)
            return [self.generateAnEnemy() for i in range(numberofenemies)]

class Desert(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🏜️"
    
    # def getType(self):
    #     return "Desert"
        

class Jungle(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🌴"
    
    # def getType(self):
    #     return "Jungle"

biomeTypes = Biome.__subclasses__()
