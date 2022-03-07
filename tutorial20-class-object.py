"""class Person:
    def display( self ):
        print("This is display function")

    def add( self, x, y ):
        s = x + y
        print("Sum=", s)

p1 = Person()
p1.display()
p1.add(10, 20)
"""

class Person:
    #constructor
    def __init__( self , a, n ):
        self.age = a
        self.name = n
        print("This is from init")

    def display( self ):
        print("You age is ", self.age)
        print("You name is ", self.name)

    def add( self, x, y ):
        s = x + y
        print("Sum=", s)

p1 = Person(30, 'Jon')
p1.display()
#p1.add(10, 20)

p2 = Person(35, 'Ron')
p2.display()
print(p2.age)

class Item:
    pass