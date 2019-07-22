import json

# Преобразовать в массив
s = '["Коля", "Вася", "Петя"]'
a1 = json.loads(s)
print(a1)


# Преобразовать в JSON
s = {'a': 'aaa', 'b': 'bbb'}

a2 = json.dumps(s)
print(a2)


# Получить массив name из Json
'''
{
    "data" : [
        { "from": { "name" : "xxx", "age": "12" }, "message" : "yyy" },
        { "from": { "name" : "yyy", "age": "15" }, "message" : "sdfsd "},
        { "from": { "name" : "zzz", "age": "17" }, "message" : "sdfsdf "}
    ]
}
'''

rez = list()

with open('Task_6.json') as f:
    data = json.load(f)
for i in range(0, 3, 1):
    rez.append((data["data"][i]["from"]["name"]))

print(rez)
