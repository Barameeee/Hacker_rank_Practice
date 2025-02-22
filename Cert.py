import math

'''
class Rectangular:
    def area_(self,lenght,sides):
        area = lenght*sides
        return area
class Circle:
    def area_(self,lenght):
        area = 3.14*(lenght**2)
        return area
'''
'''
class Rectangle:
    def __init__(self, lenght, side):
        self.lenght = lenght
        self.side = side
        self.area = lenght*side

class Circle:
    def __init__(self, radiant):
        self.radiant = radiant
        return 3.14*((self.radiant)**2)
'''


class Rectangle:
    def __init__ (self,length,side):
        self.length = length
        self.side = side
    def area(self):
        return self.length*self.side
    
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return 3.14*(self.r**2)

p1 = Rectangle(2,3)

print(p1.area())

p2 = Circle(2)
print(p2.area())

print(math.pi)