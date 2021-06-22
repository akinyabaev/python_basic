"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task1.txt')

with open(file_path, 'w', encoding='UTF-8') as file:
    while True:
        input_data = input('Введите данные для файла:\n')
        if not input_data:
            break
        file.write(f'{input_data}\n')

