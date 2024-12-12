import character
import tkinter

class player(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.position = [0,0]
        self.icon = "🏃"

    
    def getCurrontBiomeDisplay(self):
        return str(self.game.map.getBiomeAt(self.position[0], self.position[1]).getType())
