from shape_container import ShapeContainer
from help_tools import HelpTools
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


# need to add the solution to the end of the first part(don't understand what do i need to do)
if __name__ == '__main__':
    main()
