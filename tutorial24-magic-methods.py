"""
Magic Methods
"""
class A():
    def __init__(self, a):
        self.x = a

    def __add__(self, obj):
        print("Add funtion")
        return self.x + obj.x

    def __mul__(self, n):
        print("mul funtion")
        return self.x * n

    def __str__(self):
        return str(self.x)

a1 = A(100)     
print(a1)


