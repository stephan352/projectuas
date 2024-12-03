class player():
    def __init__(self):
        self.position = [5,8]
        self.health = 100
    
    def goLeft(self):
        pass

    def getPosition(self):
        return self.position.copy()
    
    def showPosition(self):
        print(self.position)