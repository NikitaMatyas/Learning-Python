s1 = input()
s2 = s1.lower()
s1 = s2.replace(' ', '')
s2 = ''

for i in range(0, len(s1), 1):
    if s1[i].isalpha():
        s2 += s1[i]

if s2 == s2[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
