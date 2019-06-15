a = [{'key': 'value'}, {1, 2, 3}, [1, 3, 3], 453, "Snake"]

result = list()


def type_conversion(my_object):
    for i in my_object:
        if isinstance(i, (int, str, bool)):
            result.append(i)
        elif isinstance(i, dict):
            for i2 in i.items():
                if isinstance(i2, (list, tuple, set)):
                    type_conversion(i2)
                else:
                    result.append(i2)
        elif isinstance(i, (list, tuple, set)):
            type_conversion(i)


type_conversion(a)
print('Ввод: ', a)
print('Вывод: ', result)

