import time

import math
class Vector:   
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        # Vector.__len__ = Vector.__abs__
    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __bool__(self) -> bool:
        return bool(self.x or self.y)
    
    def __add__(self, other):
        assert type(other) is Vector, "Type of other is meant to be vector"
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other: int):
        assert type(other) is int, "Other supposed to be integer/scalar"
        return Vector(self.x * other, self.y * other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __str__(self):
        return f"{self.x}i + {self.y}j"
def constant(f):
    def fset(self, val):
        raise AttributeError
    return property(fset=fset, fget=lambda self : f())
class Constants:
    @constant
    def PI():
        return 22/7

    def create_constant(name, value) -> None:
        setattr(Constants ,name, constant(lambda : value))



def bubble_sort(l):
    def isSorted(array):
        for index, elem in enumerate(array):
            if index + 1 == len(array):
                continue
            if array[index+1] < elem:
                return False
        return True
    while not isSorted(l):
        for index, elem in enumerate(l):
            if index + 1== len(l):
                continue
            if l[index+1] < elem:
                l[index], l[index+1] = l[index+1], l[index]
    return l
