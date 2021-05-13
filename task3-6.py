'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(some_text):
    text_list = list(some_text)
    ascii_code = ord(text_list[0])
    new_ascii_code = ascii_code - 32
    text_list[0] = chr(new_ascii_code)
    return ''.join(text_list)


some_text = input('Введите слово на латинице строчными буквами через пробел: ').split()
new_list = []
for word in some_text:
    word = int_func(word)
    new_list.append(word)
some_text = ' '.join(new_list)
print(some_text)
