def print_result(fn):
    def wrapper(*args, **kwargs):
        print(fn.__name__)
        res = fn(*args, **kwargs)
        if isinstance(res, list):
            for el in res:
                print(el)
        elif isinstance(res, dict):
            for key, value in res.items():
                print(f'{key} = {value}')
        else:
            print(res)
        return res
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()