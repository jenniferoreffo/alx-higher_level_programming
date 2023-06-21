#!/usr/bin/python3
    """Writes a string to a UTF-8 text file"""
.   def write_filename(filename= "", test="")
    """ Writes a string to a UTF-8 text file""" 
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
