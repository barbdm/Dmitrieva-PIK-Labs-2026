import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.perf_counter() #текущее показание всмтроенного секундомера
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        res = time.perf_counter() - self.start_time
        print(f'time: {res:.2f}')

@contextmanager
def cm_timer_2():
    start_time = time.perf_counter()
    yield
    res = time.perf_counter() - start_time
    print(f'time: {res:.2f}')

if __name__ == '__main__':
    print('Проверка cm_timer_1 (через класс):')
    with cm_timer_1():
        time.sleep(5.5)

    print('\nПроверка cm_timer_2 (через contextlib):')
    with cm_timer_2():
        time.sleep(5.5)
