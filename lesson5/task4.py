"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


file = open("task4.txt", "r")

line = file.readline()
russian_1 = line.replace("One", "Один")

line = file.readline()
russian_2 = line.replace("Two", "Два")

line = file.readline()
russian_3 = line.replace("Three", "Три")

line = file.readline()
russian_4 = line.replace("Four", "Четыре")
file.close()

file = open("task4_new.txt", "w", encoding='utf-8')
str_list = [russian_1, russian_2, russian_3, russian_4]
file.writelines(str_list)
file.close()
