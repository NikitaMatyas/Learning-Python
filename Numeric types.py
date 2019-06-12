# Целые числа
print(5 + 8)
print(90 - 10)
print(4 * 7)

# Деление с плавающей точкой
print(7 / 2)

# Целочисленное деление
print(7 // 2)

# Вычисление остатка
print(7 % 3)

# Возведение в степень
print(3 ** 4)

# Частное и остаток одновременно
print(divmod(9, 5))

# Модуль числа
print(abs(5))

# Отрицательные числа
print(+123)
print(-123)

# Сокращение
a = 0
a += 5
print(a)

b = 4
b *= 2
print(b)

# Преобразование типов
print(int(5.42))

print(int('99'))
print(int('-23'))

# Автоматическое преобразование
print(4 + 7.0)

# Булевы переменные (boolean)
print(int(True))
print(int(False))

print(True + 2)
print(False - 4)

# Числа с плавающей точкой
print(float(True))
print(float(False))
print(float(4))
print(float('1.0e4'))

# Комплексные числа
x = complex(1, 2)
print(x)

y = complex(3, 4)
print(y)

z = x * y
print(z)

# Сопряженное число
print(x.conjugate())

# Мнимая часть
print(x.imag)

# Действительная часть
print(x.real)

# Можно проверить на равенство, но нельзя сравнить
print(x == y)

# Модуль комплексного числа
print(abs(3 + 4j))

# Возведение в степень
print(pow(3 + 4j, 2))
