import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


circle = Circle(3)
print("Circle Area:", circle.area())         
# Output: Circle Area: 28.274333882308138
print("Circle Perimeter:", circle.perimeter()) 
# Output: Circle Perimeter: 18.84955592153876

rectangle = Rectangle(4, 8)
print("Rectangle Area:", rectangle.area())         
# Output: Rectangle Area: 32
print("Rectangle Perimeter:", rectangle.perimeter()) 
# Output: Rectangle Perimeter: 24