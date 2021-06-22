"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
"""

from functools import reduce

a = [i for i in range(100, 1000) if i % 2 == 0]
multiplication_all = reduce(lambda x, y: x * y, a)
print(multiplication_all)
