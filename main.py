from shape_container import ShapeContainer


def main():
    my_container = ShapeContainer()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())
    print("")
    print("")

    print("the list is \n " + str(my_container.sort_shapes_by_area()))


'''def sum_rectangular_shapes(shape_a, shape_b) -> (Shape, Shape):
    sum_perimeter = shape_a.perimtere() + shape_b.perimtere()
    sum_area = shape_a.area() + shape_b.area()

    sum_shape_color = shape_a.color


def solve_equation_by_perimeter_area(side1, side2, area, perimeter):
    pass'''

if __name__ == '__main__':
    main()
