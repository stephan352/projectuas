import character
import items
import food

class player(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.position = [0,0]
        self.icon = "🏃"
        self.incombat = False

        self.inventory = []
        self.weapon = None
        self.gear = None

        self.basedamage = 6
        self.damage = self.basedamage
        self.energy = 1000
        self.gold = 1000
        self.attackcost = 5

        self.armor = 0

        self.exp = 0
        self.level = 1
        # ini skills kyknya butuh OOP
        self.skills = {"BetterAttack": [False, self.practiceBetterAttack, 100], "BetterHealth":[False, self.practiceBetterHealth, 200]}
    

    def use(self, item):
        if issubclass(item.__class__, items.Weapon):
            if self.weapon:
                self.unequipWeapon()
            self.weapon = item
            self.damage = item.damage
            self.game.setOutput("Used " + str(item.__class__.__name__))
        elif issubclass(item.__class__, items.Gear):
            if self.gear:
                self.unequipGear()
            self.gear = item
            item.useEffect()
            self.game.setOutput("Used " + str(item.__class__.__name__))
        elif issubclass(item.__class__, food.Food):
            self.eat(item)
        
        if item in self.inventory:
                self.inventory.remove(item)
    
    def take(self, item):
        self.inventory.append(item)
        self.getCurrentBiome().removeItem(item)
        self.game.setOutput(str(item.__class__.__name__) + " Taken!")
    
    def drop(self, item):
        if item in self.inventory:
            self.getCurrentBiome().item.append(item)
            self.inventory.remove(item)
    
    def unequipWeapon(self):
        self.inventory.append(self.weapon)
        self.game.setOutput("Unequipped " + str(self.weapon.__class__.__name__))
        self.weapon = None
        self.damage = self.basedamage
    
    def unequipGear(self):
        self.gear.undoEffect()
        self.inventory.append(self.gear)
        self.game.setOutput("Unequipped " + str(self.gear.__class__.__name__))
        self.gear = None
    
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
    
    
    
    def getCurrontBiomeDisplay(self):
        return str(self.getCurrentBiome().getType())
    
    def stun(self, opponent):
        opponent.stunned = True
    
    def stunAttack(self, opponent):
        self.game.setCombatOutput1("Stunned & attacked enemy for " + str(self.damage))
        self.energy -= self.attackcost*5
        self.stun(opponent)
        opponent.recieveAttack(self.damage)
    
    def attack(self, opponent):
        self.game.setCombatOutput1("Attacked enemy for " + str(self.damage))
        self.energy -= self.attackcost
        opponent.recieveAttack(self.damage)
    
    def recieveAttack(self, damage):
        self.health -= damage - self.armor
        if self.health <= 0:
            self.isAlive = False
    
    def eat(self, food):
        food.useEffect()
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
