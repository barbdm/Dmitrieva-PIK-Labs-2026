import sys
import math

class InputHandler:
    @staticmethod
    def get_coef(index, prompt):
        if len(sys.argv) > index:
            try:
                return float(sys.argv[index])
            except ValueError:
                pass
                
        while True:
            try:
                return float(input(prompt + " "))
            except ValueError:
                print("Ошибка: введите корректное действительное число.")


class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.roots = set()

    def solve(self):
        if self.a == 0.0:
            if self.b != 0.0:
                self._calculate_x(-self.c / self.b)
            return

        D = self.b**2 - 4 * self.a * self.c
        print(f"Дискриминант D = {D}")

        if D == 0.0:
            self._calculate_x(-self.b / (2.0 * self.a))
        elif D > 0.0:
            sqD = math.sqrt(D)
            self._calculate_x((-self.b + sqD) / (2.0 * self.a))
            self._calculate_x((-self.b - sqD) / (2.0 * self.a))

    def _calculate_x(self, y):
        if y > 0.0:
            self.roots.update([math.sqrt(y), -math.sqrt(y)])
        elif y == 0.0:
            self.roots.add(0.0)

    def print_result(self):
        sorted_roots = sorted(list(self.roots))
        if not sorted_roots:
            print('Нет действительных корней')
        else:
            roots_str = ", ".join(map(lambda x: f"{x:.4f}", sorted_roots))
            print(f'Найдено корней ({len(sorted_roots)}): {roots_str}')


def main():
    print("Решение биквадратного уравнения: Ax^4 + Bx^2 + C = 0")
    a = InputHandler.get_coef(1, 'Введите коэффициент А:')
    b = InputHandler.get_coef(2, 'Введите коэффициент B:')
    c = InputHandler.get_coef(3, 'Введите коэффициент C:')

    equation = BiquadraticEquation(a, b, c)
    equation.solve()
    equation.print_result()

if __name__ == "__main__":
    main()