"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func (a: int, b: int, c: int) -> int :
    result = a + b
    if result < a + c or result < b + c:
        if a + c > b + c:
            result = a + c
        else:
            result = b + c

    return result


try:
    a = int(input())
    b = int(input())
    c = int(input())
    print(my_func(a, b, c))
except ValueError:
    print('Некорректный ввод')



