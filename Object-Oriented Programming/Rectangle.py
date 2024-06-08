class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        print("Area of Rectangle:", area)
    
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print("Perimeter of Rectangle:", perimeter)

# Example usage
rectangle = Rectangle(4, 6)
rectangle.area()       # Output: Area of Rectangle: 24
rectangle.perimeter()  # Output: Perimeter of Rectangle: 20