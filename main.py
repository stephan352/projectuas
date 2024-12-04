import biome
import player
import map
    

class Game():
    def __init__(self):
        self.map = map.Map()
        self.player = self.initPlayer()

    def initPlayer(self):
        return player.player()
    
    def display(self):
        display_grid = self.map.getMap()
        player_position = self.player.getPosition()
        display_grid[player_position[1]][player_position[0]] = self.player
        print("========display grid==========")
        for row in display_grid:
            print(row)
        print("==============================")


maingame = Game()
maingame.display()

maingame.player.goUp()
maingame.player.goUp()
maingame.player.goUp()
maingame.player.goUp()
maingame.player.goUp()
maingame.player.goLeft()
maingame.player.goLeft()
maingame.player.goLeft()

maingame.display()
