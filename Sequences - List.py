# Списки
empty_list = []
print(empty_list)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekdays)

# Создание пустого списка с помощью функции list()
another_empty_list = list()
print(another_empty_list)

# Преобразование других типов данных в списки с помощью list()
print(list('cat'))

# Преобразование кортежа в список с помощью list()
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

# Преобразование строки в список с помощью split()
birthday = '1/6/1952'
print(birthday.split('/'))

# Получение элемента с помощью конструкции [смещение]
marxes = ['Groucho', 'Chicho', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[-1])

# Списки списков
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, carol_birds]
print(all_birds)

# Первым элементом списка списков будет список
print(all_birds[0])

# Первый/N элемент списка из списка списков
print(all_birds[0][0])
print(all_birds[1][2])

# Изменение элемента с помощью конструкции [смещение]
marxes_new = ['Groucho', 'Chicho', 'Harpo']
marxes_new[1] = 'Wanda'
print(marxes_new)

# Извлечение элементов списка с помощью диапазона смещений
marxes = ['Groucho', 'Chicho', 'Harpo']
print(marxes[0:2])

# Инверсия списка
print(marxes[::-1])

# Добавление элемента в конец списка с помощью append()
marxes.append('Zeppo')
print(marxes)

# Объединение списков с помощью extend() или +=
marxes = ['Groucho', 'Chicho', 'Harpo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chicho', 'Harpo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

# Добавление элемента с помощью insert()
marxes = ['Groucho', 'Chicho', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)

# Удаление заданного элемента с помощью del
marxes = ['Groucho', 'Chicho', 'Harpo']
del marxes[-1]
print(marxes)

# Удаление элемента по значению с помощью remove()
marxes = ['Groucho', 'Chicho', 'Harpo']
marxes.remove('Chicho')
print(marxes)

# Получение заданного элемента с помощью pop()
marxes = ['Groucho', 'Chicho', 'Harpo']
print(marxes.pop())

# Определение смещения элемента по значению с помощью index()
marxes = ['Groucho', 'Chicho', 'Harpo']
print(marxes.index('Chicho'))

# Проверка на наличие элемента в списке с помощью оператора in
marxes = ['Groucho', 'Chicho', 'Harpo']
print('Groucho' in marxes)
print('Hello' in marxes)

# Определение включения количества значений с помощью count()
marxes = ['Groucho', 'Chicho', 'Harpo', 'Harpo']
print(marxes.count('Harpo'))

# Преобразование списка в строку с помощью join()
marxes = ['Groucho', 'Chicho', 'Harpo']
print(', '.join(marxes))

# Изменение порядка элементов с помощью sort()
marxes = ['Groucho', 'Chicho', 'Harpo', 'A']
print(sorted(marxes))

# Получение длины списка с помощью len()
marxes = ['Groucho', 'Chicho', 'Harpo']
print(len(marxes))

# Присваивание с помощью оператора = (список B будет менять значение вместе с A, т.к. ссылается на тот же объект)
A = [1,2,3]
B = A
print(B)
A[0] = 'hello'
print(B)

# Копирование с помощью copy() (список B останется уникальным после изменения A)
A = [1,2,3]
B = A.copy()
print(B)
A[0] = 'hello'
print(B)










