# import biome
import tkinter.ttk
import player
import map
import tkinter


class Game():
    def __init__(self, root):
        self.root = root
        self.initRoot()
 

    def initPlayer(self):
        return player.player(self)
    
    def generateRawScreen(self):
        display_grid = self.map.getMap()
        player_position = self.player.getPosition()
        display_grid[player_position[1]][player_position[0]] = self.player
        return [[element.getIcon() for element in row] for row in display_grid]
    
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
    
    def updateScreen(self):
        self.table.delete(*self.table.get_children())
        croppedScreen = self.getCroppedScreenTuple()
        for row in croppedScreen:
            self.table.insert(parent="", index=tkinter.END, values=row)
        
    
    def initRoot(self):
        sizeoptions = ["small", "medium", "large"]
        self.selectedsize = tkinter.StringVar()
        self.selectedsize.set(sizeoptions[0])

        tkinter.Label(self.root, text="Size:").grid(row=0,column=0)
        tkinter.OptionMenu(self.root, self.selectedsize, *sizeoptions).grid(row=0,column=1)
        tkinter.Button(self.root, text="Start game!", command=self.startGame).grid(row=1,column=0)
    
    def startGame(self):
        self.enemies = []
        size = self.selectedsize.get()
        if size == "small":
            self.map = map.Map(self, 20, 50)
        elif size == "medium":
            self.map = map.Map(self, 50, 50)
        elif size == "large":
            self.map = map.Map(self, 100, 100)
        print("Map dimensions: ", self.map.getMapDimensions())
        self.player = self.initPlayer()
        self.output = tkinter.StringVar()
        self.output.set("")
        
        gamewindow = tkinter.Toplevel()
        screenframe = tkinter.Frame(gamewindow)
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
        
        tkinter.Label(gamewindow, textvariable=self.output).grid(row=2, column=0, columnspan=3)

        tkinter.Button(gamewindow, text="Left", command=self.onLeftClick).grid(row=4, column=0)
        tkinter.Button(gamewindow, text="Right", command=self.onRightClick).grid(row=4, column=2)
        tkinter.Button(gamewindow, text="Up", command=self.onUpClick).grid(row=3, column=1)
        tkinter.Button(gamewindow, text="Down", command=self.onDownClick).grid(row=5, column=1)

        self.playerhealth = tkinter.StringVar()
        self.playerbiome = tkinter.StringVar()
        self.updateHUD()

        tkinter.Label(gamewindow, textvariable=self.playerhealth).grid(row=6, column=0, columnspan=3)
        tkinter.Label(gamewindow, textvariable=self.playerbiome).grid(row=7, column=0, columnspan=3)
    
    def updateHUD(self):
        self.playerhealth.set("Player health: " + str(self.player.health))
        self.playerbiome.set("Player biome: " + str(self.player.getCurrontBiomeDisplay()))
    
    def update(self):
        print(self.map.getBiomeAt(self.player.getPosition()[0], self.player.getPosition()[1]).enemies)
        self.updateScreen()
        self.updateHUD()
    
    def setOutput(self, outputstring):
        self.output.set(outputstring)
    

    def onLeftClick(self):
        self.player.goLeft()
        self.update()
    
    def onRightClick(self):
        self.player.goRight()
        self.update()
    
    def onUpClick(self):
        self.player.goUp()
        self.update()
    
    def onDownClick(self):
        self.player.goDown()
        self.update()

root = tkinter.Tk()
maingame = Game(root)
root.mainloop()
