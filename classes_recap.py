"""classes_recap: Recap all the python classes concepts"""


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Circle(Shape):
    pi = 3.14
    all_circles = []

    def __init__(self, r=1, x=0, y=0):
        self.radius = r
        super().__init__(x, y)
        self.__class__.all_circles.append(self)

    @staticmethod
    def circle_area(radius):
        return Circle.pi * radius * radius

    @classmethod
    def total_area(cls):
        area = 0
        for i in cls.all_circles:
            area = area + cls.circle_area(i.radius)
        return area

c1 = Circle()
print(c1.radius, c1.x, c1.y)

c2 = Circle(2, 1, 1)
print(c2.radius, c2.x, c2.y)

print(Circle.all_circles)

print(Circle.total_area())