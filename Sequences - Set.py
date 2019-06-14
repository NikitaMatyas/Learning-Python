# Множества
# Множество похоже на словарь, значения которого опущены. Оно имеет только ключи. Ключи должны быть уникальны.

# Создание множества с помощью функции set()
empty_set = set()
print(set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

# Преобразование других типов данных с помощью set()
print(set('letters'))

my_list = ['qqq', 'www', 'eee', 'rrr', 'ttt', 'yyy']
my_set = set(my_list)
print(my_set)

my_tuple = ('Ummagumma', 'Echoes', 'Atom Hearth Mother')
my_set = set(my_tuple)
print(my_set)

# В случае со словарем возвращает только ключи
my_dict = {'apple': 'red', 'orange': 'orange', 'cherry': 'red'}
my_set = set(my_dict)
print(my_set)

# Проверка на наличие значений с помощью in (Словарь со значениями из множеств)
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print('\n')

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

print('\n')

# Комбинации и операторы
# Любой напиток, содержащий апельсиновый сок или вермут (& - оператор пересечения множеств)
for name, contents in drinks.items():
    if contents & {'vermuth', 'orange juice'}:
        print(name)

print('\n')

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

# Пересечение множеств
a = {1, 2}
b = {2, 3}
print (a & b)
print(a.intersection(b))

# Объединение множеств
print(a | b)
print(a.union(b))

# Разность множеств
# Члены только первого, но не второго
print(a - b)
print(a.difference(b))

# Исключающее ИЛИ
print(a ^ b)
print(a.symmetric_difference(b))

# Является ли одно множество подмножеством другого / самого себя
print(a <= b)
print(a.issubset(b))

print(a <= a)
print(a.issubset(a))

# Собственное подмножество (второе множество должно содержать все члены первого и несколько других)
print(a < b)
print(a < a)



