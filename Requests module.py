import requests

# Get запрос
r = requests.get('https://api.github.com/events')

# По принту получим просто код ответа
print(r)

# Получение содержимого ответа (response)
print(r.text)

# Содержимое ответа в JSON
print(r.json())

# Бинарное содержимое ответа
print(r.content)

# Необработанное содержимое ответа
print(r.raw)

# Проверка кода ответа
print(r.status_code)

# Передача параметров в URL
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.text)

# Post запрос
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print('-------------------------------------------------------------------------------------------------------------')
print(r.text)

# Пользовательские заголовки (headers) (значения заголовков должны быть string)
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.text)

# Передаем словарь в аргументе data, он будет закодирован как HTML форма, когда будет сделан запрос)
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print('-------------------------------------------------------------------------------------------------------------')
print(r.text)

''' Аргумент data также может иметь несколько значений для каждого ключа. Это можно сделать, указав data в формате 
tuple, либо в виде словаря со списками в качестве значений '''
print('-------------------------------------------------------------------------------------------------------------')
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('http://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('http://httpbin.org/post', data=payload_dict)
print(r1.text)
print(r1.text == r2.text)

# Если нужно отправить данные в неизмененном виде, то нужно передать в запрос строку вместо словаря

# Вместо кодирования словаря, можно передать его напрямую, используя параметр json, и он будет автоматически закодирован
print('-------------------------------------------------------------------------------------------------------------')
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
print(r.text)

# Параметр json игнорируется, если передаются data или files
# Использование json в запросе изменит заголовок Content-Type на application/json
print('-------------------------------------------------------------------------------------------------------------')

# Если был сделан неудачный запрос, то можно вызвать исключение с помощью r.raise_for_status()
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
# bad_r.raise_for_status()

# Но если status_code для r оказался 200, то при вызове raise_for_status() мы получаем None

print('-------------------------------------------------------------------------------------------------------------')
# Заголовки ответов (headers)
print(r.headers)

print('-------------------------------------------------------------------------------------------------------------')
# Получение доступа к cookies
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print(r.cookies)

print('-------------------------------------------------------------------------------------------------------------')
# Чтобы отправить cookies на сервер используется параметр cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)

print('-------------------------------------------------------------------------------------------------------------')
''' Cookies возвращаются в RequestsCookieJar, который работает как dict, но также предлагает более полный интерфейс, 
подходящий для использования в нескольких доменах или путях. Cookie jars могут также передаваться в запросы '''
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)

print('-------------------------------------------------------------------------------------------------------------')
# Редиректы и история
''' По умолчанию Requests будет выполнять редиректы для всех HTTP глаголов, кроме HEAD. Мы можем использовать свойство 
history объекта Response, чтобы отслеживать редиректы. Список Response.history содержит объекты Response, которые были 
созданы для того, чтобы выполнить запрос. Список сортируется от более ранних, до более поздних ответов. Например, GitHub 
перенаправляет все запросы HTTP на HTTPS:
'''

r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)

print('-------------------------------------------------------------------------------------------------------------')
# Можно отключить обработку редиректа с помощью allowed_redirects
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)
print(r.history)

print('-------------------------------------------------------------------------------------------------------------')
# Если использовать HEAD, то также можно включить редирект
r = requests.head('http://github.com', allow_redirects=True)
print(r.url)
print(r.history)

print('-------------------------------------------------------------------------------------------------------------')
# Тайм-ауты
''' Вы можете сделать так, чтобы Requests прекратил ожидание ответа после определенного количества секунд с помощью 
параметра timeout. Почти весь производственный код должен использовать этот параметр почти во всех запросах. 
Несоблюдение этого требования может привести к зависанию вашей программы 
Timeout это не ограничение по времени полной загрузки ответа. Исключение возникает, если сервер не дал ответ за timeout 
секунд (точнее, если ни одного байта не было получено от основного сокета за timeout секунд) '''
requests.get('http://github.com', timeout=5)

print('-------------------------------------------------------------------------------------------------------------')
# Ошибки и исключения
''' В случае неполадок в сети (например, отказа DNS, отказа соединения и т.д.), Requests вызовет исключение 
ConnectionError. Response.raise_for_status() вызовет HTTPError если в запросе HTTP возникнет статус код ошибки.
Если выйдет время запроса, вызывается исключение Timeout.
Если запрос превышает заданное значение максимального количества редиректов, то вызывают исключение TooManyRedirects.
Все исключения, которые вызывает непосредственно Requests унаследованы от requests.exceptions.RequestException. '''