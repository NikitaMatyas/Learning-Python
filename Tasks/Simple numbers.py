n = int(input('Введите размер: '))

for x in range(1, n+1):
    flag = False
    for b in range(2, x):
        if x % b == 0:
            flag = True
    if flag is False and x > 1:
        print(x)
