#!/usr/bin/python3
"""Define a Square class with size property, area and printing."""

class Square:
    """Represent a square with size, area and printing."""

    def __init__(self, size=0):
        """Initialize a square with an optional size.

        Args:
            size: The size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
