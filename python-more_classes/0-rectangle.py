#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with a size using the setter."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the size of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the size of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the current rectangle area."""
        return self.__width * self.__width

    @property
    def height(self):
        """Retrieves the size of the rectangle."""
        return self.__height

    @width.setter
    def height(self, value):
        """Sets the size of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle area."""
        return self.__height * self.__height
