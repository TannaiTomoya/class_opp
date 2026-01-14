import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # 30.00 / 9.00 を出すため "文字列" で返す
    def area(self):
        return f"{self.height * self.width:.2f}"

    def diagonal(self):
        return round(math.sqrt(self.height**2 + self.width**2), 2)


if __name__ == "__main__":
    rectangle1 = Rectangle(height=5, width=6)
    print(rectangle1.area())  # 30.00
    print(rectangle1.diagonal())  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    print(rectangle2.area())  # 9.00
    print(rectangle2.diagonal())  # 4.24
