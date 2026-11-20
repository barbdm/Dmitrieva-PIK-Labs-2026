import random

def gen_random(num_count, begin, end):
    current_min = begin
    for _ in range(num_count):
        current_min = random.randint(current_min, end)
        yield current_min

if __name__ == '__main__':
    print("Тест 1 (5 чисел от 1 до 3):")
    print(list(gen_random(5, 1, 3)))

    print("\nТест 2 (7 чисел от 10 до 50):")
    print(list(gen_random(7, 10, 50)))

    print("\nТест 3 (10 чисел от 0 до 100):")
    print(list(gen_random(10, 0, 100)))