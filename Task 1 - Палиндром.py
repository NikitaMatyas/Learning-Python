s1 = input()
s2 = s1.lower()
s1 = s2.replace(' ', '')
s3 = ''
for i in range(0, len(s1), 1):
    if s1[i].isalpha():
        s3 += s1[i]
if s3 == s3[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
