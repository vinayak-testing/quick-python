"""circle module: contains Circle class"""


class Shape:
    """Shape Class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class Circle(Shape):
    """Circle class"""
    pi = 3.14
    all_circles = []

    def __init__(self, x, y, r=1):
        """Creates a circle of given radius"""
        super().__init__(x, y)
        self.radius = r
        self.__class__.all_circles.append(self)

    def area(self):
        """determine area of circle"""
        return self.radius * self.radius * self.__class__.pi;

    @staticmethod
    def total_area():
        total_area = 0
        for c in Circle.all_circles:
            total_area += c.area()
        return total_area


class Square(Shape):

    def __init__(self, x, y, side=1):
        super().__init__(x, y)
        self.side = side


# circle1 = Circle(1)
# circle2 = Circle(2)
# circle3 = Circle(3)

print(Circle.total_area())

# Lets create some circles and squares

my_sqr = Square(0,0,4)
my_circle = Circle(2, 2, 4)


my_sqr.move(2,3)
my_circle.move(5,6)

print("Position of Circle is x:{0}, y:{1}".format(my_circle.x, my_circle.y))
print("Position of Square is x:{0}, y:{1}".format(my_sqr.x, my_sqr.y))











