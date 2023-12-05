#!/usr/bin/python3
"""Json to string function."""
import json


def from_json_string(my_str):
    """Return the object of a json string."""
    return json.loads(my_str)
