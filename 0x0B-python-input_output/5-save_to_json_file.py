#!/usr/bin/python3
"""This module defines a JSON file-writing  function"""


import json
def save_to_json_file(my_obj, filename):
    """Writes an object to a test file using JSON fomat"""
    with open(filename, "w") as f:
        json.dumps(my_obj, f)

