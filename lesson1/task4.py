number = input('Введите целое число\n')

i = 1
lenth = len(number)
number = int(number)

while i < lenth:
    maximum = 0
    if number % (10 ** i) // (10 ** (i - 1)) > (number % (100 ** i)) // (10 ** i):
        maximum = number % 10 ** i

    else:
        maximum = (number % 100 ** i) // 10 ** i
    i += 1
    print(maximum)

print(maximum)
