class Food():
    def __init__(self):
        self.regenerate = 50

class Banana(Food):
    nativeTo = "Jungle"
    def __init__(self):
        super().__init__()

class Cactus(Food):
    nativeTo = "Desert"
    def __init__(self):
        super().__init__()

class Apple(Food):
    nativeTo = "Meadow"
    def __init__(self):
        super().__init__()

class Berries(Food):
    nativeTo = "Meadow"
    def __init__(self):
        super().__init__()

class Salmon(Food):
    nativeTo = "Tundra"
    def __init__(self):
        super().__init__()

foodtypes = Food.__subclasses__()
