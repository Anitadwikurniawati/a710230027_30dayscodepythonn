class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass  

    def perimeter(self):
        pass  

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

rectangle = Rectangle("Red", 4, 5)
circle = Circle("Blue", 3)

print(f"Rectangle - Color: {rectangle.color}, Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")

print(f"Circle - Color: {circle.color}, Area: {circle.area()}, Perimeter: {circle.perimeter()}")

