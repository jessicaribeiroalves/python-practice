import math


class Polygon:

    def get_area(self):
        raise NotImplementedError("You should implement the get_area method.")

    def get_sides(self):
        raise NotImplementedError("You should implement the get_sides method.")

    def get_perimeter(self):
        return sum(self.get_sides())


class Triangle(Polygon):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(
            semi_perimeter *
            (semi_perimeter - self.side1) *
            (semi_perimeter - self.side2) *
            (semi_perimeter - self.side3)
        )

    def get_sides(self):
        return [self.side1, self.side2, self.side3]


class Rectangle(Polygon):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_sides(self):
        return [self.width, self.height, self.width, self.height]


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
