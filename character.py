class Character():
    def __init__(self, game):
        self.game = game
        self.position = [9,0]
        self.health = 100
        self.icon = ""
    
    def getIcon(self):
        return self.icon
    
    def getPosition(self):
        return self.position.copy()
    
    def showPosition(self):
        print(self.position)


    def goLeft(self):
        self.position[0] -= 1

    def goRight(self):
        self.position[0] += 1

    def goUp(self):
        self.position[1] -= 1

    def goDown(self):
        self.position[1] += 1

class Enemy(Character):
    def __init__(self, game):
        super().__init__(game)