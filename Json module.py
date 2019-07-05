import json
import requests

''' Как правило, процесс кодирования JSON называется сериализация. Этот термин обозначает трансформацию данных в серию 
байтов (следовательно, серийных) для хранения или передачи по сети. 
Естественно, десериализация — является противоположным процессом декодирования данных, которые хранятся или направлены 
в стандарт JSON. '''

# Сериализация JSON
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# dump() принимает два аргумента: 1 - объект данных, который сериализуется и 2 - файловый объект
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

# Также можно работать со строкой через dumps()
json_string = json.dumps(data)
print('\n', json_string)

# Использование indent для изменения отступа вложенных структур
json_string = json.dumps(data, indent=4)
print(json_string)

# Десериализация JSON с помощью load и loads
blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

print('\n', data)

# loads загружается только из строки!
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
} """

data = json.loads(json_string)
print('\n', data)

# Пример работы с JSON
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print('\n', todos)

# Вывод в удобном формате
print(json.dumps(todos, indent=4, sort_keys='True'))
