from abc import ABCMeta, abstractmethod

# 抽象
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# 实现
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass

# 细化抽象
class Rectangle(Shape):
    name = '长方形'

    def draw(self):
        self.color.paint(self)

# 如果要扩展形状，只需要添加形状类
class Circle(Shape):
    name = '圆形'

    def draw(self):
        self.color.paint(self)

# 细化实现
class Red(Color):
    def paint(self, shape):
        print('画红色的%s' % shape.name)

# 如果要扩展颜色，只需要添加颜色类
class Green(Color):
    def paint(self, shape):
        print('画绿色的%s' % shape.name)

rectangle = Rectangle(Red())
rectangle.draw()
circle = Circle(Green())
circle.draw()