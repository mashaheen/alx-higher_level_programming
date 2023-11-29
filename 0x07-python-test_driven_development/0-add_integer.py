#!/usr/bin/python3
# 0-add_integer.py
"""A function for adding integers."""


def add_integer(a, b=98):
    """Return the addition of a and b.

    Floats are typecasted into ints before performing addition.

    Raises:
        TypeError: If a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
