#!/usr/bin/python3
"""Defines yet another class-checking function."""


def inherits_from(obj, a_class):
    """Checks if  object is  inherited instance of  class.

    Args:
        obj (any): The object.
        a_class (type): The class.
    Returns:
        If obj is  inherited instance of class returns True, else False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
