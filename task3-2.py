'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
'''

def user_information (name, surname, birth_year, city_of_living, email, phone):
    print(f'Имя: {name}; Фамилия: {surname}; Год рождения: {birth_year};'
          f' Город проживания: {city_of_living}; E-mail: {email}; Телефон: {phone}')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth_year = input('Введите год рождения: ')
city_living = input('Введите город проживания: ')
email = input('Введите e-mail: ')
phone = input('Введите номер телефона: ')
user_information(name,surname, birth_year, city_living, email, phone)
