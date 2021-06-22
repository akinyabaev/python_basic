# e5e4cd692a72b0b66ea0a6b80255d1c3
# api.openweathermap.org/data/2.5/weather?q={city name}&appid=e5e4cd692a72b0b66ea0a6b80255d1c3

import requests

city_name = "Yakutsk"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=e5e4cd692a72b0b66ea0a6b80255d1c3"

response = requests.get(url)
j_data = response.json()

# print(response.text)

# print(j_data)

print(f"В городе {j_data.get('name')} температура {j_data.get('main').get('temp') - 273.15} градусов")


