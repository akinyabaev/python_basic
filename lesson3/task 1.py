"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

a = input('Введите числитель\n')
b = input('Введите знаменатель\n')


def func_dev(a, b):
    return a / b


try:
    a = int(a)
    b = int(b)
    try:
        print(func_dev(a, b))
    except ZeroDivisionError:
        print('Деление на ноль')

except ValueError as error:
    print('Неверный ввод')


