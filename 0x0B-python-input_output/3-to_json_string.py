#!/usr/bin/python3
"""String-to-JSON."""
import json


def to_json_string(my_obj):
    """Return string in form of json."""
    return json.dumps(my_obj)
