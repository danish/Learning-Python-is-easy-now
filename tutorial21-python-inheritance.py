"""class A():
    def __init__(self, a):
        self.a = a

    def display(self):
        print("in A class a =", self.a)    

class B(A):
    def __init__(self, a ,b ):
        self.b = b
        A.__init__(self, a)

    def display_b(self):
        print(" in class B a =", self.a)
        print(" in class B b =", self.b)

    def display(self):
        print("in B class a =", self.a)    


b1 = B(10, 20)
b1.display_b()
b1.display()
print(b1.a)

"""


"""
Types of Inheritecne 

"""
"""
Single inheritance

  A
  |
  B

"""

"""
Multilevel inheritance
    A
    |
    B
    |
    C
"""
"""class A():
    pass

class B( A ):
    pass

class C(B):
    pass
"""
"""

Multiple inheritance

A       B
|_______|
    |
    C

"""
class A():
    def __init__(self, a):
        self.a = a

class B():
    def __init__(self, b):
        self.b = b

class C(A, B):
    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, a)
        self.c = c  

    def display(self):
        print(" a =", self.a)
        print(" b =", self.b)
        print(" c =", self.c)          

c1 = C(10, 20, 30)
c1.display()


"""
Hierarchical inheritance
     A
  ___|___
 |       |
 B       C

"""

"""
Hybrid inheritance
     A
  ___|___
 |       |
 B       C
 |_______|
     |
     D   
"""