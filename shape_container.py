from rectangle import Rectangle
from square import Square
from circle import Circle
from shape import Shape
import random
import json


class ShapeContainer:
    @staticmethod
    def generate(num_of_shapes):
        instance_list = []
        count = 0
        for shape in range(num_of_shapes):
            random_num = random.randint(0, 2)
            if random_num == 0:
                instance_list.append(Circle(random.randint(1, 10)))
            elif random_num == 1:
                instance_list.append(Square(random.randint(1, 10)))
            elif random_num == 2:
                instance_list.append(Rectangle(random.randint(1, 10), random.randint(1, 10)))
            instance_list[count].color = generate_random_color()
            count += 1

        return instance_list

    @staticmethod
    def sum_perimeters(shapes_list):
        perimeter_sum = 0
        for shape in shapes_list:
            perimeter_sum += shape.perimeter()
        return perimeter_sum

    @staticmethod
    def sum_areas(shapes_list):
        areas_sum = 0
        for shape in shapes_list:
            areas_sum += shape.area()
        return areas_sum

    @staticmethod
    def count_colors(shapes_list):
        color_dict = {
            'blue': 0, 'red': 0, 'white': 0, 'black': 0, 'green': 0, 'orange': 0, 'pink': 0, 'purple': 0, 'yellow': 0,
            'gray': 0
        }
        for shape in shapes_list:
            color_dict[shape.color] = color_dict[shape.color] + 1
        return turn_dict_to_string(color_dict)


def turn_dict_to_string(dictionary):
    result = json.dumps(dictionary)

    # printing result as string
    return result


def generate_random_color():
    color_list = ['blue', 'red', 'white', 'black', 'green', 'orange', 'pink', 'purple', 'yellow', 'gray']
    return color_list[random.randint(0, 9)]
