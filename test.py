class car():
    pass

childrenlist = car.__subclasses__()

class lambo(car):
    pass

class honda(car):
    def test(self):
        print("Hello world!")

class toyota(car):
    pass



print(childrenlist)
# childrenlist[1]().test()

def testFunction():
    print("A second Hello World")