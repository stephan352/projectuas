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
        self.output = tkinter.StringVar()
        self.output.set("test")

        self.initRoot()

    def initPlayer(self):
        return player.player(self)
    
    def generateRawScreen(self):
        display_grid = self.map.getMap()
        player_position = self.player.getPosition()
        display_grid[player_position[1]][player_position[0]] = self.player
        # print("========display grid==========")
        # for row in display_grid:
        #     print(row)
        # print("==============================")
        return [[element.getIcon() for element in row] for row in display_grid]
    
    # def getTupleRowDisplay(self):  #generate tuple for tkinter display
    #     return [tuple([element.getIcon() for element in row]) for row in self.generateRawScreen()]
    
    def getCroppedScreenTuple(self):
        playerXposition = self.player.getPosition()[0]
        playerYposition = self.player.getPosition()[1]
        if playerXposition < 5:
            croppedX = [row[0:9] for row in self.generateRawScreen()]
        elif playerXposition > self.map.getMapDimensions()[0] - 5:
            croppedX = [row[self.map.getMapDimensions()[0] - 9:] for row in self.generateRawScreen()]
        else:
            croppedX = [row[playerXposition - 4:playerXposition + 5] for row in self.generateRawScreen()]
        
        if playerYposition < 5:
            cropped = croppedX[0:9]
        elif playerYposition > self.map.getMapDimensions()[1] - 5:
            cropped = croppedX[self.map.getMapDimensions()[1] - 9:]
        else:
            cropped = croppedX[playerYposition - 4:playerYposition + 5]
        
        return tuple(cropped)


        # if playerXposition < 5:
        #     if playerYposition < 5:
        #         croppedY = self.generateRawScreen()[0:8]
        #         screen = [row[0:9] for row in croppedY]
        #         return tuple(screen)
        #     elif playerYposition > self.map.getMapDimensions()[1] - 5:
        #         croppedY = self.generateRawScreen()[self.map.getMapDimensions()[1] - 8:]
        #         screen = [row[0:9] for row in croppedY]
        #         return tuple(screen)
        #     else:
        #         croppedY = self.generateRawScreen()[playerYposition - 4:playerYposition + 4]
        #         screen = [row[0:9] for row in croppedY]
        #         return tuple(screen)
        # elif playerXposition > self.map.getMapDimensions()[0] - 5:
        #     if playerYposition < 5:
        #         croppedY = self.generateRawScreen()[0:8]
        #         screen = [row[self.map.getMapDimensions()[0] - 8:] for row in croppedY]
        #         return tuple(screen)
        #     elif playerYposition > self.map.getMapDimensions()[1] - 5:
        #         croppedY = self.generateRawScreen()[self.map.getMapDimensions()[1] - 8:]
        #         screen = [row[self.map.getMapDimensions()[0] - 8:] for row in croppedY]
        #         return tuple(screen)
        #     else:
        #         croppedY = self.generateRawScreen()[playerYposition - 4:playerYposition + 4]
        #         screen = [row[self.map.getMapDimensions()[0] - 8:] for row in croppedY]
        #         return tuple(screen)
        # elif playerYposition < 5:
        #     croppedY = croppedY = self.generateRawScreen()[0:8]
        #     screen = [row[playerXposition - 4: playerXposition + 4] for row in croppedY]
        #     return tuple(screen)
        # elif playerYposition > self.map.getMapDimensions()[1] - 5:
        #     croppedY = self.generateRawScreen()[self.map.getMapDimensions()[1] - 8:]
        #     screen = [row[playerXposition - 4: playerXposition + 4] for row in croppedY]
        #     return tuple(screen)
        # else:
        #     croppedY = self.generateRawScreen()[playerYposition - 4:playerYposition + 4]
        #     screen = [row[playerXposition - 4:playerXposition + 4] for row in croppedY]
        #     return tuple(screen)
    
    def updateScreen(self):
        self.table.delete(*self.table.get_children())
        croppedScreen = self.getCroppedScreenTuple()
        for row in croppedScreen:
            self.table.insert(parent="", index=tkinter.END, values=row)
    
    def initRoot(self):
        mainframe = tkinter.Frame(root).grid(row=0, column=0)
        screenframe = tkinter.Frame(mainframe)
        screenframe.grid(row=0,column=0,columnspan=3)
        map_columns = tuple([str(i) for i in range(9)])
        self.table = tkinter.ttk.Treeview(screenframe, columns= map_columns, show="tree")

        self.table.column("#0", minwidth=0, width=0)
        self.table.pack()
        for column_element in map_columns:
            self.table.column(column_element, width=20)
        croppedScreen = self.getCroppedScreenTuple()
        for row in croppedScreen:
            self.table.insert(parent="", index=tkinter.END, values=row)
        
        tkinter.Label(mainframe, textvariable=self.output).grid(row=2, column=0, columnspan=3)
        tkinter.Button(mainframe, text="Left", command=self.onLeftClick).grid(row=4, column=0)
        tkinter.Button(mainframe, text="Right", command=self.onRightClick).grid(row=4, column=2)
        tkinter.Button(mainframe, text="Up", command=self.onUpClick).grid(row=3, column=1)
        tkinter.Button(mainframe, text="Down", command=self.onDownClick).grid(row=5, column=1)

        tkinter.Button(mainframe, text="test", command=lambda: self.setOutput("Hello World!")).grid(row=0, column=3)
    
    def onButtonClick(self):
        self.updateScreen()
    
    def setOutput(self, outputstring):
        self.output.set(outputstring)
    

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
