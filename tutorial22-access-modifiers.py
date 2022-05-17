"""
Access Modifiers in Python

Public:
Attributes are always public and can be accessed using the dot (.) within the class and outside the class using its object

Protected:
Protected method are created by using prefix _ (single underscore)

Private:
Private members are created by using prefix __ (double underscore) and can not be accessed directly via its object.

"""
"""

class A():
    def __init__(self, a):
        self.a = a

    def display(self):
        print('a in class A=', self.a)

class B(A):
    def __init__(self, a, b):
        A.__init__( self, a)
        self.b = b

    def display_b(self):
        print('a in class B=', self.a)

a1 = A(10)

a1.display()
print(a1.a)

b1 = B(10, 20)
b1.display_b()
print(b1.a)"""

#protected Members
"""
class A():
    def __init__(self, a):
        self._a = a

    def display(self):
        print('a in class A=', self._a)

class B(A):
    def __init__(self, a, b):
        A.__init__( self, a)
        self.b = b

    def display_b(self):
        print('a in class B=', self._a)

a1 = A(10)

a1.display()
print(a1._a)

b1 = B(10, 20)
b1.display_b()
print(b1._a)
"""

#private members

class A():
    def __init__(self, a):
        self.__a = a

    def display(self):
        print('a in class A=', self.__a)

class B(A):
    def __init__(self, a, b):
        A.__init__( self, a)
        self.b = b

    def display_b(self):
        print('a in class B=', self._a)

a1 = A(10)

a1.display()
print(a1._A__a)

b1 =  B(100, 200)

print(b1._A__a)