"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]
"""

rating_list = [22, 6, 5]

while True:
    user_input = input('Введите новый рейтинг или q для выхода из цикла: \n')

    try:
        new_rating = abs(int(user_input))
    except ValueError as error:
        if user_input.lower() == 'q':
            print('Выход')
            break
        continue

    new_rating_count = rating_list.count(new_rating)

    if not new_rating_count:
        if new_rating > rating_list[0]:
            rating_list.insert(0, new_rating)
        elif new_rating < rating_list[-1]:
            rating_list.append(new_rating)
        else:
            for idx, itm in enumerate(rating_list):
                if itm < new_rating:
                    rating_list.insert(idx, new_rating)
                    break
    else:
        end_idx = rating_list.index(new_rating) + new_rating_count
        rating_list.insert(end_idx, new_rating)


    print(rating_list)