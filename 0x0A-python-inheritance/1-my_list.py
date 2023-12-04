#!/usr/bin/python3
"""Defines inherited class"""


class MyList(list):
    """Implements sorted printing Mylist class."""

    def print_sorted(self):
        """Print list in sorted order."""
        if issubclass(MyList, list):
            print(sorted(self))
