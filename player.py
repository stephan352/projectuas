class player():
    def __init__(self):
        self.position = [5,8]
        self.health = 100


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