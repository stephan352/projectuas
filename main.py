import biome
import player

class game():
    def __init__(self):
        self.map = self.generateMap(10, 10)
        self.player = self.initPlayer()
    
    def changeTile(self, a_grid, x, y, new_tile):
        a_grid[y][x] = new_tile
    

    def initPlayer(self):
        return player.player()

    def showGrid(self):
        display_grid = self.map.copy()
        player_position = self.player.getPosition()
        self.changeTile(display_grid, player_position[0], player_position[1], self.player)

        for row in display_grid:
            print(row)
    
    def setColumn(self, y, columnlist):
        i = 0
        for row in self.map:
            row[y] = columnlist[i]
            i += 1
    
    def generateMap(self, length, width):
        return [["" for i in range(length)] for j in range(width)]
        # return [[biome.biome() for i in range(10)] for j in range(10)]

maingrid = game()
maingrid.showGrid()

        