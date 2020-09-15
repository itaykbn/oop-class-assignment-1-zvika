from rectangle import Rectangle
from square import Square
from circle import Circle
import random
from help_tools import HelpTools


class ShapeContainer:
    @property
    def shapes_list(self):
        return self._shapes_list

    @shapes_list.setter
    def shapes_list(self, value):
        self._shapes_list = value

    def generate(self, num_of_shapes):
        instance_list = []
        for index in range(num_of_shapes):
            random_num = random.randint(0, 2)
            shape = self.get_random_instance(random_num)
            instance_list.append(shape)
            instance_list[index].color = HelpTools.generate_random_color()

        self._shapes_list = instance_list

    @staticmethod
    def get_random_instance(random_num):
        if random_num == 0:
            return Circle(random.randint(1, 10))
        elif random_num == 1:
            return Square(random.randint(1, 10))
        elif random_num == 2:
            return Rectangle(random.randint(1, 10), random.randint(1, 10))
        return None

    def sum_perimeters(self):
        perimeter_sum = 0
        for shape in self._shapes_list:
            perimeter_sum += shape.perimeter()
        return perimeter_sum

    def sum_areas(self):
        areas_sum = 0
        for shape in self._shapes_list:
            areas_sum += shape.area()
        return areas_sum

    def count_colors(self):
        color_dict = {'blue': 0, 'red': 0, 'white': 0, 'black': 0, 'green': 0, 'orange': 0, 'pink': 0, 'purple': 0,
                      'yellow': 0, 'gray': 0}

        for shape in self._shapes_list:
            color_dict[shape.color] += 1

        return HelpTools.turn_dict_to_string(color_dict)

    def sort_shapes_by_area(self):
        sorted_list = sorted(self._shapes_list, key=lambda _shape: _shape.area(), reverse=True)
        dictionary = dict()
        for i in range(len(sorted_list)):
            dictionary[sorted_list[i]] = sorted_list[i].area()

        return dictionary
