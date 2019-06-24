# Генераторы - объекты, предназначенные для создания последовательностей

a = sum(range(1, 101))
print(a)


# Функция генератора (возвращает значение с помощью yield, а не return)
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
# Важно понимать, что обычная функция возвращает просто значение и не помнит о предыдущих вызовах
# Генератор же отслеживает где он находится во время предыдущего вызова и возвращает следующее значение


print(type(my_range))

ranger = my_range(1, 5)
print(type(ranger))

for x in ranger:
    print(x)




