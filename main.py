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
        # print("========display grid==========")
        # for row in display_grid:
        #     print(row)
        # print("==============================")
        return display_grid
    
    def getTupleRowDisplay(self):  #generate tuple for tkinter display
        return [tuple([element.getIcon() for element in row]) for row in self.generateDisplayList()]
    
    def updateScreen(self, table):
        table.delete(*table.get_children())
        for row in self.getTupleRowDisplay():
            table.insert(parent="", index=tkinter.END, values=row)


# def insertToTable(table, listOfTuples):
#     for row in listOfTuples:
#         table.insert(parent="", index=tkinter.END, values=row)

maingame = Game()

root = tkinter.Tk()
# child = tkinter.Toplevel(root)

screenframe = tkinter.Frame(root)
screenframe.grid(row=0,column=0,columnspan=3)
screenscroll = tkinter.Scrollbar(screenframe)
screenscroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
map_dimension = maingame.map.getMapDimensions()
map_columns = tuple([str(i) for i in range(map_dimension[0])])
table = tkinter.ttk.Treeview(screenframe, columns= map_columns, show="tree", yscrollcommand=screenscroll.set)
screenscroll.config(command=table.yview)
# table.pack(expand=tkinter.YES, fill=tkinter.BOTH)
table.column("#0", minwidth=0, width=0)
table.pack()
for column_element in map_columns:
    table.column(column_element, width=20)
for row in maingame.getTupleRowDisplay():
    table.insert(parent="", index=tkinter.END, values=row)


def onLeftClick(table, game):
    game.player.goLeft()
    game.updateScreen(table)
leftButton = tkinter.Button(root, text="Left", command=lambda: onLeftClick(table,maingame)).grid(row=2, column=0)

def onRightCLick(table, game):
    game.player.goRight()
    game.updateScreen(table)
rightButton = tkinter.Button(root, text="Right", command=lambda: onRightCLick(table,maingame)).grid(row=2, column=2)

def onUpClick(table, game):
    game.player.goUp()
    game.updateScreen(table)
upButton = tkinter.Button(root, text="Up", command=lambda: onUpClick(table,maingame)).grid(row=1, column=1)

def onDownClick(table, game):
    game.player.goDown()
    game.updateScreen(table)
downButton = tkinter.Button(root, text="Down", command=lambda: onDownClick(table,maingame)).grid(row=3, column=1)

# leftButton.pack()

# root.bind("a", lambda:onAPress(table, maingame))

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
