'''
Implement class named Color.
It should construct color from hex value (e.g. #ffffff) and have optional name = ‘color’.
Add possibility to set and get name (property).
Add property rgb that returns rgb tuple of color
Add method to convert hex value to rgb tuple.
Add possibility to construct object from rgb value (classmethod).
Add methods to convert: hex > rgb; rgb > hex (staticmethod).
Add str and repr methods; add possibility to compare 2 colors (__eq__)
'''


import collections


# class Color:
#     def __init__(self, hex_value, name=None):
#         self.hex_value = hex_value
#         self._name = name
#         self._rgb = self.hex_to_rgb(hex_value)
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#     @property
#     def rgb(self):
#         return self._rgb
#
#     @staticmethod
#     def hex_to_rgb(hex_value):
#         return (int(hex_value[1:3], 16), int(hex_value[3:5], 16), int(hex_value[5:], 16))
#
#     @classmethod
#     def construct_object_from_rgb_value(cls, rgb):
#         return Color(cls.rgb_to_hex(rgb))
#
#     @staticmethod
#     def rgb_to_hex(rgb):
#         return '#'+''.join([hex(int(item))[2:] if int(item)!=0 else '00' for item in rgb])
#
#     def __str__(self):
#         return str(self.name)
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}{self.rgb}"
#
#     def __eq__(self, color):
#         return self.hex_value == color.hex_value


from typing import NamedTuple


class Color(NamedTuple):

    hex_value: str
    color_name: str = 'color'

    @property
    def name(self):
        return self.color_name

    @name.setter
    def name(self, name):
        self.color_name = name

    @property
    def rgb(self):
        return self.hex_to_rgb(self.hex_value)

    @staticmethod
    def hex_to_rgb(hex_value):
        return (int(hex_value[1:3], 16), int(hex_value[3:5], 16), int(hex_value[5:], 16))

    @classmethod
    def construct_object_from_rgb_value(cls, rgb):
        return Color(cls.rgb_to_hex(rgb))

    @staticmethod
    def rgb_to_hex(rgb):
        return '#'+''.join([hex(int(item))[2:] if int(item)!=0 else '00' for item in rgb])

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"{self.__class__.__name__}{self.rgb}"

    def __eq__(self, color):
        return self.hex_value == color.hex_value


c1 = Color('#ffffff')
print(c1)
print(c1.rgb)
print(Color.rgb_to_hex((255, 255, 255)))
c2 = Color('#fffff0')
print(c1 == c2)
c3 = Color.construct_object_from_rgb_value((255, 0, 0))
print(c3)
print(c3.hex_value)
print(c3.__repr__())