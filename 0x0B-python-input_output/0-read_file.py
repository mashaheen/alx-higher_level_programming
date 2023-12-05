#!/usr/bin/python3
"""Defines file-reading function."""


def read_file(filename=""):
    """Print the contents of text file with utf-8 encoding."""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
