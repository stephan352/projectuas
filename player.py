import character

class player(character.Character):
    def __init__(self, game):
        super().__init__(game)
        self.position = [0,0]
        self.icon = "🏃"
