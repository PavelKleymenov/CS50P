"""Impement a class which defines a cookie jar"""
class Jar:

    """Initialize a cookie jar with the given capacity,
    which represents the maximum number of cookies that can fit in the cookie jar"""
    def __init__(self, capacity=12):

        # Render an error if the capacity is a negative integer
        if capacity < 0:
            raise ValueError("No such thing as negative number of cookies")

        # Otherwise, return the number of cookies the jar can hold
        else:
            self._capacity = capacity
            self._size = 0

    """Implement a method that returns the number of cookies in the cookie jar"""
    def __str__(self):
        return self.size * '🍪'

    """Implement a method that allows users to add some number of cookies to the cookie jar"""
    def deposit(self, n):

        # Render an error if the user tries to deposit the number of cookies that is too big for the jar
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError

        # Otherwise, return the number of added cookies
        self._size += n

    """Implement a method that allows users to take some number of cookies from the jar"""
    def withdraw(self, n):

        # Render an error if the user tries to snatch the number of cookies that is higher that the jar currently has
        if n > self.size:
            raise ValueError

        # Otherwise, return the number of cookies grabbed
        self._size -= n

    # Add validation logic around getting and setting a value
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


