from shape_container import ShapeContainer
from help_tools import HelpTools
from shape import Shape
import random
from rectangle import Rectangle


def main():
    HelpTools.delete_log_dialog()
    my_container = ShapeContainer()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())
    print("")
    print("")

    print("the list is \n " + str(my_container.sort_shapes_by_area()))


def sum_square_rectangle(shape_1, shape_2) -> (Shape, Shape):
    sum_shape = shape_1.area() + shape_2.area()
    side_a = random.randint(1, 10)
    side_b = sum_shape / side_a
    return Rectangle(side_a, side_b)


if __name__ == '__main__':
    main()
