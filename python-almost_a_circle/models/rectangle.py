#!/usr/bin/python3
"""comment"""


from models.base import Base


class Rectangle(Base):
    """comment"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.validator(width, "width")
        self.validator(height, "height")
        self.validator(x, "x")
        self.validator(y, "y")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validator(self, value, name):
        """comment"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator(value, "height")
        self.__height = value

    def area(self):
        """comment"""
        return self.__height * self.__width

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator(value, "y")
        self.__y = value

    def display(self):
        """comment"""
        for _ in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """comment"""
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({self.id}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """comment"""
        my_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for name, value in zip(my_list, args):
                setattr(name, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """comment"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
            }

    def __repr__(self):
        return str(self.to_dictionary())
