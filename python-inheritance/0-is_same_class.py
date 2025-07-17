#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Defines if the object is exactly an instance of the specified class
    Checks for exact type match (and return True for a match)

    """

    return type(obj) == a_class
