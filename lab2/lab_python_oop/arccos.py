import math
from lab_python_oop.function import Function
from lab_python_oop.derivative import Derivative

class Arccos(Function):
    """f(x) = k * arccos(x), область определения [-1; 1]"""

    def __init__(self, coefficient=1.0):
        super().__init__("Арккосинус", coefficient)

    def value(self, x):
        self.check_x(x)
        if not -1 <= x <= 1:
            raise ValueError("Арккосинус определён только при -1 <= x <= 1")
        return self.coefficient * math.acos(x)

    def derivative(self):
        return Derivative(self, -self.coefficient)     # -k / sqrt(1 - x^2)

    def __str__(self):        # расширяем метод родителя через super()
        return super().__str__() + ", область определения [-1; 1], область значений [0; pi]"