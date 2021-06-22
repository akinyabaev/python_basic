"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

def profit(data):
    data = data.split(" ")
    profit = int(data[2]) - int(data[3])
    return profit

my_list = []

with open("task7.txt", "r", encoding="utf-8") as file:
    for line in file:
        number = profit(line)
        my_list.append(number)
    aver, count = 0, 0
    for itm in my_list:
        if itm > 0:
            aver += itm
            count += 1
    aver = aver / count
    my_list1 = [{"firm1": my_list[0], "firm2": my_list[1], "firm3": my_list[2]}, {"average_profit": aver}]

with open("task7.json", "w", encoding="utf-8") as file:
    json.dump(my_list1, file)


