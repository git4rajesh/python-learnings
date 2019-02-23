class Shape:
    def __init__(self):
        self.color = ''


class Rect(Shape):
    def __init__(self, color):
        self.len = 5
        self.breadth = 4
        self.color = color

    def get_area(self):
        return self.len * self.breadth

    def get_details(self):
        print('This is a rectangle with {0} color and area {1} sq.meter'.format(self.color.col, self.get_area()))


class Circle(Shape):
    def __init__(self, color):
        self.radius = 2
        self.color = color

    def get_area(self):
        return 2 * 22 / 7 * self.radius

    def get_details(self):
        print('This is a circle with {0} color and area {1} sq.meter'.format(self.color.col, self.get_area()))
