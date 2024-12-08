class Biome():
    def __init__(self, game):
        self.game = game
        self.position = [0,0] #blm selesai
        self.icon = ""
    
    def getIcon(self):
        return self.icon

class Desert(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🏜️"
        

class Jungle(Biome):
    def __init__(self, game):
        super().__init__(game)
        self.icon = "🌴"

biomeTypes = Biome.__subclasses__()