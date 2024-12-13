import character
import tkinter

class player(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.position = [0,0]
        self.icon = "🏃"
        self.incombat = False

        self.damage = 150
        self.energy = 1000
        self.attackcost = 20
    
    def goToPosition(self, x, y):
        if self.incombat:
            self.game.setOutput("Defeat the enemy first!")
        else:
            map_dimensionX = self.game.map.getMapDimensions()[0]
            map_dimensionY = self.game.map.getMapDimensions()[1]
            if 0 <= x < map_dimensionX and 0 <= y < map_dimensionY:
                self.position = [x, y]
            else:
                print("Out of boundaries!")
    
    def getCurrentBiome(self):
        return self.game.map.getBiomeAt(self.position[0], self.position[1])
    
    def getCurrontBiomeDisplay(self):
        return str(self.getCurrentBiome().getType())
    
    def attack(self, opponent):
        self.game.setCombatOutput1("Attacked enemy for " + str(self.damage))
        self.energy -= self.attackcost
        opponent.recieveAttack(self.damage)
    
    def eat(self, food):
        self.health += food.regenerate
        self.game.setOutput(food.__class__.__name__ + " eaten!")
