# Декоратор - функция, которая принимает одну функцию в качестве аргумента и возвращает другую функцию

'''
Функция document_it() определяет декоратор, который:
1. выведет имя функции и значение переданных в нее аргументов;
2. запустит функцию с полученными аргументами;
3. выведет результат;
4. вернет модифицированную функцию, готовую для использования.
'''


def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


''' 
Независимо от того, какую функцию func передать document_it(), получим новую функцию, которая содержит дополнительные 
значения, добавляемые document_it(). Декоратор не обязательно должен запускать код функции func, но функция 
document_it() вызовет часть func, поэтому мы получим результат работы функции func, а также дополнительные данные
'''


def add_ints(a, b):
    return a + b


cooler_add_ints = document_it(add_ints)  # Мануальное присваивание декоратора
cooler_add_ints(3, 5)


# В качестве альтернативы мануальному присваиванию, можно добавить конструкцию @имя_декоратора перед функцией
@document_it
def add_ints(a, b):
    return a + b


add_ints(3, 5)


# Каждая функция может иметь более одного декоратора
def square_it(func):
    def new_function(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * result
    return new_function


''' 
Декоратор, размещенный ближе всего к функции (прямо над def), будет выполнен первым, а затем - тот, что находится
сразу над ним. Любой порядок вызова вернет один и тот же конечный результат, но вы можете увидеть, как меняются 
промежуточные шаги
'''


@document_it
@square_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

# Поменяем порядок декораторов


@square_it
@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))
