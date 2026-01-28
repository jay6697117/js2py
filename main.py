# math_utils.py
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x):
        self.result += x
        return self


# main.py
from math_utils import add, subtract, Calculator
import math_utils as math

calc = Calculator()
print(add(5, 3))
print(math.subtract(10, 4))
