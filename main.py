

class grid():
    def __init__(self):
        self.grid = [["" for i in range(10)] for j in range(10)]


    def showGrid(self):
        for row in self.grid:
            print(row)
    
    def setColumn(self, y, columnlist):
        i = 0
        for row in self.grid:
            row[y] = columnlist[i]
            i += 1

x = grid()
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Julia"]
x.setColumn(2, names)
x.showGrid()