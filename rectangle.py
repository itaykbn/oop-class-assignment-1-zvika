from shape import Shape


class Rectangle(Shape):

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        # self.color = color

    def perimeter(self):
        return 2 * (self.side_b + self.side_a)

    def area(self):
        return self.side_a * self.side_b
