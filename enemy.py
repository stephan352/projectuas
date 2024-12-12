import character
import random

class Enemy(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.dodge = 10
        self.damage = 5
    
    def counterAttack(self, player):
        player.recieveAttack(self.damage)
    
    def recieveAttack(self, damage):
        if random.randint(0, 100) <= self.dodge:
            self.game.setCombatOutput1(self.__class__.__name__ + " dodged!")
            self.counterAttack(self.game.player)
            self.game.setCombatOutput2(self.__class__.__name__ + " attacked for " + str(self.damage))
        else:
            self.health -= damage
        if self.health <= 0:
            self.isAlive = False
            self.game.onEnemyDeath()
    
    
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