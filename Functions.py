# Функции


# Объявление функции
def do_nothing():
    pass


# Вызов функции
do_nothing()


# Функция без параметров
def make_a_sound():
    print('quack')


make_a_sound()


# Функция, возвращающая значение
def agree():
    return True


if agree():
    print('Splendid!')
else:
    print('That was unexpected. ')


# Функция с параметром
def echo(anything):
    return anything + ' ' + anything


print(echo('Rumplestilskin'))


# Функция определения цвета
def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper"
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it"
    else:
        return "I've never heard of the color " + color + "."


print(commentary('orange'))


# Позиционные аргументы (чьи значения копируются в соответствующие параметры согласно порядку их следования)
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))

# Если передать в качестве последнего аргумента марку вина, то результат выйдет совершенно другим :)
print(menu('beef', 'bagel', 'bordeaux'))

# Аргументы - ключевые слова (порядок следования аргументов может быть любым)
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# Можно объединять позиционные аргументы и аргументы - ключевые слова (позиционные необходимо указывать первыми)
print(menu('frostenac', dessert='flan', entree='fish'))


# Указываем значение параметра по умолчанию (оно используется, если вызовающая строка не передала аргумент)
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


# Значение аргумента по умолчанию высчитывается, когда функция определяется, а не выполняется
# Поэтому не стоит использовать изменяемый тип данных вроде списка или словаря в качестве аргумента по умолчанию
print(menu('chardonnay', 'chicken'))
print(menu('chardonnay', 'chicken', 'cake'))


# Получение позиционных аргументов с помощью *

