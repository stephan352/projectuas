import character
import random

class Enemy(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.dodge = 15
        self.damage = 4

        self.stunned = False
    
    def counterAttack(self, player):
        player.recieveAttack(self.damage)
        self.game.setCombatOutput2(self.__class__.__name__ + " attacked for " + str(self.damage))
    
    def recieveAttack(self, damage):
        if self.stunned:
            self.health -= damage
            self.stunned = False
        elif random.randint(0, 100) <= self.dodge:
            self.game.setCombatOutput1(self.__class__.__name__ + " dodged!")
            self.counterAttack(self.game.player)
        else:
            self.health -= damage
            self.counterAttack(self.game.player)
        if self.health <= 0:
            self.isAlive = False
            self.game.onEnemyDeath()
    
    
class GiantScorpion(Enemy):
    nativeTo = "Desert"
    def __init__(self, game):
        super().__init__(game)

class Gorilla(Enemy):
    nativeTo = "Jungle"
    def __init__(self, game):
        super().__init__(game)

class Crodocile(Enemy):
    nativeTo = "Jungle"
    def __init__(self, game):
        super().__init__(game)

class AngryCamel(Enemy):
    nativeTo = "Desert"
    def __init__(self, game):
        super().__init__(game)

class Wolf(Enemy):
    nativeTo = "Meadow"
    def __init__(self, game):
        super().__init__(game)

class Leopard(Enemy):
    nativeTo = "Meadow"
    def __init__(self, game):
        super().__init__(game)

class PolarBear(Enemy):
    nativeTo = "Tundra"
    def __init__(self, game):
        super().__init__(game)


enemyTypes = Enemy.__subclasses__()