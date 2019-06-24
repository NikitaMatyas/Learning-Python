# Обработка ошибок с помощью try и except

# Запускается код внутри блока try. Если произошла ошибка, генерируется исключение и выполняется код внутри except
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, 'but got', position)

# Можно получить объект исключения целиком в переменной
# Исключение IndexError сохраняется в переменной err, а другое исключение - в переменной other

short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

# Создание собственных исключений (стандартные исключения заранее определены в Python или его библиотеках)
# Любое исключение является классом, в частности потомком класса Exception


# Собственное исключение, которое вызывается, когда встречается слово, записанное в верхнем регистре
class UppercaseException(Exception):
    pass


words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)


# Можно получить доступ к самому объекту исключения и вывести его на экран
try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)
