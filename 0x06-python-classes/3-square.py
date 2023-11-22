#!/usr/bin/python3

"""Defining a class"""


class Square:
    """class representing a square"""

    def __init__(self, size):
        """Make an instance of a square.

        Args:
            size : square size.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Return  square area."""
        return (self.__size * self.__size)
