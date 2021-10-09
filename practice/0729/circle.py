class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)

circle = Circle()
circle.r = 3
circle.center = (2, 4)

print(circle.area())
print(circle.circumference())
