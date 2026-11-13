#!/usr/bin/python3
"""Define a Square class with a private size attribute."""

class Square:
    """Represent a square with a private size."""

    def __init__(self, size):
        """Initialize a square with a given size.

        Args:
            size: The size of the square.
        """
        self.__size = size
