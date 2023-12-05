#!/usr/bin/python3
"""Json file reading function."""
import json


def load_from_json_file(filename):
    """Creates object from json file."""
    with open(filename) as f:
        return json.load(f)
