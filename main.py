import tkinter.ttk
import player
import map
import tkinter


class Game():
    def __init__(self, root, sourceimages):
        self.sourceimages = sourceimages
        self.root = root
        self.initRoot()
 

    def initPlayer(self):
        return player.player(self)
    
    def generateRawScreen(self):
        display_grid = self.map.getMap()
        player_position = self.player.getPosition()
        display_grid[player_position[1]][player_position[0]] = self.player
        return display_grid
    
    def getCroppedScreen(self):
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
        
        return cropped
    
    def generateScreenTopLevel(self):
        self.screenwindow = tkinter.Toplevel()
        self.screenwindow.geometry("+%d+%d" % (self.gamewindow.winfo_x() + 350, self.gamewindow.winfo_y()))
        croppedScreen = self.getCroppedScreen()
        rowindex = 0
        for row in croppedScreen:
            columnindex = 0
            for element in row:
                photo = self.sourceimages[element.imagesrc]
                label = tkinter.Label(self.screenwindow, image=photo)
                label.grid(row=rowindex, column=columnindex)
                columnindex += 1
            rowindex += 1

    def updateScreen(self):
        self.screenwindow.destroy()
        self.generateScreenTopLevel()
        
    
    def initRoot(self):
        sizeoptions = ["small", "medium", "large"]
        self.selectedsize = tkinter.StringVar()
        self.selectedsize.set(sizeoptions[0])

        tkinter.Label(self.root, text="Size:").grid(row=0,column=0)
        tkinter.OptionMenu(self.root, self.selectedsize, *sizeoptions).grid(row=0,column=1)
        tkinter.Button(self.root, text="Start game!", command=self.startGame).grid(row=1,column=0)
    
    def startGame(self):
        self.enemies = []
        self.bottomrow = 25
        self.merchantHUD = False
        size = self.selectedsize.get()
        if size == "small":
            self.map = map.Map(self, 25, 25)
        elif size == "medium":
            self.map = map.Map(self, 50, 50)
        elif size == "large":
            self.map = map.Map(self, 100, 100)
        self.player = self.initPlayer()
        self.output = tkinter.StringVar()
        self.output.set("")

        self.targetfounditem = self.player.getCurrentBiome().getTargetItem()
        # self.playeritemindex = 0
        

        self.playerskills = self.player.skills.copy()
        for skill in self.playerskills:
            self.playerskills[skill].append(False)
        
        self.gamewindow = tkinter.Toplevel()
        self.gamewindow.geometry("+%d+%d" % (100, 200))


        
        self.generateScreenTopLevel()

        # screenframe = tkinter.Frame(self.gamewindow)
        # screenframe.grid(row=0,column=0,columnspan=3)
        # map_columns = tuple([str(i) for i in range(9)])
        # self.table = tkinter.ttk.Treeview(screenframe, columns= map_columns, show="tree")

        # self.table.column("#0", minwidth=0, width=0)
        # self.table.pack()
        # for column_element in map_columns:
        #     self.table.column(column_element, width=20)
        # croppedScreen = self.getCroppedScreenTuple()
        # for row in croppedScreen:
        #     self.table.insert(parent="", index=tkinter.END, values=row)
        
        tkinter.Label(self.gamewindow, textvariable=self.output).grid(row=2, column=0, columnspan=3)

        b1 = tkinter.Button(self.gamewindow, text="Left", command=self.onLeftClick)
        b2 = tkinter.Button(self.gamewindow, text="Right", command=self.onRightClick)
        b3 = tkinter.Button(self.gamewindow, text="Up", command=self.onUpClick)
        b4 = tkinter.Button(self.gamewindow, text="Down", command=self.onDownClick)

        b1.grid(row=4, column=0)
        b2.grid(row=4, column=2)
        b3.grid(row=3, column=1)
        b4.grid(row=5, column=1)

        self.playerhealth = tkinter.StringVar()
        self.playerbiome = tkinter.StringVar()
        self.playerenergy = tkinter.StringVar()
        self.playergold = tkinter.StringVar()
        self.attackcost = tkinter.StringVar()
        self.stunattackcost = tkinter.StringVar()

        self.combatoutput1 = tkinter.StringVar()
        self.combatoutput2 = tkinter.StringVar()

        self.enemiesleft = tkinter.StringVar()
        self.enemyhealth = tkinter.StringVar()

        self.itemsfound = tkinter.StringVar()

        self.inventorylen = tkinter.StringVar()
        self.inventoryitem = tkinter.StringVar()

        self.playerexp = tkinter.StringVar()
        self.playerlevel = tkinter.StringVar()

        self.playergear = tkinter.StringVar()

        self.enemiesremaining = tkinter.StringVar()

        tkinter.Label(self.gamewindow, textvariable=self.playerhealth).grid(row=6, column=0, columnspan=3)
        tkinter.Label(self.gamewindow, textvariable=self.playergear).grid(row=7, column=0, columnspan=3)
        tkinter.Label(self.gamewindow, textvariable=self.playerbiome).grid(row=8, column=0, columnspan=3)

        tkinter.Label(self.gamewindow, textvariable=self.combatoutput1).grid(row=1, column=4, columnspan=3)
        tkinter.Label(self.gamewindow, textvariable=self.combatoutput2).grid(row=2, column=4, columnspan=3)

        tkinter.Label(self.gamewindow, textvariable=self.enemiesleft).grid(row=3, column=4, columnspan=3)
        tkinter.Label(self.gamewindow, textvariable=self.enemyhealth).grid(row=4, column=4, columnspan=3)

        b5 = tkinter.Button(self.gamewindow, textvariable=self.attackcost, command=self.onAttackClick)
        b5.grid(row=5, column=4)
        
        b7 = tkinter.Button(self.gamewindow, textvariable=self.stunattackcost, command=self.onStunAttackClick)
        b7.grid(row=5, column=5)

        tkinter.Label(self.gamewindow, textvariable=self.playerenergy).grid(row=9, column=0, columnspan=3)
        tkinter.Label(self.gamewindow, textvariable=self.playergold).grid(row=10, column=0, columnspan=3)

        tkinter.Label(self.gamewindow, textvariable=self.itemsfound).grid(row=6, column=4, columnspan=3)
        b6 = tkinter.Button(self.gamewindow, text="take", command=self.onTakeClick)
        b6.grid(row=7, column=4, columnspan=3)

        tkinter.Label(self.gamewindow, textvariable=self.inventorylen).grid(row=8, column=4, columnspan=3)
        tkinter.Label(self.gamewindow, textvariable=self.inventoryitem).grid(row=9, column=4, columnspan=3)
        tkinter.Button(self.gamewindow, text=">", command=self.onNextPlayerItemClick).grid(row=10, column=5)
        tkinter.Button(self.gamewindow, text="use", command=self.onUseClick).grid(row=10, column=4, columnspan=3)
        tkinter.Button(self.gamewindow, text="drop", command=self.onDropClick).grid(row=11, column=4, columnspan=3)

        tkinter.Label(self.gamewindow, textvariable=self.playerexp).grid(row=11, column=0, columnspan=3)

        tkinter.Label(self.gamewindow, textvariable=self.playerlevel).grid(row=12, column=0, columnspan=3)

        tkinter.Label(self.gamewindow, textvariable=self.enemiesremaining).grid(row=13, column=0, columnspan=3)
        tkinter.Label(self.gamewindow, text="Defeat all enemies to win!").grid(row=14, column=0, columnspan=3)
        

        self.buttons = (b1, b2, b3, b4, b5, b6)
        

        self.update()
    
    def setOutput(self, outputstring):
        self.output.set(outputstring)
    
    def setCombatOutput1(self, outputstring):
        self.combatoutput1.set(outputstring)
    
    def setCombatOutput2(self, outputstring):
        self.combatoutput2.set(outputstring)
    
    def initiateCombat(self):
        self.player.incombat = True
    
    def onEnemyDeath(self):
        self.setOutput(self.targetenemy.__class__.__name__ + " is dead!")
        self.setCombatOutput2("-")
        self.player.getCurrentBiome().enemies.pop(0)
        self.enemies.remove(self.targetenemy)
        self.player.gainExp(20)
        if not self.player.getCurrentBiome().enemies:
            self.setOutput("Enemies cleared!")
            self.player.incombat = False
        self.update()
    
    def checkForEnemy(self):
        if self.player.getCurrentBiome().enemies:
            self.setOutput("Enemies here!")
            self.initiateCombat()
            if self.player.energy < 5:
                self.setOutput("You died! Game over")
                for button in self.buttons:
                    button.destroy()
                tkinter.Button(self.gamewindow, text="NEW GAME", command=self.startGame).grid(row=self.bottomrow, column=0, columnspan=3)

    def updateHUD(self):
        if self.player.inventory:
            self.targetplayeritem = self.player.inventory[0]
        else:
            self.targetplayeritem = None
        
        if self.player.getCurrentBiome().item:
            self.targetfounditem = self.player.getCurrentBiome().getTargetItem()
        else:
            self.targetfounditem = None

        self.playerhealth.set("Health: " + str(self.player.health))
        self.playergear.set("Armor: " + self.player.gear.__class__.__name__)

        self.attackcost.set("Attack! (" + str(self.player.attackcost) + ")")
        self.stunattackcost.set("Stun & attack! (" + str(self.player.attackcost*5) + ")")

        self.playerbiome.set("Biome: " + str(self.player.getCurrontBiomeDisplay()))
        self.playerenergy.set("Energy: " + str(self.player.energy))
        self.playergold.set("Gold: " + str(self.player.gold))

        self.itemsfound.set("Found " + str(self.targetfounditem.__class__.__name__))

        self.playerexp.set("Exp: " + str(self.player.exp))
        self.playerlevel.set("Level: " + str(self.player.level))

        self.inventorylen.set("==inventory (" + str(len(self.player.inventory)) + ")==")
        self.inventoryitem.set(str(self.targetplayeritem.__class__.__name__))

        self.enemiesremaining.set("Enemies left: " + str(len(self.enemies)))
        
        if self.merchantHUD:
            self.updateMerchantHUD()

        if self.player.getCurrentBiome().enemies:
            self.targetenemy = self.player.getCurrentBiome().enemies[0]
            self.enemiesleft.set("Enemiesleft: " + str(len(self.player.getCurrentBiome().enemies)))
            self.enemyhealth.set(self.targetenemy.__class__.__name__ + " health: " + str(self.targetenemy.health))
        else:
            self.enemiesleft.set("No enemies")
            self.enemyhealth.set("-")

            for skill in self.player.skills:
                if self.player.exp > self.player.skills[skill][2] and not self.playerskills[skill][3]:
                    currentskill = skill
                    skillbutton = tkinter.Button(self.gamewindow, text="Practice " + skill, command=lambda: self.onPracticeClick(currentskill))
                    self.playerskills[currentskill].append(skillbutton)
                    skillbutton.grid(row=self.bottomrow, column=0, columnspan=3)
                    self.playerskills[currentskill][3] = True
                    self.bottomrow += 1
    
    def update(self):
        if self.player.health <= 0:
            self.setOutput("You died! Game over")
            for button in self.buttons:
                button.destroy()
            tkinter.Button(self.gamewindow, text="NEW GAME", command=self.startGame).grid(row=self.bottomrow, column=0, columnspan=3)
        if not self.enemies:
            self.setOutput("You finished the game!")
            for button in self.buttons:
                button.destroy()
            tkinter.Button(self.gamewindow, text="NEW GAME", command=self.startGame).grid(row=self.bottomrow, column=0, columnspan=3)
        if not self.player.incombat:
            self.checkForEnemy()

            if self.player.getCurrentBiome().merchant and not self.player.incombat:
                if not self.merchantHUD:
                    self.generateMerchantHUD()
            elif self.merchantHUD:
                self.removeMerchantHUD()
                
        self.updateScreen()
        self.updateHUD()
    
    def generateMerchantHUD(self):
        self.merchantHUD = True
        merchant = self.player.getCurrentBiome().merchant
        youmetmerchant = tkinter.Label(self.gamewindow, text="You met a merchant!")
        youmetmerchant.grid(row=12, column=4, columnspan=3)

        if merchant.inventory:

            self.targetmerchantitem = merchant.inventory[0]
            self.displayedmerchantitem = tkinter.StringVar()
            self.displayedmerchantitem.set(merchant.inventory[0].__class__.__name__)
            merchantitemdisplay = tkinter.Label(self.gamewindow, textvariable=self.displayedmerchantitem)
            merchantitemdisplay.grid(row=13, column=4, columnspan=3)

            self.merchantsell = tkinter.StringVar()
            tradebutton = tkinter.Button(self.gamewindow, textvariable=self.merchantsell, command=self.onBuyClick)
            tradebutton.grid(row=14, column=5)
            nextmerchantitem = tkinter.Button(self.gamewindow, text=">", command=self.onNextMerchantItemClick)
            nextmerchantitem.grid(row=14, column=6)
            self.sellprice = tkinter.StringVar()
            sellbutton = tkinter.Button(self.gamewindow, textvariable=self.sellprice, command=self.onSellClick)
            sellbutton.grid(row=15, column=5)
        
            self.merchantHUD = (youmetmerchant, merchantitemdisplay, nextmerchantitem, tradebutton, sellbutton)
        else:
            self.displayedmerchantitem = tkinter.StringVar()
            self.displayedmerchantitem.set("-")

            merchantitemdisplay = tkinter.Label(self.gamewindow, textvariable=self.displayedmerchantitem)
            merchantitemdisplay.grid(row=13, column=4, columnspan=3)

            self.merchantsell = tkinter.StringVar()
            tradebutton = tkinter.Button(self.gamewindow, textvariable=self.merchantsell, command=self.onBuyClick)
            tradebutton.grid(row=14, column=5)
            nextmerchantitem = tkinter.Button(self.gamewindow, text=">", command=self.onNextMerchantItemClick)
            nextmerchantitem.grid(row=14, column=6)
            self.sellprice = tkinter.StringVar()
            sellbutton = tkinter.Button(self.gamewindow, textvariable=self.sellprice, command=self.onSellClick)
            sellbutton.grid(row=15, column=5)
        
            self.merchantHUD = (youmetmerchant, merchantitemdisplay, nextmerchantitem, tradebutton, sellbutton)

    def removeMerchantHUD(self):
        self.targetmerchantitem = None
        for widget in self.merchantHUD:
            widget.destroy()
        self.merchantHUD = False
    
    def updateMerchantHUD(self):
        merchant = self.player.getCurrentBiome().merchant
        if merchant.inventory:
            self.targetmerchantitem = merchant.inventory[0]
            self.displayedmerchantitem.set(self.targetmerchantitem.__class__.__name__)
            self.merchantsell.set("Buy (" + str(merchant.prices[self.targetmerchantitem]) + ")")
            self.sellprice.set("Sell current item (" + str(merchant.buyingprice) + ")")
        else:
            self.targetmerchantitem = None
            self.displayedmerchantitem.set("-")
            self.merchantsell.set("Buy (-)")
            self.sellprice.set("Sell current item (" + str(merchant.buyingprice) + ")")


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
    
    def onAttackClick(self):
        if self.player.getCurrentBiome().enemies:
            self.player.attack(self.targetenemy)
        self.update()
    
    def onUseClick(self):
        if self.player.inventory:
            if self.player.incombat:
                self.setOutput("Cannot use in combat!")
            else:
                self.player.use(self.targetplayeritem)
        self.update()
    
    def onPracticeClick(self, skill):
        self.player.practiceSkill(skill)
        self.update()
    
    def onStunAttackClick(self):
        if self.player.getCurrentBiome().enemies:
            self.player.stunAttack(self.targetenemy)
        self.setCombatOutput2("-")
        self.update()
    
    def onTakeClick(self):
        if self.player.getCurrentBiome().item:
            if self.player.incombat:
                self.setOutput("Cannot take in combat!")
            else:
                self.player.take(self.targetfounditem)
        self.update()
    
    def onNextPlayerItemClick(self):
        if self.player.inventory:
            lastitem = self.player.inventory.pop(0)
            self.player.inventory.append(lastitem)
        self.update()
    
    def onDropClick(self):
        if self.player.inventory:
            self.player.drop(self.targetplayeritem)
        self.update()

    def onNextMerchantItemClick(self):
        merchant = self.player.getCurrentBiome().merchant
        if merchant.inventory:
            lastitem = merchant.inventory.pop(0)
            merchant.inventory.append(lastitem)
        self.update()
    
    def onBuyClick(self):
        merchant = self.player.getCurrentBiome().merchant
        if merchant.inventory:
            price = merchant.prices[self.targetmerchantitem]
            self.player.gold -= price
            self.player.inventory.append(self.targetmerchantitem)
            merchant.lose(self.targetmerchantitem)
        self.update()
    
    def onSellClick(self):
        if self.player.inventory:
            merchant = self.player.getCurrentBiome().merchant
            merchant.gain(self.targetplayeritem, merchant.buyingprice*2)
            if self.targetplayeritem in self.player.inventory:
                self.player.inventory.remove(self.targetplayeritem)
            self.player.gold += merchant.buyingprice

        self.update()
    


root = tkinter.Tk()

image_boy = tkinter.PhotoImage(file="boy.png")
image_meadow = tkinter.PhotoImage(file="meadow.png")

images = {"meadow.png": image_meadow, "boy.png": image_boy}

maingame = Game(root, images)
root.mainloop()
