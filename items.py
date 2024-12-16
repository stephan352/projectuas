class Item():
    def __init__(self, game):
        self.game = game

        # self.price = 0

class Gear(Item):
    def __init__(self, game):
        super().__init__(game)
        self.beingused = False

    def useEffect(self):
        self.game.player.armor += self.armorgain
        self.beingused = True

    def undoEffect(self):
        self.game.player.armor -= self.armorgain
        self.beingused = False

class Weapon(Item):
    def __init__(self, game):
        super().__init__(game)


class Kevlar(Gear):
    def __init__(self, game):
        super().__init__(game)
        self.armorgain = 1

class Machete(Weapon):
    def __init__(self, game):
        super().__init__(game)
        self.damage = 20

class KitchenKnife(Weapon):
    def __init__(self, game):
        super().__init__(game)
        self.damage = 15

weaponTypes = Weapon.__subclasses__()
gearTypes = Gear.__subclasses__()
