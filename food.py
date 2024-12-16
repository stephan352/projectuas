class Food():
    def __init__(self, game):
        self.game = game
        self.regenerateHP = 50
        self.regenerateEnergy = 200
    
    def useEffect(self):
        self.game.player.health += self.regenerateHP
        self.game.player.energy += self.regenerateEnergy

class Banana(Food):
    nativeTo = "Jungle"
    def __init__(self, game):
        super().__init__(game)

class Cactus(Food):
    nativeTo = "Desert"
    def __init__(self, game):
        super().__init__(game)

class Apple(Food):
    nativeTo = "Meadow"
    def __init__(self, game):
        super().__init__(game)

class Berries(Food):
    nativeTo = "Meadow"
    def __init__(self, game):
        super().__init__(game)

class Salmon(Food):
    nativeTo = "Tundra"
    def __init__(self, game):
        super().__init__(game)

foodtypes = Food.__subclasses__()
