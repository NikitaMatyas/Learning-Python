# Строки
print('Boom')
print('''Boom''')
print("""Boom""")

# Преобразование в строку
print(str(98.6))
print(str(1.0e4))
print(str(True))

# Переход на новую строку
print('A man\nA plan\nA canal')

# Табуляция
print('\tabc')

# Экранирование кавычек
print('\'abc\'')
print('\"abc\"')

# Обратный слеш
print('\\')

# Объединение строк с помощью +
print('Release the ' + 'kraken!')

# Размножение строк с помощью *
print('Hello ' * 4)

# Извлечение символа с помощью []
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])

# Извлечение последних символов
print(letters[-1])
print(letters[-2])

# Извлечение подстроки с помощью [ start : end : step ]
# Вся строка
print(letters[:])

# Получить символы, начиная с 20-го и заканчивая последним
print(letters[20:])

# Получить символы с 12-го по 14-й (Python не включает символ, расположенный под номером, который указан последним)
print(letters[12:15])

# Последние три символа
print(letters[-3:])

# Начать со смещения 18 и идти до четвертого с конца символа
print(letters[18:-3])

# Каждый седьмой символ с начала до конца
print(letters[::7])

# Каждый третий символ, начиная со смещения 4 и заканчивая 19-м символом
print(letters[4:20:3])

# Получение длины строки с помощью функции len()
print(len(letters))

# Разделение строки с помощью функции split()
todos = 'get gloves.get mask.give cat vitamins.call ambulance'
print(todos.split('.'))

# Объединение строк с помощью фунцкии join()
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster', 'Bigfoot']
crypto_string = ', '.join(crypto_list)
print(crypto_string)

# Проверка строки на соответствие с помощью функций startswith() и endswith()
print(crypto_string.startswith('Yeti'))
print(crypto_string.startswith('NoNoNo'))
print(crypto_string.endswith('Loch Ness Monster'))
print(crypto_string.endswith('Yes'))

# Поиск первого смещения с помощью функции find()
print(crypto_string.find('Bigfoot'))

# Поиск последнего смещения с помощью функции rfind()
print(crypto_string.rfind('Bigfoot'))

# Количество вхождений в строку
print(crypto_string.count('Bigfoot'))

# Являются ли все символы цифрами
print(crypto_string.isalnum())

# Удаление определенных символов с начала и конца строки
duck = '...A duck goes into a bar..'
print(duck.strip('.'))

# Сделать букву первого слова заглавной с помощью функции capitalize()
print('hello how are you'.capitalize())

# Сделать все буквы заглавными с помощью функции title()
print('hello how are you'.title())

# Все слова большими буквами с помощью функции upper()
print('hello how are you'.upper())

# Все слова маленькими буквами с помощью функции lower()
print('HELLO HOW ARE YOU'.lower())

# Смена регистра букв
print('hello how are you'.swapcase())
print('HeLLo HoW arE YOU'.swapcase())

# Отцентрировать строку в промежутке из 30 пробелов
print('A duck goes into a bar'.center(30))

# Выравнивание строки по левому/правому краю
print('A duck goes into a bar'.ljust(30))
print('A duck goes into a bar'.rjust(30))

# Замена символов с помощью функции replace()
print('A duck goes into a bar'.replace('duck', 'marmoset'))

# Замена до 100 включений
print('a duck goes into a bar'.replace('a ', 'a famous ', 100))

