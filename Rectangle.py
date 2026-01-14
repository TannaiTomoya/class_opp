import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def diagonal(self):
        return math.sqrt(self.height**2 + self.width**2)


# 高さ5・幅6の長方形
rectangle1 = Rectangle(height=5, width=6)
print(round(rectangle1.area(), 2))  # 30.00
print(round(rectangle1.diagonal(), 2))  # 7.81

# 高さ3・幅3の長方形
rectangle2 = Rectangle(height=3, width=3)
print(round(rectangle2.area(), 2))  # 9.00
print(round(rectangle2.diagonal(), 2))  # 4.24
