#!/usr/bin/python3
"""
Defines if the object is exactly an instance of the specified class.
Returns True if exact match, otherwise False.
"""
def is_same_class(obj, a_class):
    return type(obj) == a_class
