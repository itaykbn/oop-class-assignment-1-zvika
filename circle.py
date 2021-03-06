from shape import Shape
import math


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius * self.radius)
