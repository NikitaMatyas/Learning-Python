# Кортежи (в отличие от списков, кортежи неизменяемы)
# Кортежи занимают меньше места чем списки
# Нельзя уничтожить элемент кортежа по ошибке
# Можно использовать кортежи как ключи словаря
# Аргументы функции передаются как кортежи

# Создание кортежей с помощью оператора ()
empty_tuple = ()
print(empty_tuple)

# Кортеж с одним элементом (ставится запятая после)
one_marx = 'Groucho',
print(one_marx)

# Кортеж с произвольным количеством элементов (запятая не ставится после последнего)
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

# Можно окружить скобками для наглядности
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

# Присваивание нескольких переменных за один раз (последовательно)
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a, b, c)

# Обмен значениями без дополнительной переменной
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password, icecream)

# Создание кортежа из другого объекта с помощью tuple()
marx_list = ['Groucho', 'Chicho', 'Harpo']
print(tuple(marx_list))
