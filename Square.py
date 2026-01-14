import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def diagonal(self):
        return math.sqrt(2) * self.side


# 一辺 1.5 の正方形
square1 = Square(side=1.5)
print(round(square1.area(), 2))  # 2.25
print(round(square1.diagonal(), 2))  # 2.12

# 一辺 15 の正方形
square2 = Square(side=15)
print(round(square2.area(), 2))  # 225
print(round(square2.diagonal(), 2))  # 21.21
