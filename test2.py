class Animal():
    def __init__(self):
        pass

class Cat(Animal):
    def __init__(self):
        super().__init__()

x = Cat()
print(issubclass(x.__class__, Animal))