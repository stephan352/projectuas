class Item():
    def __init__(self, game):
        self.game = game

class Gear(Item):
    def __init__(self, game):
        super().__init__(game)

class Weapon(Item):
    def __init__(self, game):
        super().__init__(game)


class Kevlar(Gear):
    def __init__(self, game):
        super().__init__(game)
        self.armorgain = 1
        self.beingused = False
    
    def useEffect(self):
        self.game.player.armor += self.armorgain
        self.beingused = True

    def undoEffect(self):
        self.game.player.armor -= self.armorgain
        self.beingused = False

class Machete(Weapon):
    def __init__(self, game):
        super().__init__(game)
        self.damage = 20

weaponTypes = Weapon.__subclasses__()
gearTypes = Gear.__subclasses__()
