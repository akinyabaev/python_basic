"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

import os

text = 'asdfkksadlkfsdl\n' \
       'sdfmknfg123 123j4k3j2 2314 234234\n' \
       'rewerf sdfasdfad fdg th trh r htyj wrg wer g g tg\n' \
       'ds 123 235  k lk 534 yt;p[w]w,trw\n'

file_path = os.path.join(os.path.dirname(__file__), 'task2.txt')

with open(file_path, 'w', encoding='UTF-8') as file:
    file.write(text)

lines_count = 0

with open(file_path, 'r', encoding='UTF-8') as file:
    for line in file:
        lines_count = lines_count + 1
        print(f'Строка номер {lines_count} содержит в себе {len(line.split())} слова')
    print(f'Всего строк в файле {lines_count}')
