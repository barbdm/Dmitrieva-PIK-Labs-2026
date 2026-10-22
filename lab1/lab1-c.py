import sys
import math

print("Решение биквадратного уравнения: Ax^4 + Bx^2 + C = 0")

coeffs = []
prompts = ['А', 'B', 'C']

for i in range(3):
    coef = None
    if len(sys.argv) > i + 1:
        try:
            coef = float(sys.argv[i + 1])
        except ValueError:
            pass  
            
    while coef is None:
        try:
            coef = float(input(f"Введите коэффициент {prompts[i]}: "))
        except ValueError:
            print("Ошибка: введено некорректное значение. Пожалуйста, введите действительное число.")
            
    coeffs.append(coef)

a, b, c = coeffs[0], coeffs[1], coeffs[2]

result = set() 

if a == 0.0:
    if b != 0.0:
        y = -c / b
        if y > 0.0:
            result.update([math.sqrt(y), -math.sqrt(y)])
        elif y == 0.0:
            result.add(0.0)
else:
    D = b**2 - 4 * a * c
    print(f"Дискриминант D = {D}")
    
    if D >= 0.0:
        y_roots = []
        if D == 0.0:
            y_roots.append(-b / (2.0 * a))
        else:
            sqD = math.sqrt(D)
            y_roots.append((-b + sqD) / (2.0 * a))
            y_roots.append((-b - sqD) / (2.0 * a))

        for y in y_roots:
            if y > 0.0:
                result.update([math.sqrt(y), -math.sqrt(y)])
            elif y == 0.0:
                result.add(0.0)

roots = sorted(list(result))
len_roots = len(roots)

if len_roots == 0:
    print('Нет действительных корней')
else:
    roots_str = ", ".join([f"{x:.4f}" for x in roots])
    print(f'Количество действительных корней: {len_roots}')
    print(f'Корни: {roots_str}')