import json
import requests

'''
1. Выполнить get https://swapi.co/api/planets/
2. Проверить, что поле count равно 61
'''
print('Task 1:')

r = requests.get('https://swapi.co/api/planets/')
data = r.json()

if r.status_code == requests.codes.ok:
    if data["count"] == 61:
        print('Count = 61')
    else:
        print('Count != 61')
else:
    print('Cannot get data, status code is ', r.status_code)

''' 
1. Выполнить get https://swapi.co/api/planets/
2. Из запроса достать url первой планеты 
3. Выполнить get полученного url 
4. Проверить что status code 200
'''
print('\nTask 2:')

r = requests.get('https://swapi.co/api/planets/')
data = r.json()

FirstPlanetURL = data["results"][0]["url"]
print('URL of the first planet: ', FirstPlanetURL)

r = requests.get(FirstPlanetURL)
if r.status_code == requests.codes.ok:
    print('Status code is ', r.status_code)
    print('Response:\n', r.json())
else:
    print('Cannot get data, status code is ', r.status_code)

'''
1. Выполнить get https://swapi.co/api/films/
2. Из запроса достать названия фильмов titles 
'''
print('\nTask 3:')

r = requests.get('https://swapi.co/api/films/')
data = r.json()

if r.status_code == requests.codes.ok:
    for i in data["results"]:
        print(i["title"])
else:
    print('Cannot get data, status code is ', r.status_code)

'''
1. авторизоваться(ввести любой токен) https://openapi.appcenter.ms/#:
http://prntscr.com/js2kgp
http://prntscr.com/js2ktl
2. Использовать логин для любого метода post и выполнить post
пример https://api.appcenter.ms/v0.1/user/invitations/orgs/arsenal/reject
'''
print('\nTask 4:')

url = 'https://api.appcenter.ms/v0.1/user/invitations/orgs/qwerty/reject'
headers = {'X-API-Token': '123'}
r = requests.post(url, headers=headers)
print(r.text)
