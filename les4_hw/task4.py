# Lesson 4 HomeWork - Task 4

"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def product(prev_el, el):
    return prev_el * el


user_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Числа от 100 до 1000 кратные 2: {user_list}")
print(f"Произведение всех этих чисел: {reduce(product, user_list)}")
