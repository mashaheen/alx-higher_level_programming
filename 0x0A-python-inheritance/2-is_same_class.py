#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Checks if `obj` is instance of the class

    Args:
        obj (any): The object
        a_class (any): The class

    Returns:
        `True` if the object is instance of the class, else return `False`
    """

    if type(obj) == a_class:
        return True

    return False
