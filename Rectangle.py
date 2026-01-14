import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        # 小数点第2位まで必ず表示
        return f"{self.height * self.width:.2f}"

    def diagonal(self):
        # 小数点第2位まで必ず表示
        diagonal = math.sqrt(self.height**2 + self.width**2)
        return f"{diagonal:.2f}"


if __name__ == "__main__":
    rectangle1 = Rectangle(height=5, width=6)
    print(rectangle1.area())  # 30.00
    print(rectangle1.diagonal())  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    print(rectangle2.area())  # 9.00
    print(rectangle2.diagonal())  # 4.24
