from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.items = list(items)[::-1]
        self.index = 0

    def __next__(self):
        while self.index < len(self.items):
            current = self.items[self.index]
            self.index += 1

            if self.ignore_case and isinstance(current, str):
                check_key = current.lower()
            else:
                check_key = current

            if check_key not in self.seen:
                self.seen.add(check_key)
                return current

        raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print("Тест 1 (список чисел в обратном порядке):", list(Unique(data1)))

    data2 = gen_random(10, 1, 3)
    print("Тест 2 (генератор):", list(Unique(data2)))

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    print("Тест 3 (ignore_case=False):", list(Unique(data3)))
    
    print("Тест 4 (ignore_case=True):", list(Unique(data3, ignore_case=True)))
    