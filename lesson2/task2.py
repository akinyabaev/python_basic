"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

user_input = input('Введите список через запятую\n')
user_list = user_input.split(',')

idx = 0
stop = len(user_list) - 1

while idx < stop:
    user_list[idx] = user_list[idx + 1]
    user_list[idx + 1] = user_list[idx]
    idx += 2
print(user_list)

