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

    def subtract(self, x):
        self.result -= x
        return self
