# import biome
import tkinter.ttk
import player
import map
import tkinter
    

class Game():
    def __init__(self):
        self.map = map.Map(self)
        self.player = self.initPlayer()

    def initPlayer(self):
        return player.player(self)
    
    def generateDisplayList(self):
        display_grid = self.map.getMap()
        player_position = self.player.getPosition()
        display_grid[player_position[1]][player_position[0]] = self.player
        print("========display grid==========")
        for row in display_grid:
            print(row)
        print("==============================")
        return display_grid
    
    # def displayToTerminal(self):
    #     display_grid = self.generateDisplayList()
    #     print("========display grid==========")
    #     for row in display_grid:
    #         print(row)
    #     print("==============================")
    
    def getTupleRowDisplay(self):
        result = [tuple([element.getIcon() for element in row]) for row in self.generateDisplayList()]
        return result #generate tuple for tkinter display
    
    # def getTkinterDisplayString(self):
    #     display_grid = self.map.getMap()
    #     player_position = self.player.getPosition()
    #     display_grid[player_position[1]][player_position[0]] = self.player
    #     output_string = ""

    #     for row in display_grid:
    #         for element in row:
    #             output_string += element.getIcon()
    #         output_string += "\n"
    #     return output_string
    
    # def displayToTkinter(self, root):
    #     game_display = tkinter.Text(root)
    #     game_display.pack()
    #     game_display.insert(tkinter.END, self.getTkinterDisplayString())



maingame = Game()

root = tkinter.Tk()

map_dimension = maingame.map.getMapDimensions()
map_columns = tuple([str(i) for i in range(map_dimension[0])])
table = tkinter.ttk.Treeview(root, columns= map_columns)
table.pack(expand=tkinter.YES, fill=tkinter.BOTH)
table.column("#0", minwidth=0, width=0, stretch=tkinter.NO)
for column_element in map_columns:
    table.column(column_element, width=20, stretch=tkinter.NO)

tupleDisplayList = maingame.getTupleRowDisplay()
for row in tupleDisplayList:
    table.insert(parent="", index=tkinter.END, values=row)

# game_display = tkinter.Text(root)
# game_display.pack()
# game_display.insert(tkinter.END, maingame.getTkinterDisplayString())

root.mainloop()

# maingame.display()

# maingame.player.goUp()
# maingame.player.goUp()
# maingame.player.goUp()
# maingame.player.goUp()
# maingame.player.goUp()
# maingame.player.goLeft()
# maingame.player.goLeft()
# maingame.player.goLeft()

# maingame.display()


# TO-DO LIST:
# display as emoji
# create enemy