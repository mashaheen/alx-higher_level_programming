#!/usr/bin/python3
# 0-rectangle.py
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get rec width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rec width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get rec height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rec height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rec area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return rec perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")