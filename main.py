# import biome
import tkinter.ttk
import player
import map
import tkinter


class Game():
    def __init__(self):
        self.map = map.Map(self)
        self.player = self.initPlayer()

        self.root = tkinter.Tk()
        self.screen = self.generateTkinterScreen()

        leftButton = tkinter.Button(self.root, text="Left", command= lambda: self.onLeftPress())
        leftButton.pack()

        self.root.mainloop()

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
    
    def generateTupleRowDisplay(self):
        result = [tuple([element.getIcon() for element in row]) for row in self.generateDisplayList()]
        return result #generate tuple for tkinter display
    
    def generateTkinterScreen(self):
        map_dimension = self.map.getMapDimensions()
        map_columns = tuple([str(i) for i in range(map_dimension[0])])
        table = tkinter.ttk.Treeview(self.root, columns= map_columns, show="tree")
        # table["show"] = "headings"
        table.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        table.column("#0", width=0, stretch=tkinter.NO)
        # table.heading("#0", minheight=0, height=0, stretch=tkinter.NO)
        for column_element in map_columns:
            table.column(column_element, width=20, stretch=tkinter.NO)
        
        tupleDisplayList = self.generateTupleRowDisplay()
        for row in tupleDisplayList:
            table.insert(parent="", index=tkinter.END, values=row)
        return table

    def updateScreen(self):
        self.screen.pack_forget()
        self.screen = self.generateTkinterScreen()
    
    def onButtonPress(self):
        self.updateScreen()

    def onLeftPress(self):
        self.player.goLeft()
        self.onButtonPress()



maingame = Game()
