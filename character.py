class Character():
    def __init__(self, game):
        self.game = game
        self.isAlive = True
        self.position = [0,0]
        self.health = 100
        self.icon = ""
    
    def getIcon(self):
        return self.icon
    
    def getPosition(self):
        return self.position.copy()
    
    def showPosition(self):
        print(self.position)
    

    def goToPosition(self, x, y):
        map_dimensionX = self.game.map.getMapDimensions()[0]
        map_dimensionY = self.game.map.getMapDimensions()[1]
        if 0 <= x < map_dimensionX and 0 <= y < map_dimensionY:
            self.position = [x, y]
        else:
            print("Out of boundaries!")

    def goLeft(self):
        self.goToPosition(self.position[0] - 1, self.position[1])

    def goRight(self):
        self.goToPosition(self.position[0] + 1, self.position[1])

    def goUp(self):
        self.goToPosition(self.position[0], self.position[1] - 1)

    def goDown(self):
        self.goToPosition(self.position[0], self.position[1] + 1)
    
    def recieveAttack(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.isAlive = False
