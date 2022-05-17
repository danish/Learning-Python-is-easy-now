"""
Operator Overloading
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


a1 = A(100)
a2 = A(200)

x = a1 * 10
print(x)