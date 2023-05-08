import math


class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def area(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Cube(Shape):
    def __init__(self, side):
        super().__init__("Cube")
        self.side = side

    def ts_area(self):
        return 6 * (self.side ** 2)

    def ls_area(self):
        return 4 * (self.side ** 2)

    def volume(self):
        return self.side ** 3


print("select a shape type 2D or 3D")

while True:
    shape_type_input = input("Select a shape type (2D or 3D): ")
    if shape_type_input in ('2D', '3D'):
        try:
            shape_type_input = input("Select a shape type (2D or 3D): ")

        except ValueError:
            print("Invalid input.")
            continue

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
            next_calculation = input("calculate volume ? (yes/no): ")
            formula = input("Enter the formula for volume: ")

            var_values = {}
            for var in formula.split():
                if var.isalpha() and var not in var_values:
                    val = float(input("Enter value for {}: ".format(var)))
                    var_values[var] = val

            volume = eval(formula, var_values)
            print("Volume = ", volume)

        else:
            print("Invalid shape input. Please try again.")
if __name__ == '__main__':
    shape = Shape(" ")
