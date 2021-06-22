"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
"""


def my_func(*args):
    result = 0
    flag = False
    for itm in args:
        try:
            result += float(itm) if itm else 0
        except ValueError:
            if itm == 'q':
                flag = not flag
                break
    return  result, flag


user_input_sum = 0
while True:
    user_input = input('Введите числа через пробел\n').split(' ')
    result_sum, exit_flag = my_func(*user_input)
    user_input_sum += result_sum
    print(f'{user_input_sum}')

    if exit_flag:
        print('Выход')
        break

