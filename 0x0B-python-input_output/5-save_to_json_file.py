#!/usr/bin/python3
"""JSON writing to a file function."""
import json


def save_to_json_file(my_obj, filename):
    """Writing to a file using json."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
