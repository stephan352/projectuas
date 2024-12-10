# import biome
import tkinter.ttk
import player
import map
import tkinter


class Game():
    def __init__(self, root):
        self.root = root
        self.map = map.Map(self)
        self.player = self.initPlayer()

        self.initRoot()

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
    
    def updateScreen(self):
        self.table.delete(*self.table.get_children())
        for row in self.getTupleRowDisplay():
            self.table.insert(parent="", index=tkinter.END, values=row)
    
    def initRoot(self):
        screenframe = tkinter.Frame(root)
        screenframe.grid(row=0,column=0,columnspan=3)
        screenscroll = tkinter.Scrollbar(screenframe)
        screenscroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        map_dimension = self.map.getMapDimensions()
        map_columns = tuple([str(i) for i in range(map_dimension[0])])
        self.table = tkinter.ttk.Treeview(screenframe, columns= map_columns, show="tree", yscrollcommand=screenscroll.set)
        screenscroll.config(command=self.table.yview)
        self.table.column("#0", minwidth=0, width=0)
        self.table.pack()
        for column_element in map_columns:
            self.table.column(column_element, width=20)
        for row in self.getTupleRowDisplay():
            self.table.insert(parent="", index=tkinter.END, values=row)
        
        tkinter.Button(root, text="Left", command=self.onLeftClick).grid(row=2, column=0)
        tkinter.Button(root, text="Right", command=self.onRightClick).grid(row=2, column=2)
        tkinter.Button(root, text="Up", command=self.onUpClick).grid(row=1, column=1)
        tkinter.Button(root, text="Down", command=self.onDownClick).grid(row=3, column=1)
    
    def onButtonClick(self):
        self.updateScreen()
    

    def onLeftClick(self):
        self.player.goLeft()
        self.onButtonClick()
    
    def onRightClick(self):
        self.player.goRight()
        self.onButtonClick()
    
    def onUpClick(self):
        self.player.goUp()
        self.onButtonClick()
    
    def onDownClick(self):
        self.player.goDown()
        self.onButtonClick()

root = tkinter.Tk()
maingame = Game(root)
root.mainloop()
