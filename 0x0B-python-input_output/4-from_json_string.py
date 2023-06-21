#!/usr/bin/python3
"""This module define a JSON-to-string function"""
import json

def from_json_string(my_str):
    """Returns the python object representation of the JSON string"""
    return json.loads(my_str)
