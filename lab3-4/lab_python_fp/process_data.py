import json
import sys
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1

path = sys.argv[1] if len(sys.argv) > 1 else '/home/asus/labs/Dmitrieva-PIK-Labs-2026/lab3/lab_python_fp/data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=lambda x: (len(x.split()), x.lower()))

@print_result
def f2(arg):
    return list(filter(lambda x: len(x.split()) <= 2, arg))

@print_result
def f3(arg):
    return list(map(lambda x: f'Senior {x}', arg))

@print_result
def f4(arg):
    salaries = sorted(gen_random(len(arg), 20000, 300000))
    return [f'{job}, зарплата {salary} руб.' for job, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
