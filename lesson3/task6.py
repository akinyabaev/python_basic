"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(word):
    word = word[0].upper() + word[1:]
    return word


input_str = input('Введите строку\n')

print(int_func(input_str))

input_words_string = input('Введиет слова через пробел\n').split(' ')
print(input_words_string)

for itm in input_str:
    itm = int_func(itm)


print(input_words_string)


