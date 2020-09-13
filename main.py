from rectangle import Rectangle
from square import Square
from circle import Circle
from shape import Shape
from shape_container import ShapeContainer

import math


def main():
    rect = Rectangle(10, 10)
    square = Square(2)
    circle = Circle(5)
    sc = ShapeContainer

    my_container = ShapeContainer()
    shapes = my_container.generate(100)
    print("total area:", my_container.sum_areas(shapes))
    print("total perimeter:", my_container.sum_perimeters(shapes))
    print("colors:", my_container.count_colors(shapes))


'''def sum_rectangular_shapes(shape_a, shape_b) -> (Shape, Shape):
    sum_perimeter = shape_a.perimtere() + shape_b.perimtere()
    sum_area = shape_a.area() + shape_b.area()

    sum_shape_color = shape_a.color


def solve_equation_by_perimeter_area(side1, side2, area, perimeter):
    pass'''


if __name__ == '__main__':
    main()
