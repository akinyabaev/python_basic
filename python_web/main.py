import requests

url = "https://www.google.ru"

response = requests.get(url)

if response.ok:
    pass

if response.status_code == 200:
    pass
else:
    pass

response.headers.get('Content-Type')

response.text   # Текстовое содержимое тела ответа от сервера

response.content   # Бинарное содержимое ответа от сервера

response.url

print()
