"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


file = open("task3.txt", "r")
content = file.read()

my_list = content.split()
my_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}

salary, count = 0, 0

for key, value in my_dict.items():
    if int(value) < 20000:
        print(f"Сотрудник {key} зарабатывает меньше 20000")
    salary += int(value)
    count += 1

print(f"Средняя зарплата сотрудников: {salary / count}")

file.close()