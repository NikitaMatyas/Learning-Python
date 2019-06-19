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
# Если * будет использована с параметром, произвольное количество позиционных аргументов будет сгрупированно в кортеж
def print_args(*args):
    print('Positional argument tuple: ', args)


print_args()
print_args(3, 2, 1, 'wait!', 'uh...')


# Если в функции имеются обязательные позиционные аргументы, то *args отправится в конец списка
def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)


print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')


# Получение аргументов - ключевых слов с помощью **
# Можно использовать ** чтобы сгруппировать аргументы - ключевые слова в словарь
# Где имена аргументов станут ключами, а их значения - соответствующими значениями в словаре
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


# Строки документации
def echo(anything):
    """echo returns its input argument"""
    return anything


def print_if_true(thing, check):
    """
    Prints the first argument it a second argument is true.
    Tre operation is:
    1. Check whether the *second* argument is true.
    2. If it is, print the *first* argument.
    """
    if check:
        print(thing)


help(print_if_true)
# Без форматирования
print(print_if_true.__doc__)


# Функции - это объекты первого класса
# Их можно присваивать переменным, использовать как аргументы для других функций и возвращать из функций
def answer():
    print(42)


def run_something(func):
    func()


# Передача функции как параметра (без круглых скобок, чтобы относится к функции как объекту, а не вызывать)
run_something(answer)


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


# Запускаем функцию run_something_with_args, которая запустит переданную в нее функцию func с аргументами arg1 и arg2
run_something_with_args(add_args, 5, 9)


# Можно объединять этот прием с использованием *args и **kwargs
def sum_args(*args):
    return sum(args)


print(sum_args(10, 10, 30, 10))


def run_with_positional_args(func, *args):
    return func(*args)


print(run_with_positional_args(sum_args, 1, 2, 3, 4))

# Функции можно использовать как элементы списков, кортежей, множеств и словарей или ключи для словарей


# Внутренние функции (можно определить функцию внутри другой функции)
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


print('Outer = ', outer(4, 7))


# Внутрення функция добавляет текст к своему аргументу
def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)


print(knights('Ni!'))


# Замыкания (внутренняя функция может действовать как замыкание - функция, которая генерируется другой функцией)
# и они обе могут изменяться и запоминать значения переменных, которые были созданы вне функции
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2


# Функция inner2() знает значение переменной saying, которое было передано в фунцкию, и запоминанает его
# Строка inner2 возвращает эту особую копию функции inner2, но не вызывает ее
# Это и есть замыкание: динамически созданная функция, которая запоминает, откуда она появилась
a = knights2('Duck')
print(a)
print(type(a))
print(a())

# Анонимные функции: функция lambda() - анонимная функция, выраженная одним выражением


# Для начала определим обычную функцию edit_story()
# func - функция, которая должна быть применена к каждому слову в списке words
def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


# Еще одна функция запишет с большой буквы каждое слово и добавит к нему восклицательный знак
def enliven(word):
    return word.capitalize() + '!'


edit_story(stairs, enliven)
print('\n')
# Лямбда принимает один аргумент word
# Все, что находится между двоеточием и закрывающей скобкой, является определением функции
edit_story(stairs, lambda word: word.capitalize() + '!')

# Лямбды полезны в случаях, когда нужно определить множество мелких функций и запомнить все их имена
# В частности, можно использовать лямбды в графических UI, чтобы определить функции внешнего вызова
