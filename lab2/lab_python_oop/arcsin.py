import math
from lab_python_oop.function import Function
from lab_python_oop.derivative import Derivative

class Arcsin(Function):
    """f(x) = k * arcsin(x), область определения [-1; 1]"""

    def __init__(self, coefficient=1.0):
        super().__init__("Арксинус", coefficient)

    def value(self, x):
        self.check_x(x)
        if not -1 <= x <= 1:
            raise ValueError("Арксинус определён только при -1 <= x <= 1")
        return self.coefficient * math.asin(x)

    def derivative(self):
        return Derivative(self, self.coefficient)      # k / sqrt(1 - x^2)

    def describe(self):       #переопределяем метод родителя
        return "Арксинус: область определения [-1; 1], область значений [-pi/2; pi/2]"