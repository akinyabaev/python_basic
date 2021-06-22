from sys import argv



try:
    _, hour, price, bonus, *__ = argv
    result = float(hour) * float(price) + float(bonus)
    print(result)

except ValueError:
    print('Некорректный ввод\n')