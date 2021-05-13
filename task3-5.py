'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
'''


def summator():
    sum_result = 0
    while True:
        numbers = input('Введите числа через пробел. Чтобы остановить программы введите "/". ')
        list_of_numbers = numbers.split(' ')
        if '/' in list_of_numbers:
            stop_index = list_of_numbers.index('/')
            list_of_numbers = list_of_numbers[:stop_index]
            total_in_local_list = sum(map(int, list_of_numbers))
            sum_result += total_in_local_list
            break
        total_in_local_list = sum(map(int, list_of_numbers))
        sum_result += total_in_local_list
    print(sum_result)


summator()
