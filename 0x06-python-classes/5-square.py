#!/usr/bin/python3

"""Defining a class"""


class Square:
    """class representing a square"""

    def __init__(self, size):
        """Make an instance of a square.

        Args:
            size : square size.
        """

        self.__size = size

    @property
    def size(self):
        """getter/setter for the size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return  square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square area with #."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
