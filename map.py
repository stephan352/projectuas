class Map():
    def __init__(self):
        self.map = self.generateMap(10, 10)
    
    def setColumn(self, y, columnlist):
        i = 0
        for row in self.map:
            row[y] = columnlist[i]
            i += 1
    
    def getMap(self):
        grid_to_copy = [row.copy() for row in self.map]
        return grid_to_copy

    def generateMap(self, length, width):
        return [["" for i in range(length)] for j in range(width)]
        # return [[biome.biome() for i in range(10)] for j in range(10)]
    
    def displayMap(self):
        print("=============Map==============")
        for row in self.map:
            print(row)
        print("==============================")