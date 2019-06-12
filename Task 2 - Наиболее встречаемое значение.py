list = []
result = set()
count = 0

print('Введите количество элементов списка')
n = input()

for i in range(0, int(n), 1):
    print('Введите элемент списка')
    list.append(input())
    if list.count(list[i]) > count:
        count = list.count(list[i])

for i in range(0, int(n), 1):
    if list.count(list[i]) == count:
        result.add(list[i])

print('Наиболее часто встречающиеся значения:')
print(*result)


