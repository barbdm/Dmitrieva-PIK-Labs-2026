import cowsay
from lab_python_oop.arcsin import Arcsin
from lab_python_oop.arccos import Arccos

def read_number(prompt):
    """Просит ввести число, пока пользователь не введёт корректно"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Нужно ввести число!")

def demo(func, x):
    """Показывает работу всех методов для объекта func в точке x"""
    print(func)                                  
    print(func.describe())
    try:
        print(f"f({x}) = {func.value(x)}")
    except ValueError as e:
        print("Ошибка значения:", e)
    d = func.derivative()
    print(d)
    print(d.describe())
    print("Исходная функция производной:", d.source.name)
    try:
        print(f"f'({x}) = {d.value(x)}")
    except ValueError as e:
        print("Ошибка производной:", e)
    try:
        d.derivative()
    except NotImplementedError as e:
        print("Ожидаемая ошибка:", e)
    try:
        func.coefficient = 0                     
    except ValueError as e:
        print("Сеттер не пропустил:", e)
    try:
        func.name = "   "                     
    except ValueError as e:
        print("Сеттер не пропустил:", e)        

def main():
    while True:
        print("\n1 - Арксинус\n2 - Арккосинус\n0 - Выход")
        choice = input("Выбор: ")
        if choice == "0":
            break
        if choice not in ("1", "2"):
            print("Нет такого пункта")
            continue
        k = read_number("Коэффициент k (не 0): ")
        x = read_number("Значение x (от -1 до 1): ")
        try:
            func = Arcsin(k) if choice == "1" else Arccos(k)
        except ValueError as e:
            print("Ошибка:", e)
            continue
        demo(func, x)
    cowsay.cow("Лабораторная готова!")           # метод внешнего пакета

if __name__ == "__main__":
    main()