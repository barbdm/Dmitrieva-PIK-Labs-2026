def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value

    else:
        for item in items:
            result_dict = {}
            for key in args:
                value = item.get(key)
                if value is not None:
                    result_dict[key] = value
            if len(result_dict) > 0:
                yield result_dict

if __name__ == '__main__':
    funcs = [
        {'name': 'arcsin(x)', 'domain': '[-1, 1]', 'derivative': '1 / sqrt(1 - x^2)'},
        {'name': 'arccos(x)', 'domain': '[-1, 1]', 'derivative': '-1 / sqrt(1 - x^2)'},
        {'name': None, 'domain': '(-1, 1)', 'derivative': '1 / sqrt(1 - x^2)'},
        {'name': None, 'domain': '(-inf, +inf)', 'derivative': None}
    ]

    print("Тест 1 (один аргумент 'name'):")
    print(list(field(funcs, 'name')))

    print("\nТест 2 (два аргумента 'name', 'derivative'):")
    print(list(field(funcs, 'name', 'derivative')))