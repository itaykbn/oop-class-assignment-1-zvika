from abc import ABC, abstractmethod
from help_tools import HelpTools


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
            HelpTools.add_to_log(40, "illegal color - not in list")
            raise ValueError("illegal color - not in list")

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def get_type(self):
        return type(self).__name__
