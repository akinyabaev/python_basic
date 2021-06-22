"""
Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json.
"""

import requests
import json


username = 'akinyabaev'
password = '93298dd2f9166dd29172ed68b391977e81bd4f1e'

response = requests.get('https://api.github.com/user/repos', auth=(username, password))

with open('response.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, indent=2, ensure_ascii=False)

#Распечатка списка всех public репозиториев
for response in response.json():
    if not response['private']:
        print(response['html_url'])

