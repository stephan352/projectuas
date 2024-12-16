import character

class player(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.position = [0,0]
        self.icon = "🏃"
        self.incombat = False

        self.damage = 20
        self.energy = 1000
        self.attackcost = 20

        self.exp = 0
        self.level = 1

        self.skills = {"BetterAttack": [False, self.practiceBetterAttack, 100], "BetterHealth":[False, self.practiceBetterHealth, 200]}
    
    def goToPosition(self, x, y):
        if self.incombat:
            self.game.setOutput("Defeat the enemy first!")
        else:
            map_dimensionX = self.game.map.getMapDimensions()[0]
            map_dimensionY = self.game.map.getMapDimensions()[1]
            if 0 <= x < map_dimensionX and 0 <= y < map_dimensionY:
                self.position = [x, y]
            else:
                self.game.setOutput("Map limit reached!")
    
    def getCurrentBiome(self):
        return self.game.map.getBiomeAt(self.position[0], self.position[1])
    
    def getCurrontBiomeDisplay(self):
        return str(self.getCurrentBiome().getType())
    
    def attack(self, opponent):
        self.game.setCombatOutput1("Attacked enemy for " + str(self.damage))
        self.energy -= self.attackcost
        opponent.recieveAttack(self.damage)
    
    def eat(self, food):
        self.health += food.regenerate
        self.game.setOutput(food.__class__.__name__ + " eaten!")
    
    def practiceSkill(self, skill):
        print(skill + ": " + str(self.skills[skill]))
        if self.incombat:
            self.game.setOutput("Cannot train with enemy!")
        elif skill in self.skills:
            if self.skills[skill][0]:
                self.game.setOutput("Already have skill!")
            elif self.exp < self.skills[skill][2]:
                print(self.skills[skill][2])
                self.game.setOutput("Not enough exp!")
            else:
                self.skills[skill][1]()
        else:
            self.game.setOutput("Cannot train skill!")
    
    def practiceBetterHealth(self):
        if self.energy < 100:
            self.game.setOutput("Not enough energy!")
        else:
            self.energy -= 100
            self.health += 30
            self.skills["BetterHealth"][0] = True
            self.game.setOutput("Health skill practiced!")
            self.game.playerskills["BetterHealth"][-1].destroy()
            self.gainExp(30)

    
    def practiceBetterAttack(self):
        if self.energy < 80:
            self.game.setOutput("Not enough energy!")
        else:
            self.energy -= 80
            self.damage += 2
            self.skills["BetterAttack"][0] = True
            self.game.setOutput("Attack skill practiced!")
            self.game.playerskills["BetterAttack"][-1].destroy()
            self.gainExp(20)
    
    def gainExp(self, exp):
        self.exp += exp*self.level
        self.updateLevel()

    def updateLevel(self):
        levellimit = (1, 50, 200, 400, 600)
        i = 1
        for limit in levellimit:
            if self.exp > limit:
                self.level = i
            i += 1
