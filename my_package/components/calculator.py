from ..utils.math_utils import add, multiply
from ..utils.string_utils import capitalize


class Calculator:
    def __init__(self):
        self.math = {"add": add, "multiply": multiply}
        self.string = {"capitalize": capitalize}
