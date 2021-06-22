"""
Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
"""

import requests
import json


username = 'akinyabaev'
password = '93298dd2f9166dd29172ed68b391977e81bd4f1e'

response = requests.get('https://api.vk.com/method/groups.get?v=5.52&access_token=b2b39b4ea0e72a07acb950d3f283ffcf23437adfa9302bb0229cc31598108c620653d28d3ffcc737284b2')

with open('response_2.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, indent=2, ensure_ascii=False)

