"""
Если желаете использовать функцию из этого списка, надо написать ее аналог

sum()
map()
reduce()
min()
max()
enumerate()
zip()
"""


def my_sum(a: int, b: int) -> int:
    """My function for sum two element
    :param a int or float digit
    :param b int or float digit
    """
    return a + b

def some(a: int) -> float:
    return a ** 3

def my_map(func, iter_obj):
    print('f 1')
    for itm in iter_obj:
        print('f 2')
        yield func(itm)
        print('f 3')
        yield  itm + 5
    yield 'Some var'
    print('f 4')

b = my_map(some, [1, 2, 3, 4, 5])

while True:
    try:
        itm = next(b)
        print(itm)
    except StopIteration:
        break





