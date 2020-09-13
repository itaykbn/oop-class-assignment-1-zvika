from abc import ABC, abstractmethod


class Shape(ABC):

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        color_list = ['blue', 'red', 'white', 'black', 'green', 'orange', 'pink', 'purple', 'yellow', 'gray']
        if color in color_list:
            self._color = color
        else:
            raise ValueError("color not legal")

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def get_type(self):
        return type(self).__name__
