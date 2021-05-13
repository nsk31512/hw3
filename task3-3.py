'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
'''

def my_func(num1, num2, num3):
    max1 = max(num1, num2)
    max2 = max(num2, num3)
    return max1 + max2
