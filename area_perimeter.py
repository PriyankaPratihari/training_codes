"""
area perimeter
"""
import math


class Shape:
    """shape"""
    def __init__(self, shape_type):
        """

        :param shape_type:
        """
        self.shape_type = shape_type

    def area(self):
        """area"""

    def perimeter(self):
        """perimeter"""

    def volume(self):
        """volume"""


class Square(Shape):
    """square"""
    def __init__(self, side):
        """

        :param side:
        """
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        """

        :return:
        """
        return 4 * self.side


class Rectangle(Shape):
    """rectangle"""
    def __init__(self, length, width):
        """

        :param length:
        :param width:
        """
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        """

        :return:
        """
        return self.length * self.width

    def perimeter(self):
        """

        :return:
        """
        return 2 * (self.length + self.width)


class Circle(Shape):
    """class """
    def __init__(self, radius):
        """

        :param radius:
        """
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """

        :return:
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """

        :return:
        """
        return 2 * math.pi * self.radius


class Cube(Shape):
    """
    This class is for Calculating Volume, Total Surface area & Lateral Surface area of cube.
    """
    def __init__(self, side):
        """

        :param side:
        """
        super().__init__("Cube")
        self.side = side

    def ts_area(self):
        """

        :return:
        """
        return 6 * (self.side ** 2)

    def ls_area(self):
        """

        :return:
        """
        return 4 * (self.side ** 2)

    def volume(self):
        """

        :return:
        """
        return self.side ** 3


if __name__ == '__main__':
    while True:
        shape_type_input = input("Select a shape type (2D or 3D): ")
        if shape_type_input == "2D":
            shape_input = input("Select a 2D shape (square, rectangle, circle): ")
            if shape_input == "square":
                side_input = float(input("Enter the side length: "))
                square = Square(side_input)
                print("Area = {:.2f}".format(square.area()))
                print("Perimeter = {:.2f}".format(square.perimeter()))

            elif shape_input == "rectangle":
                length_input = float(input("Enter the length: "))
                width_input = float(input("Enter the width: "))
                rectangle = Rectangle(length_input, width_input)
                print("Area = {:.2f}".format(rectangle.area()))
                print("Perimeter = {:.2f}".format(rectangle.perimeter()))

            elif shape_input == "circle":
                radius_input = float(input("Enter the radius: "))
                circle = Circle(radius_input)
                print("Area = {:.2f}".format(circle.area()))
                print("Perimeter = {:.2f}".format(circle.perimeter()))

            else:
                print("Invalid shape input. Please try again.")

        elif shape_type_input == "3D":
            shape_input = input("Select a 3D shape (cube, sphere): ")

            if shape_input == "cube":
                side_input = float(input("Enter the side length: "))
                cube = Cube(side_input)
                print("ts_area = {:.2f}".format(cube.ts_area()))
                print("ls_area = {:.2f}".format(cube.ls_area()))
                print("volume = {:.2f}".format(cube.volume()))

            else:
                print("Invalid shape input. Please try again.")
