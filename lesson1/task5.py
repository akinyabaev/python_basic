profit = input('Введите выручку компании\n')
loses = input('Введите расходы компании\n')

profit = float(profit)
loses = float(loses)

if profit > loses:
    print('Компания работает с прибылью\n')
    proceeds = (profit - loses) / loses * 100
    print(proceeds, '%')
    staff = int(input('Введите кол-во сторуднико в компании\n'))
    proceeds_per_staff = proceeds / 100 / staff
    print('Выручка на 1 сотрудника составляет:\n', proceeds_per_staff)

else:
    print('Компания работает с убытком')


