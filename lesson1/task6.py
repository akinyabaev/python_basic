a = int(input('Начальное количество километров\n'))
b = int(input('Конечная дистанция\n'))

i = 0
while a * 1.1 ** i <= b:
    i += 1

print('Необходимое количество дней:', i+1)