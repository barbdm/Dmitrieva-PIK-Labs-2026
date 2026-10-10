import sys
import math

def get_coef(index, prompt):
    """
    Читает коэффициент из командной строки. Если он некорректен или отсутствует,
    запрашивает его с клавиатуры до тех пор, пока не будет введено корректное число.
    """

    if len(sys.argv) > index:
        try:
            return float(sys.argv[index])
        except ValueError:
            pass
            
    while True:
        coef_str = input(prompt + " ")
        try:
            return float(coef_str)
        except ValueError:
            print("Ошибка: введено некорректное значение. Пожалуйста, введите действительное число.")

def get_roots(a, b, c):
    """
    Вычисляет дискриминант и действительные корни биквадратного уравнения.
    """
    result = set() 
    
    if a == 0.0:
        if b != 0.0:
            y = -c / b
            if y > 0.0:
                result.update([math.sqrt(y), -math.sqrt(y)])
            elif y == 0.0:
                result.add(0.0)
        return sorted(list(result))

    D = b*b - 4*a*c
    print(f"Дискриминант D = {D}")
    
    if D < 0.0:
        return []

    y_roots = []
    if D == 0.0:
        y_roots.append(-b / (2.0*a))
    else:
        sqD = math.sqrt(D)
        y_roots.append((-b + sqD) / (2.0*a))
        y_roots.append((-b - sqD) / (2.0*a))

    for y in y_roots:
        if y > 0.0:
            result.update([math.sqrt(y), -math.sqrt(y)])
        elif y == 0.0:
            result.add(0.0)

    return sorted(list(result))

def main():
    print("Решение биквадратного уравнения: Ax^4 + Bx^2 + C = 0")
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    
    roots = get_roots(a, b, c)
    
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет действительных корней')
    else:
        roots_str = ", ".join(map(lambda x: f"{x:.4f}", roots))
        print(f'Количество действительных корней: {len_roots}')
        print(f'Корни: {roots_str}')

if __name__ == "__main__":
    main()