import math
from lab_python_oop.function import Function

class Derivative(Function):
    """Производная функции: f'(x) = k / sqrt(1 - x^2)"""

    def __init__(self, source, factor):
        super().__init__("Производная от " + source.name, factor)
        self.__source = source      # исходная функция

    @property
    def source(self):
        """Функция, от которой взята производная"""
        return self.__source

    def value(self, x):
        self.check_x(x)
        if not -1 < x < 1:
            raise ValueError("Производная определена только при -1 < x < 1")
        return self.coefficient / math.sqrt(1 - x ** 2)

    def derivative(self):
        raise NotImplementedError("Вторая производная не реализована")

    def __str__(self):
        return super().__str__() 