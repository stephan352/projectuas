import character
import biome

class Enemy(character.Character):
    def __init__(self, game):
        super().__init__(game)
    
class GiantScorpion(Enemy):
    # nativeTo = biome.Desert
    nativeTo = "Desert"
    def __init__(self, game):
        super().__init__(game)
        # self.nativeTo = biome.Desert

class Gorilla(Enemy):
    # nativeTo = biome.Jungle
    nativeTo = "Jungle"
    def __init__(self, game):
        super().__init__(game)
        # self.nativeTo = biome.Jungle


enemyTypes = Enemy.__subclasses__()