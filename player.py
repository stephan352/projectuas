import character
import tkinter

class player(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.position = [0,0]
        self.icon = "🏃"
        self.incombat = False
    
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
        opponent.recieveAttack(150)
