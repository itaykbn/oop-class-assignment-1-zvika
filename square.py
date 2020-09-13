from shape import Shape


class Square(Shape):

    def __init__(self, side):
        self.side = side
        # self.color = color

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ^ 2
