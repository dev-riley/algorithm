class Point:  # 좌표
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Point): # 좌표를 2개 받아와야 함.
    def __init__(self, first, second):
        self.first = first # 좌측 상단 좌표
        self.second = second # 우측 하단 좌표

    def get_area(self):
        return abs(self.first.x - self.second.x) * abs(self.first.y - self.second.y)

    def get_perimeter(self):
        return 2 * (abs(self.first.x - self.second.x) + abs(self.first.y - self.second.y))

    def is_square(self):
        return abs(self.first.x - self.second.x) == abs(self.first.y - self.second.y)

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())