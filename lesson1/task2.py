time = input('Введите время в секундах\n')

time = int(time)
time_second = time % 60
time_minutes = (time % 3600) // 60
time_hours = time // 3600

if time_second < 10:
    time_second = '0' + str(time_second)
else:
    time_second = str(time_second)

if time_minutes < 10:
    time_minutes = '0' + str(time_minutes)
else:
    time_minutes = str(time_minutes)

if time_hours < 10:
    time_hours = '0' + str(time_hours)
else:
    time_hours = str(time_hours)

print('Время в формате чч:мм:сс\n', time_hours, ':', time_minutes, ':', time_second)
