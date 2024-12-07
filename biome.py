class Biome():
    def __init__(self, game):
        self.game = game

class Desert(Biome):
    def __init__(self, game):
        super().__init__(game)

class Jungle(Biome):
    def __init__(self, game):
        super().__init__(game)

biomeTypes = Biome.__subclasses__()