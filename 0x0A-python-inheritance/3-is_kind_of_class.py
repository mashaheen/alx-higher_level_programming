#!/usr/bin/python3
"""Defines class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is  instance or inherited instance of  class.

    Args:
        obj (any): The object.
        a_class (type): The class.
    Returns:
        If obj is  instance or inherited instance of class returns True, else false.
    """
    if isinstance(obj, a_class):
        return True
    return False
