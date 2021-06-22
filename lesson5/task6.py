"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def numbers(data):
    num_list = []
    num = ' '
    summa = 0
    for char in data:
        index = data.index(":")
        subject = data[:index]
        if char.isdigit():
            num = num + char
        else:
            if num != ' ':
                num_list.append(int(num))
                num = ' '
    for itm in num_list:
        summa += itm
    return subject, summa

file = open("task6.txt", "r", encoding="utf-8")
data = file.readlines()

my_list = []
for itm in data:
    a, b = numbers(itm)
    my_list.append(a)
    my_list.append(b)

final_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}
print(final_dict)

file.close()
