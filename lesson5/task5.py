"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def sum_numbers(number):
    number = number.split(" ")
    num_sum = 0
    try:
        for idx in number:
            num_sum += int(idx)
    except ValueError:
        print("Неверный символ")
    return num_sum

file = open("task5.txt", "w")
content = file.write(input("Введите числа через пробел\n"))
file.close()

file = open("task5.txt", "r")
line = file.readline()
result = sum_numbers(line)
print(f"Сумма чисел в файле: {result}")
file.close()
