from abc import ABC, abstractmethod

class Function(ABC):
    """Абстрактная функция одной переменной: f(x) = k * g(x)"""

    def __init__(self, name, coefficient=1.0):
        self.__name = ""            
        self.__coefficient = 1.0
        self.name = name            
        self.coefficient = coefficient

    @property
    def name(self):
        """Название функции"""
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        if not value.strip():
            raise ValueError("Название не может быть пустым")
        self.__name = value.strip()

    @property
    def coefficient(self):
        """Множитель k перед функцией"""
        return self.__coefficient

    @coefficient.setter
    def coefficient(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Коэффициент должен быть числом")
        if value == 0:
            raise ValueError("Коэффициент не может быть равен нулю")
        self.__coefficient = float(value)

    @staticmethod
    def check_x(x):
        """Проверка, что аргумент - число"""
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError("Аргумент x должен быть числом")

    @abstractmethod
    def value(self, x):
        """Возвращает значение функции в точке x"""

    @abstractmethod
    def derivative(self):
        """Возвращает производную функции"""

    def describe(self):       #в Arcsin переопределяется, в Arccos нет
        """Общее описание""" 
        return f"Тригонометрическая функция '{self.name}' вида k*g(x), k = {self.coefficient}"

    def __str__(self):
        return f"{self.name} с k = {self.coefficient}"