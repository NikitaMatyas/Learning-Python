# Словари
# Порядок элементов в словаре не имеет значения, и они не выбираются с помощью смещения

# Создание словаря с помощью {}
empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses"
}
print(bierce)

# Преобразование с помощью функции dict()
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
d = dict(lol)
print(d)

tos = ('ab', 'cd', 'ef')
d = dict(tos)
print(d)

# Добавление или изменение элемента с помощью конструкции [key]
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}

pythons['Gilliam'] = 'Gerry'
print(pythons)

pythons['Gilliam'] = 'Terry'
print(pythons)

# Объединение словарей с помощью update()
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}

others = {'Marx': 'Groucho', 'Howard': 'Moe'}

pythons.update(others)
print(pythons)

# Удаление элементов по ключу с помощью del
del pythons['Marx']
del pythons['Howard']
print(pythons)

# Удаление всех элементов с помощью clear()
pythons.clear()
print(pythons)

# Проверка на наличие ключа с помошью in
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}

print('Chapman' in pythons)
print('QQQ' in pythons)

# Получение элемента словаря с помощью конструкции [ключ]
print(pythons['Cleese'])

# Как избежать exception если ключа нет в словаре с помощью get()
print(pythons.get('Cleese'))
print(pythons.get('QQQ'))

# Можно добавить сообщение для вывода
print(pythons.get('QQQ', 'Not in Python'))

# Получение всех ключей с помощью keys()
print(pythons.keys())

# Преобразование dict_keys полученных с помощью keys() в список
a = list(pythons.keys())
print(a)

# Получение всех значений с помощью функции values()
print(pythons.values())
a = list(pythons.values())
print(a)

# Получение всех пар <ключ - значение> с помощью функции items()
print(pythons.items())
a = list(pythons.items())
print(a)

# Присваивание значения с помощью оператора = (save_signals будет ссылаться на тот же объект)
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

# Копирование с помощью copy()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

